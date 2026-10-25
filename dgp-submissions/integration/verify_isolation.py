"""Verify that an intake run cannot alter the surrounding benchmark repository."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path
HOME=Path(__file__).resolve().parents[1]
ROOT=HOME.parent

def snapshot():
    paths=subprocess.check_output(["git","ls-files","-z"],cwd=ROOT).decode().split("\0")
    result={}
    for name in paths:
        if not name or name=="CONTRIBUTING.md" or name.startswith(HOME.name+"/"):continue
        path=ROOT/name
        result[name]=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    return result

def main():
    path=ROOT/".git"/"dgp-protected-before.json"
    if sys.argv[1:]==["capture"]:
        current=snapshot();path.write_text(json.dumps(current,sort_keys=True),encoding="utf-8")
        print(f"Captured {len(current)} protected files before DGP processing.")
    elif sys.argv[1:]==["verify"]:
        before=json.loads(path.read_text(encoding="utf-8"));after=snapshot()
        if before!=after:
            changed=[p for p in set(before)|set(after) if before.get(p)!=after.get(p)]
            raise SystemExit("Protected files changed: "+", ".join(changed))
        print(f"Verified all {len(before)} protected files are byte-identical.")
    else:raise SystemExit("Usage: verify_isolation.py capture|verify")

if __name__=="__main__":main()
