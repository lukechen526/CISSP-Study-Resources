#!/usr/bin/env python3
"""Check traceability, objective coverage, application checks, and local links."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content'
def normalized(s):
 s=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',s)
 return re.sub(r'\s+',' ',s.replace('*','').replace('`','')).strip().lower()

def main():
 records=[json.loads(s) for s in (CONTENT/'coverage.jsonl').read_text().splitlines()]
 summaries=json.loads((CONTENT/'coverage-summary.json').read_text())
 failures=[];total_objectives=0;total_subtopics=0
 for n in range(1,9):
  path=CONTENT/f'CISSP-Domain-{n}-Content.md';s=path.read_text();norm=normalized(s)
  source=next(ROOT.glob(f'CISSP-Domain-{n}-2024+Objectives.md'));original=source.read_text()
  if hashlib.sha256(source.read_bytes()).hexdigest()!=summaries[n-1]['source_sha256']:failures.append(f'Domain {n}: source changed since coverage snapshot')
  expected=set(re.findall(r'^## \[(\d+\.\d+)\]',original,re.M));actual=re.findall(r'^## (\d+\.\d+) ',s,re.M)
  if set(actual)!=expected or len(actual)!=len(expected):failures.append(f'Domain {n}: objective coverage mismatch')
  sub=set(re.findall(r'^\s*- (\d+\.\d+\.\d+)\s',original,re.M));actual_sub=re.findall(r'^### (\d+\.\d+\.\d+) ',s,re.M)
  if set(actual_sub)!=sub or len(actual_sub)!=len(sub):failures.append(f'Domain {n}: subtopic mismatch')
  total_objectives+=len(actual);total_subtopics+=len(actual_sub)
  if s.count('### Apply this objective')!=len(expected):failures.append(f'Domain {n}: missing application checks')
  ids=re.findall(r'<a id="([^"]+)"',s)
  if len(ids)!=len(set(ids)):failures.append(f'Domain {n}: duplicate anchors')
  for r in [r for r in records if r['domain']==n]:
   if r['anchor'] not in ids:failures.append(f'Domain {n} line {r["line"]}: missing destination')
   if r.get('rendered') and normalized(r['rendered']) not in norm:failures.append(f'Domain {n} line {r["line"]}: mapped text missing')
  for url in re.findall(r'\]\(([^\s]+)\)',s):
   if url.startswith(('https://','http://','mailto:')):continue
   filename,_,anchor=url.partition('#');target=path.parent/filename if filename else path
   if not target.exists():failures.append(f'Domain {n}: missing local file {url}')
   elif anchor and f'id="{anchor}"' not in target.read_text():failures.append(f'Domain {n}: missing anchor {url}')
 result={'domains':8,'objectives':total_objectives,'numbered_subtopics':total_subtopics,'mapped_source_lines':len(records),'application_checks':total_objectives,'failures':failures}
 print(json.dumps(result,indent=2))
 if failures:raise SystemExit(1)
if __name__=='__main__':main()
