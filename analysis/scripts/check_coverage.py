#!/usr/bin/env python3
"""Check the analytic overlay against the unchanged canonical catalogue."""
import hashlib
import json
from pathlib import Path
import re
import tomllib

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
modules = ["CatalogueAnalysis", "SpecifiedModels", "Madelung", "Vorticity", "Fluids", "RecursiveLagrangian"]
assert sorted(p.stem for p in HERE.glob("*.lean") if p.name != "Audit.lean") == sorted(modules)
package = tomllib.loads((HERE / "lakefile.toml").read_text())
assert sorted(package["defaultTargets"]) == sorted(modules)
assert sorted(lib["name"] for lib in package["lean_lib"]) == sorted(modules)
audit = (HERE / "Audit.lean").read_text()
assert re.findall(r"^import (?!Lean$)(\w+)$", audit, re.M) == modules
assert re.search(r"let modules : Array Name := #\[(.*?)\]", audit).group(1) == ", ".join("`" + m for m in modules)
source = "\n".join((HERE / (name + ".lean")).read_text() for name in modules)
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
assert models == [f"ME-{i:03d}" for i in [2, 4, 5, 12, 16, 17, 26, 33, 34, 46, 55, 57, 59, 60, 61, 66, 80, 84, 87, 92, 93]]
assert partials == [f"ME-{i:03d}" for i in [3, 6, 7, 8, 10, 11, 15, 18, 19, 20, 21, 24, 36, 37, 40, 51, 52, 53, 54, 56, 67, 68, 77, 81]]
assert open_entries == [f"ME-{i:03d}" for i in [9, 13, 14, 39]]
me003 = next(e for e in entries if e["id"] == "ME-003")
assert me003["general_covariant_status"] == "open"
print("Canonical source unchanged; 49 entries tracked, 21 analytic models, 24 partial specializations, 4 without new analytic work.")
print("All six analytic modules are build targets and included in the declaration audit.")
print("ME-003 remains open for a complete covariant formalization; the flat theorem does not validate a physical interpretation.")
