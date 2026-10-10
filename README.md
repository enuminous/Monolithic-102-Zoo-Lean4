# Monolithic 102 — ZOO Audit + Lean 4

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

This package freezes the canonical ME-001 through ME-102 corpus, runs a
per-equation adversarial ZOO classification, and supplies a compile-checked Lean
4 companion without treating compilation as scientific validation.

## Final ZOO determination

**Conditionally supported as a research program; not established as a unified
physical theory.**

| Disposition | Count | Meaning |
|---|---:|---|
| Conditional standard survivor | 15 | Recognizable standard mathematics; theorem obligations remain. |
| Structural survivor | 28 | Coherent as a definition or predicate; interpretation remains open. |
| Empirical test required | 12 | Only frozen external benchmarks can decide the claim. |
| Open specification | 47 | Domains, units, operators, assumptions, or derivations are incomplete. |
| **Total** | **102** | Every canonical ID is accounted for. |

The compile-checked typed core represents 53 equations at a discrete or
structural level. The remaining 49 are preserved in the canonical Lean catalog
and deliberately not given invented semantics.

## Package map

- `canonical/CANONICAL_102.md` — frozen canonical equation text.
- `canonical/equations.json` / `.ndjson` — machine-readable source.
- `zoo/ZOO_AUDIT.md` — full per-equation verdict and failure conditions.
- `zoo/equation-audit.json` / `.csv` — machine-readable audit.
- `Monolithic102/Catalog.lean` — all 102 source records.
- `Monolithic102/ZooAudit.lean` — all 102 ZOO dispositions in Lean.
- `Monolithic102/Formalized.lean` — typed core and kernel-checked theorems.
- `Monolithic102/ME001.lean` … `ME102.lean` — stable namespaces and canonical traceability.
- `THEOREM_REGISTER.md` — exact theorem claims.
- `BUILD_REPORT.md` — build environment and result.
- `legacy-mathlib/TURTLE-survivors/` — preserved prior Mathlib theorem tranche; not part of the dependency-free build target.

## Reproduce

```bash
python3 scripts/build_zoo_audit.py
lake update
lake build
```

The project is pinned by `lean-toolchain` to Lean 4.19.0 and has no external Lean
package dependencies.

## Evidence boundary

The package separates four distinct claims:

1. Canonical preservation: the source text and numbering were retained.
2. Formal typing: a formula has an explicit Lean domain and codomain.
3. Deductive proof: a proposition follows from encoded assumptions.
4. Scientific validation: predictions match independent observations.

Only the first three can be addressed by this repository. For ME-102 and every
other empirical item, acceptance still requires a preregistered baseline,
false-alarm budget, compute budget, held-out data, and independent replication.
