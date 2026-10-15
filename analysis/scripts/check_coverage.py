#!/usr/bin/env python3
"""Check the analytic overlay against the unchanged canonical catalogue."""
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parent
coverage = json.loads((HERE / "coverage.json").read_text())
canonical = json.loads((ROOT / "canonical/equations.json").read_text())
old = json.loads((ROOT / "zoo/equation-audit.json").read_text())
assert hashlib.sha256((ROOT / "canonical/CANONICAL_102.md").read_bytes()).hexdigest() == coverage["canonical_sha256"] == canonical["source_sha256"]
entries = coverage["entries"]
assert [e["id"] for e in entries] == [e["id"] for e in old["records"] if e["lean_status"] == "canonical_catalog"]
assert len(entries) == 49
formulas = {e["id"]: e["formula"] for e in canonical["equations"]}
source = (HERE / "CatalogueAnalysis.lean").read_text()
models = []
for e in entries:
    assert e["formula"] == formulas[e["id"]]
    assert e["status"] in {"open", "analytic_model"}
    if e["status"] == "analytic_model":
        models.append(e["id"])
        for kind in ["definition", "theorem"]:
            name = e[kind].split(".")[-1]
            assert re.search(r"\b(?:def|theorem) " + re.escape(name) + r"\b", source), e
assert models == [f"ME-{i:03d}" for i in [2, 4, 5, 16, 17, 26, 34, 46, 57, 60, 61, 92, 93]]
print("Canonical source unchanged; 49 entries tracked, 13 explicit analytic models, 36 open.")
print("The analytic models have the restrictions in COVERAGE.md; this is not a full-semantics count.")
