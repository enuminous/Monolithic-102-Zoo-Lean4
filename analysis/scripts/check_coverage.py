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
source = "\n".join((HERE / name).read_text() for name in ["CatalogueAnalysis.lean", "SpecifiedModels.lean"])
models = []
partials = []
open_entries = []
for e in entries:
    assert e["formula"] == formulas[e["id"]]
    assert e["status"] in {"open", "analytic_model", "partial_specialization"}
    if e["status"] == "analytic_model":
        models.append(e["id"])
    elif e["status"] == "partial_specialization":
        partials.append(e["id"])
    else:
        open_entries.append(e["id"])
    if e["status"] in {"analytic_model", "partial_specialization"}:
        for kind in ["definition", "theorem"]:
            name = e[kind].split(".")[-1]
            assert re.search(r"\b(?:def|theorem) " + re.escape(name) + r"\b", source), e
assert models == [f"ME-{i:03d}" for i in [2, 4, 5, 12, 16, 17, 26, 33, 34, 46, 57, 59, 60, 61, 66, 84, 87, 92, 93]]
assert partials == [f"ME-{i:03d}" for i in [3, 6, 7, 8, 10, 15, 24, 36, 37, 40, 51, 52, 53, 54, 56, 67, 68, 81]]
assert len(open_entries) == 12
me003 = next(e for e in entries if e["id"] == "ME-003")
assert me003["general_covariant_status"] == "open"
print("Canonical source unchanged; 49 entries tracked, 19 analytic models, 18 partial specializations, 12 without new analytic work.")
print("ME-003 remains open for a complete covariant formalization; the flat theorem does not validate a physical interpretation.")
