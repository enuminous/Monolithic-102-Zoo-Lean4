#!/usr/bin/env python3
"""Build the deterministic per-equation ZOO audit from frozen canonical inputs."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "canonical" / "equations.json"
PASS1 = ROOT / "zoo" / "PASS1_SOURCE.md"
OUT_JSON = ROOT / "zoo" / "equation-audit.json"
OUT_CSV = ROOT / "zoo" / "equation-audit.csv"
OUT_MD = ROOT / "zoo" / "ZOO_AUDIT.md"
OUT_LEAN = ROOT / "Monolithic102" / "ZooAudit.lean"

CLUSTERS = [
    (range(1, 2), "Framework signature", "SALMON → TORTOISE → SPIDER → WEASEL → TURTLE"),
    (range(2, 16), "Field/action", "SALMON → RAVEN → SPIDER → CHAMELEON → WEASEL → TURTLE"),
    (range(16, 22), "Quantum/Madelung", "RAVEN → WEAVER → SPIDER → WEASEL → TURTLE"),
    (range(22, 36), "Recursive control", "SALMON → SPIDER → DRAGON → OWL → CROCODILE → HEDGEHOG → TURTLE"),
    (range(36, 41), "Coupled nonlinear PDE", "SALMON → WEAVER → DRAGON → CHAMELEON → HEDGEHOG → TURTLE"),
    (range(41, 51), "Phi/coherence", "RAVEN → WEASEL → CHAMELEON → CAT → TURTLE"),
    (range(51, 59), "Emergence/cosmology", "SALMON → RAVEN → CHAMELEON → CROCODILE → TURTLE"),
    (range(59, 77), "Collapse/recursion/time", "SALMON → SPIDER → WEASEL → PHOENIX → AXOLOTL → TURTLE"),
    (range(77, 89), "Fluid/symbolic bases", "RAVEN → WEAVER → CHAMELEON → HEDGEHOG → TURTLE"),
    (range(89, 103), "Evaluation/epistemic", "SALMON → CAT → OWL → CROCODILE → HUMMINGBIRD → TURTLE"),
]

DEPENDENCIES = {
    5: [2, 4], 7: [6], 8: [6, 7], 13: [3, 10], 14: [13, 15], 15: [10],
    17: [16], 18: [16], 19: [18], 20: [16, 21], 21: [16],
    23: [22], 24: [22, 23, 25, 26], 26: [22, 23], 27: [22, 23, 26],
    28: [24, 27], 29: [28], 30: [29], 31: [22, 23, 24], 32: [31],
    33: [32], 35: [31], 37: [36], 39: [40], 42: [41], 43: [41, 42],
    44: [41], 45: [42, 43], 46: [41], 47: [22, 23], 48: [47],
    49: [47], 50: [49], 52: [27], 54: [53], 56: [55], 57: [56],
    58: [57], 60: [59], 61: [60], 63: [62], 64: [47], 65: [64],
    66: [65], 68: [67], 69: [70], 72: [71, 47], 73: [64], 74: [73],
    75: [64], 76: [75], 78: [77, 82], 79: [77], 80: [77], 81: [77, 78],
    82: [78], 84: [83, 41], 85: [41, 42], 86: [85], 87: [86],
    88: [85, 86], 89: [47], 90: [47, 94], 91: [45], 94: [47],
    95: [94], 96: [72, 95], 97: [98], 98: [47, 97], 99: [24, 26, 47],
    100: [99], 101: [47, 72], 102: [28, 29, 30],
}

TYPED_CORE = {
    1, 22, 23, 25, 27, 28, 29, 30, 31, 32, 35, 38, 41, 42, 43, 44,
    45, 47, 48, 49, 50, 58, 62, 63, 64, 65, 69, 70, 71, 72, 73, 74,
    75, 76, 78, 79, 82, 83, 85, 86, 88, 89, 90, 91, 94, 95, 96, 97,
    98, 99, 100, 101, 102,
}


def parse_pass1() -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    pattern = re.compile(r"^\| (ME-\d{3}) \| .*? \| (.*?) \| (.*?) \|$")
    for line in PASS1.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            rows[match.group(1)] = (match.group(2), match.group(3))
    return rows


def cluster_for(number: int) -> tuple[str, str]:
    for numbers, cluster, route in CLUSTERS:
        if number in numbers:
            return cluster, route
    raise ValueError(number)


def disposition(pass_class: str) -> tuple[str, str, str]:
    lower = pass_class.lower()
    if "standard-math reduction" in lower:
        return (
            "CONDITIONAL_STANDARD_SURVIVOR",
            "Recognizable standard relation; theorem requires explicit conventions and hypotheses.",
            "theorem_candidate",
        )
    if "typed" in lower:
        return (
            "STRUCTURAL_SURVIVOR",
            "Well-formed as a definition or predicate; this does not establish novelty or physical truth.",
            "definition_only",
        )
    if "empirical/model" in lower:
        return (
            "EMPIRICAL_TEST_REQUIRED",
            "No algebraic proof can establish performance or interpretation; decide with frozen external data.",
            "empirical_only",
        )
    return (
        "OPEN_SPECIFICATION",
        "Blocked pending explicit domains, units, operators, assumptions, and claimed derivation direction.",
        "blocked_by_semantics",
    )


def risks(eq: dict) -> list[str]:
    n, formula, title = eq["number"], eq["formula"], eq["title"].lower()
    found: list[str] = []
    if "/" in formula or "ρ" in formula and "∇²ρ" in formula:
        found.append("nonzero-denominator/domain conditions")
    if "lim" in formula or "→∞" in formula:
        found.append("limit existence and topology")
    if any(mark in formula for mark in ("∂", "∇", "d/dt", "d²")):
        found.append("regularity/boundary conditions")
    if n in {59, 97}:
        found.append("existence/uniqueness of optimizer")
    if n in set(range(41, 47)) | set(range(83, 89)):
        found.append("special-number privilege/invariance")
    if n in {26, 47, 48, 60, 61, 92}:
        found.append("normalization and zero-denominator behavior")
    if any(word in title for word in ("cognitive", "conscious", "legal", "ethical", "observer", "identity")):
        found.append("interpretive leap beyond mathematics")
    if n in set(range(28, 36)) | {57, 58, 61, 69, 72} | set(range(89, 103)):
        found.append("external validation and baseline dependence")
    return found or ["symbol/domain freeze"]


def failure_condition(result_code: str, risk_list: list[str]) -> str:
    primary = risk_list[0]
    if result_code == "EMPIRICAL_TEST_REQUIRED":
        return "Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets."
    if result_code == "CONDITIONAL_STANDARD_SURVIVOR":
        return f"Fails as written if the claimed reduction breaks under frozen conventions, especially {primary}."
    if result_code == "STRUCTURAL_SURVIVOR":
        return f"Fails as a useful construct if it is undefined, non-invariant, or non-identifying under {primary}."
    return f"Cannot advance until a complete specification resolves {primary}; inconsistent specifications reject it."


def main() -> None:
    source = json.loads(CANONICAL.read_text(encoding="utf-8"))
    pass1 = parse_pass1()
    equations = source["equations"]
    if len(equations) != 102 or len(pass1) != 102:
        raise SystemExit(f"coverage failure: canonical={len(equations)}, pass1={len(pass1)}")

    records = []
    for eq in equations:
        n, eid = eq["number"], eq["id"]
        pass_class, obligation = pass1[eid]
        result_code, result, proof_status = disposition(pass_class)
        cluster, route = cluster_for(n)
        risk_list = risks(eq)
        records.append({
            "number": n,
            "id": eid,
            "title": eq["title"],
            "classification": eq["classification"],
            "formula": eq["formula"],
            "cluster": cluster,
            "zoo_route": route,
            "pass1_class": pass_class,
            "result_code": result_code,
            "result": result,
            "proof_status": proof_status,
            "lean_status": "typed_core" if n in TYPED_CORE else "canonical_catalog",
            "dependencies": [f"ME-{d:03d}" for d in DEPENDENCIES.get(n, [])],
            "risk_flags": risk_list,
            "immediate_obligation": obligation,
            "failure_condition": failure_condition(result_code, risk_list),
        })

    wrapper = {
        "audit_name": "Monolithic 102 ZOO audit",
        "audit_version": "1.0.0",
        "canonical_source_sha256": source["source_sha256"],
        "coverage": len(records),
        "semantics": "Compilation proves only the stated Lean propositions, never empirical or physical validity.",
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(wrapper, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    fields = [
        "id", "title", "cluster", "pass1_class", "result_code", "proof_status",
        "lean_status", "dependencies", "risk_flags", "failure_condition",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = {key: record[key] for key in fields}
            row["dependencies"] = ";".join(row["dependencies"])
            row["risk_flags"] = ";".join(row["risk_flags"])
            writer.writerow(row)

    counts = Counter(record["result_code"] for record in records)
    lean_counts = Counter(record["lean_status"] for record in records)
    lines = [
        "# Monolithic 102 — ZOO Audit v1.0",
        "",
        "## Determination",
        "",
        "The 102-item corpus survives as a **versioned research program**, not as 102 proved laws. "
        "The ZOO separates standard reductions, typed constructs, empirical claims, and open specifications. "
        "No item is promoted merely because it compiles.",
        "",
        "## Coverage and disposition",
        "",
        f"- Canonical items audited: **{len(records)}/102**",
        f"- Conditional standard survivors: **{counts['CONDITIONAL_STANDARD_SURVIVOR']}**",
        f"- Structural/definitional survivors: **{counts['STRUCTURAL_SURVIVOR']}**",
        f"- Empirical tests required: **{counts['EMPIRICAL_TEST_REQUIRED']}**",
        f"- Open specifications: **{counts['OPEN_SPECIFICATION']}**",
        f"- Typed in the compile-checked core: **{lean_counts['typed_core']}**",
        f"- Preserved in the canonical Lean catalog: **{lean_counts['canonical_catalog']}**",
        "",
        "## ZOO protocol",
        "",
        "SALMON/TORTOISE freeze provenance; RAVEN identifies prior mathematics; WEAVER/SPIDER map structure "
        "and dependencies; WEASEL/CHAMELEON attack assumptions and representation dependence; DRAGON tests "
        "stability/attractors; OWL/CROCODILE test warning and causal claims; HEDGEHOG tests generalization; "
        "CAT checks consistency; PHOENIX/AXOLOTL test recovery; HUMMINGBIRD defines live monitoring; TURTLE "
        "retains only claims that survive at their proper evidence level.",
        "",
        "## Per-equation register",
        "",
        "| ID | Cluster | Result | Lean | Dependencies | Primary failure condition |",
        "|---|---|---|---|---|---|",
    ]
    for record in records:
        deps = ", ".join(record["dependencies"]) or "—"
        failure = record["failure_condition"].replace("|", "\\|")
        lines.append(
            f"| {record['id']} | {record['cluster']} | {record['result_code']} | "
            f"{record['lean_status']} | {deps} | {failure} |"
        )
    lines += [
        "",
        "## Hard boundary",
        "",
        "A successful `lake build` establishes parser/type/proof-kernel acceptance for the encoded objects only. "
        "It does not establish dimensional correctness, covariance, existence of physical solutions, empirical "
        "superiority, consciousness, legal validity, or a unified theory of nature.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    disposition_names = {
        "CONDITIONAL_STANDARD_SURVIVOR": "conditionalStandardSurvivor",
        "STRUCTURAL_SURVIVOR": "structuralSurvivor",
        "EMPIRICAL_TEST_REQUIRED": "empiricalTestRequired",
        "OPEN_SPECIFICATION": "openSpecification",
    }
    boundary_names = {
        "theorem_candidate": "theoremCandidate",
        "definition_only": "definitionOnly",
        "empirical_only": "empiricalOnly",
        "blocked_by_semantics": "blockedBySemantics",
    }
    lean_lines = [
        "import Monolithic102.Schema",
        "",
        "namespace Monolithic102",
        "",
        "/-- Machine-generated ZOO disposition for all 102 canonical equations. -/",
        "def zooAudit : Array AuditSpec := #[",
    ]
    for record in records:
        deps = ", ".join(str(int(dep[-3:])) for dep in record["dependencies"])
        lean_lines.append(
            "  { number := %d, canonicalId := \"%s\", disposition := ZooDisposition.%s, "
            "proofBoundary := ProofBoundary.%s, typedCore := %s, dependencies := [%s] },"
            % (
                record["number"], record["id"], disposition_names[record["result_code"]],
                boundary_names[record["proof_status"]],
                "true" if record["lean_status"] == "typed_core" else "false", deps,
            )
        )
    lean_lines += [
        "]",
        "",
        "theorem zooAudit_count : zooAudit.size = 102 := by native_decide",
        "",
        "end Monolithic102",
        "",
    ]
    OUT_LEAN.write_text("\n".join(lean_lines), encoding="utf-8")

    digest = hashlib.sha256(OUT_JSON.read_bytes()).hexdigest()
    print(f"generated {len(records)} records; audit_sha256={digest}")


if __name__ == "__main__":
    main()
