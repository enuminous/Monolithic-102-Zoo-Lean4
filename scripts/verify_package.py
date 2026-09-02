#!/usr/bin/env python3
"""Static integrity checks that complement `lake build`."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
canonical = json.loads((ROOT / "canonical" / "equations.json").read_text(encoding="utf-8"))
audit = json.loads((ROOT / "zoo" / "equation-audit.json").read_text(encoding="utf-8"))

expected_ids = [f"ME-{number:03d}" for number in range(1, 103)]
canonical_ids = [record["id"] for record in canonical["equations"]]
audit_ids = [record["id"] for record in audit["records"]]
assert canonical["count"] == 102
assert audit["coverage"] == 102
assert canonical_ids == expected_ids
assert audit_ids == expected_ids

source_path = ROOT / "canonical" / "CANONICAL_102.md"
source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
assert source_digest == canonical["source_sha256"]

lean_files = sorted((ROOT / "Monolithic102").glob("ME[0-9][0-9][0-9].lean"))
assert len(lean_files) == 102

forbidden = re.compile(r"(?m)^\s*(axiom|opaque)\b|\b(sorry|admit)\b")
for path in (ROOT / "Monolithic102").rglob("*.lean"):
    match = forbidden.search(path.read_text(encoding="utf-8"))
    assert match is None, f"forbidden proof placeholder in {path}: {match.group(0)}"

print("PASS: 102 canonical IDs, 102 audit rows, 102 Lean namespaces, source hash matched, no proof placeholders")
