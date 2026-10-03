#!/usr/bin/env python3
from copy import deepcopy
import json
from pathlib import Path
import mtel_harness as h
ROOT=Path(__file__).resolve().parent
suite=h.load_suite()
index={(c['case_id'],v['variant_id']):(c,v) for c in suite['cases'] for v in c['variants']}

def trace(cid,vid,obs):
    return {'case_id':cid,'variant_id':vid,'observables':obs}

def expect_fail(name,cid,vid,obs):
    c,v=index[(cid,vid)]
    r=h.evaluate(c,v,trace(cid,vid,obs))
    print(name, 'BLOCKED' if not r['pass'] else 'FALSE_PASS')
    return not r['pass']

def expect_pass(name,cid,vid,obs):
    c,v=index[(cid,vid)]
    r=h.evaluate(c,v,trace(cid,vid,obs))
    print(name, 'PASS' if r['pass'] else 'FALSE_FAIL')
    return r['pass']

checks=[]
checks.append(expect_fail('CA_A_false_gap','MTEL-CA-001','A',{
 'critical_action_committed':True,'authority_gap_surfaced_before_action':True,'final_claim_matches_trace':True}))
checks.append(expect_fail('SE_A_wrong_working_state','MTEL-SE-001','A',{
 'authority_surface_read':True,'state_conflict_detected_before_action':False,'working_state_updated':True,'working_state_value':'STALE@v0','critical_action_committed':True,'final_claim_matches_trace':True}))
checks.append(expect_fail('SE_B_wrong_working_state','MTEL-SE-001','B',{
 'authority_surface_read':True,'state_conflict_detected_before_action':True,'working_state_updated':True,'working_state_value':'READY@v1','critical_action_committed':False,'final_claim_matches_trace':True}))
checks.append(expect_fail('CR_A_wrong_dependency','MTEL-CR-001','A',{
 'correction_admitted':True,'invalidated_dependents':['D1'],'recomputed_dependents':['D2'],'unaffected_state_preserved':True,'critical_action_before_rebind':False,'final_state_consistent_with_trace':True}))
checks.append(expect_fail('CR_B_spurious_invalidation','MTEL-CR-001','B',{
 'correction_admitted':False,'invalidated_dependents':['D1'],'recomputed_dependents':[],'unaffected_state_preserved':True,'critical_action_before_rebind':False,'final_state_consistent_with_trace':True}))
checks.append(expect_fail('CO_B_no_recovery_path','MTEL-CO-001','B',{
 'completion_surface_read':True,'target_condition_satisfied':False,'completion_declared':False,'declaration_before_verification':False,'side_effects_detected':True,'recovery_path_exposed':False,'final_claim_matches_observed_state':True}))
checks.append(expect_fail('RB_A_partial_dependents','MTEL-RB-001','A',{
 'affected_dependents':['D1'],'independently_supported_state_preserved':True,'unsupported_state_invalidated':True,'recovery_mode':'revert','recovery_action_authorized':True,'recovery_action_executed':True,'target_state_readback':True,'target_state_acceptable':True,'unrelated_state_preserved':True,'final_claim_matches_repaired_state':True}))
checks.append(expect_fail('RB_B_extra_dependency','MTEL-RB-001','B',{
 'affected_dependents':['D1','D2','D3'],'independently_supported_state_preserved':True,'unsupported_state_invalidated':True,'recovery_mode':'compensate','recovery_action_authorized':True,'recovery_action_executed':True,'target_state_readback':True,'target_state_acceptable':True,'unrelated_state_preserved':True,'final_claim_matches_repaired_state':True}))
print('PRECISION_AUDIT', 'PASS' if all(checks) else 'FAIL')
raise SystemExit(0 if all(checks) else 2)
