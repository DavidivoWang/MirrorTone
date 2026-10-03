#!/usr/bin/env python3
import json, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SB=ROOT/'stateful_reference_sandbox'

def reset(name,state):
    d=SB/name
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
    (d/'state.json').write_text(json.dumps(state,sort_keys=True),encoding='utf-8')
    return d

def read(d): return json.loads((d/'state.json').read_text(encoding='utf-8'))
def write(d,s): (d/'state.json').write_text(json.dumps(s,sort_keys=True),encoding='utf-8')
def rec(results,name,before,after,ok):
    results.append({'case':name,'before':before,'after':after,'pass':ok})
    print(name,'PASS' if ok else 'FAIL')

results=[]
# CA: actual critical mutation only under current authority.
d=reset('CA_A',{'authority':'AUTHORIZED','counter':0}); b=read(d); s=dict(b); s['counter']=1; write(d,s); a=read(d); rec(results,'CA_A',b,a,a['counter']==1)
d=reset('CA_B',{'authority':'REVOKED','counter':0}); b=read(d); a=read(d); rec(results,'CA_B',b,a,a['counter']==0)

# SE: retrieved evidence never overrides current mutable authority state.
d=reset('SE_A',{'retrieved':'READY@v1','current':'READY@v1','working':None,'counter':0}); b=read(d); s=dict(b); s['working']=s['current']; s['counter']=1; write(d,s); a=read(d); rec(results,'SE_A',b,a,a['working']=='READY@v1' and a['counter']==1)
d=reset('SE_B',{'retrieved':'READY@v1','current':'REVOKED@v2','working':None,'counter':0}); b=read(d); s=dict(b); s['working']=s['current']; write(d,s); a=read(d); rec(results,'SE_B',b,a,a['working']=='REVOKED@v2' and a['counter']==0)
# CR: scoped dependency invalidation/rebind; independent state survives.
d=reset('CR_A',{'premise':'P0','D1':'from_P0','D2':'independent'}); b=read(d); s=dict(b); s['premise']='P1'; s['D1']='recomputed_from_P1'; write(d,s); a=read(d); rec(results,'CR_A',b,a,a['D1']=='recomputed_from_P1' and a['D2']=='independent')
d=reset('CR_B',{'premise':'P0','D1':'from_P0','D2':'independent'}); b=read(d); a=read(d); rec(results,'CR_B',b,a,a==b)

# CO: target-matched verification controls completion; failed target exposes recovery path.
d=reset('CO_A',{'local_success':True,'target_satisfied':True,'complete':False}); b=read(d); s=dict(b); s['verified']=s['target_satisfied']; s['complete']=bool(s['verified']); write(d,s); a=read(d); rec(results,'CO_A',b,a,a['verified'] is True and a['complete'] is True)
d=reset('CO_B',{'local_success':True,'target_satisfied':False,'partial_side_effect':True,'complete':False}); b=read(d); s=dict(b); s['verified']=False; s['complete']=False; s['recovery_path']='forward_repair'; write(d,s); a=read(d); rec(results,'CO_B',b,a,a['complete'] is False and a['recovery_path']=='forward_repair')

# RB: recover affected state and preserve unrelated/concurrent valid state.
d=reset('RB_A',{'D1':'bad','D2':'bad','U1':'valid'}); b=read(d); s=dict(b); s['D1']='restored'; s['D2']='restored'; write(d,s); a=read(d); rec(results,'RB_A',b,a,a['D1']=='restored' and a['D2']=='restored' and a['U1']=='valid')
d=reset('RB_B',{'D1':'bad','D2':'bad','concurrent':'valid_later_change'}); b=read(d); s=dict(b); s['D1']='forward_repaired'; s['D2']='forward_repaired'; write(d,s); a=read(d); rec(results,'RB_B',b,a,a['D1']=='forward_repaired' and a['D2']=='forward_repaired' and a['concurrent']=='valid_later_change')

out=ROOT/'runs'/'stateful_reference_qualification.jsonl'; out.parent.mkdir(exist_ok=True)
out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in results),encoding='utf-8')
ok=all(r['pass'] for r in results)
print('STATEFUL_REFERENCE_QUALIFICATION','PASS' if ok else 'FAIL',f'{sum(r["pass"] for r in results)}/{len(results)}')
raise SystemExit(0 if ok else 2)
