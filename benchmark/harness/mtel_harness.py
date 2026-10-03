#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES_PATH = ROOT / "cases.json"


def load_suite():
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    for key in ("schema_version", "suite_id", "status", "pairing_rule", "cases"):
        if key not in data:
            raise ValueError(f"missing suite field: {key}")
    seen = set()
    for case in data["cases"]:
        for key in ("case_id", "title", "dimension", "source_spec", "variants"):
            if key not in case:
                raise ValueError(f"{case.get('case_id', '<unknown>')}: missing {key}")
        if case["case_id"] in seen:
            raise ValueError(f"duplicate case_id: {case['case_id']}")
        seen.add(case["case_id"])
        vids = set()
        for variant in case["variants"]:
            for key in ("variant_id", "label", "controlled_delta", "setup", "prompt", "environment", "required_observables", "assertions"):
                if key not in variant:
                    raise ValueError(f"{case['case_id']}: variant missing {key}")
            if variant["variant_id"] in vids:
                raise ValueError(f"{case['case_id']}: duplicate variant {variant['variant_id']}")
            vids.add(variant["variant_id"])
    return data


def get_path(obj, path):
    current = obj
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None, False
        current = current[part]
    return current, True


def check(trace, assertion):
    value, exists = get_path(trace, assertion["path"])
    op = assertion["op"]
    expected = assertion.get("value")
    if op == "eq":
        ok = exists and value == expected
    elif op == "neq":
        ok = exists and value != expected
    elif op == "in":
        ok = exists and value in expected
    elif op == "not_in":
        ok = exists and value not in expected
    elif op == "nonempty":
        ok = exists and value not in (None, "", [], {})
    elif op == "empty":
        ok = exists and value in (None, "", [], {})
    else:
        return False, {"error": f"unknown op {op}"}
    return ok, {"path": assertion["path"], "op": op, "expected": expected, "actual": value, "exists": exists}


def evaluate(case, variant, trace):
    errors = []
    if trace.get("case_id") != case["case_id"]:
        errors.append("case_id mismatch")
    if trace.get("variant_id") != variant["variant_id"]:
        errors.append("variant_id mismatch")
    observables = trace.get("observables")
    if not isinstance(observables, dict):
        errors.append("observables must be object")
        observables = {}
    missing = [key for key in variant["required_observables"] if key not in observables]
    if missing:
        errors.append("missing observables: " + ", ".join(missing))
    checks = []
    for assertion in variant["assertions"]:
        ok, detail = check(trace, assertion)
        checks.append({"pass": ok, **detail})
    return {
        "case_id": case["case_id"],
        "variant_id": variant["variant_id"],
        "pass": not errors and all(item["pass"] for item in checks),
        "errors": errors,
        "checks": checks,
    }


def request_for(case, variant, agent_id):
    return {
        "schema_version": "0.1",
        "case_id": case["case_id"],
        "variant_id": variant["variant_id"],
        "title": case["title"],
        "dimension": case["dimension"],
        "agent_id": agent_id,
        "setup": variant["setup"],
        "prompt": variant["prompt"],
        "environment": variant["environment"],
        "required_observables": variant["required_observables"],
        "trace_contract": {
            "required_top_level": ["schema_version", "case_id", "variant_id", "run_id", "agent_id", "events", "observables", "final_response"],
            "event_types": ["read", "decision", "action", "claim", "recovery", "other"],
        },
    }


def selected(suite, ids):
    wanted = None if not ids or "all" in ids else set(ids)
    for case in suite["cases"]:
        if wanted is None or case["case_id"] in wanted:
            for variant in case["variants"]:
                yield case, variant


def invoke(command, request, timeout):
    use_shell = os.name == "nt"
    argv = command if use_shell else shlex.split(command)
    if not argv:
        raise ValueError("empty agent command")
    process = subprocess.run(
        argv,
        input=json.dumps(request, ensure_ascii=False),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
        shell=use_shell,
    )
    if process.returncode != 0:
        raise RuntimeError(f"agent command failed rc={process.returncode}: {process.stderr.strip()}")
    try:
        trace = json.loads(process.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"agent stdout must be one JSON trace: {exc}") from exc
    return trace, process.stderr.strip()


def run_suite(suite, command, agent_id, ids, timeout, out_path):
    results = []
    records = []
    for case, variant in selected(suite, ids):
        request = request_for(case, variant, agent_id)
        trace, stderr = invoke(command, request, timeout)
        result = evaluate(case, variant, trace)
        record = {"request": request, "trace": trace, "evaluation": result}
        if stderr:
            record["agent_stderr"] = stderr
        records.append(record)
        results.append(result)
        print(f"{case['case_id']}:{variant['variant_id']} {'PASS' if result['pass'] else 'FAIL'}")
    if out_path:
        path = Path(out_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records), encoding="utf-8")
    overall = bool(results) and all(result["pass"] for result in results)
    print(f"OVERALL {'PASS' if overall else 'FAIL'}")
    return 0 if overall else 2


def main():
    parser = argparse.ArgumentParser(description="MTEL Governance Benchmark Harness v0.1")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("selftest")

    run = sub.add_parser("run")
    run.add_argument("--agent-cmd", required=True)
    run.add_argument("--agent-id", default="candidate-agent")
    run.add_argument("--case", action="append", default=[])
    run.add_argument("--timeout", type=int, default=120)
    run.add_argument("--out", default="")

    evaluate_cmd = sub.add_parser("evaluate")
    evaluate_cmd.add_argument("--traces", required=True)

    args = parser.parse_args()
    suite = load_suite()

    if args.cmd == "validate":
        print(json.dumps({
            "suite": suite["suite_id"],
            "cases": len(suite["cases"]),
            "variants": sum(len(case["variants"]) for case in suite["cases"]),
            "valid": True,
        }, indent=2))
        return 0

    if args.cmd == "selftest":
        mock = f"{shlex.quote(sys.executable)} {shlex.quote(str(ROOT / 'mock_agent.py'))}"
        return run_suite(suite, mock, "protocol-smoke", [], 30, "")

    if args.cmd == "run":
        return run_suite(suite, args.agent_cmd, args.agent_id, args.case, args.timeout, args.out)

    if args.cmd == "evaluate":
        index = {(case["case_id"], variant["variant_id"]): (case, variant) for case in suite["cases"] for variant in case["variants"]}
        failures = 0
        for line in Path(args.traces).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            obj = json.loads(line)
            trace = obj.get("trace", obj)
            key = (trace.get("case_id"), trace.get("variant_id"))
            if key not in index:
                print(json.dumps({"pass": False, "error": "unknown case/variant", "key": key}))
                failures += 1
                continue
            case, variant = index[key]
            result = evaluate(case, variant, trace)
            print(json.dumps(result, ensure_ascii=False))
            failures += 0 if result["pass"] else 1
        return 0 if failures == 0 else 2

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
