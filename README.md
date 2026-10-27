# Monolithic 102 — ZOO Audit + Lean 4

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#lean-proofs-and-independent-audits)

<details open>
<summary><strong>On this page</strong></summary>

- [Final ZOO determination](#final-zoo-determination)
- [Package map](#package-map)
- [Reproduce](#reproduce)
- [Evidence boundary](#evidence-boundary)


</details>

**Related repositories:** [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW) · [EFMW](https://github.com/enuminous/EFMW) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) · [Nightengale-Full-Zoo-Audit](https://github.com/enuminous/Nightengale-Full-Zoo-Audit) · [Monlithic_EFMW_102_Lean4](https://github.com/enuminous/Monlithic_EFMW_102_Lean4) · [Cadence-Zoo-Evidence](https://github.com/enuminous/Cadence-Zoo-Evidence)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


> **Review boundary (2026-10-21):** The published ME-003 result is a **flat Cartesian specialization**, not a general curved-spacetime proof. Begin at the [independent review guide](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/REVIEW_START_HERE.md) and [claims register](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/CLAIMS_EVIDENCE_REGISTER.md). Do not interpret coverage counts as physical validation or infer an independently checked build from this documentation.


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
structural level. The remaining 49 are preserved in the canonical Lean catalog. A separate
[real and complex analysis package](analysis/COVERAGE.md) now gives 21 entries
explicit analytic models and 28 entries partial specializations or
counterexample results. None of those 49 remain catalogue-only. This does not
mean that all 102 source obligations have been fully formalized.
The [authored specifications](analysis/SPECIFICATIONS.md) resolve the dyad,
torus and null-pair constructions explicitly. Full source obligations and
physical/operator interpretations remain distinct from these results.
The [phase-current and Madelung proofs](analysis/MADELUNG.md) derive actual wave
derivatives, flat current conservation and the Schrödinger equivalence under
explicit assumptions for ME-018–021.
The [Cartesian vorticity model](analysis/VORTICITY.md) supplies ME-055's actual
curl operator, derivative identities and examples of spatially varying coupling.
The [ME-055/056 rotation and cosmology tranche](analysis/ROTATION_COSMOLOGY.md)
adds 54 theorems connecting planar algebra, actual rotation trajectories and
vorticity, then characterizing positive-scale cosmological branches, curvature
degeneracy, and explicit vacuum scale-factor solutions. The scalar/vector
normalization is explicit; a rotating-spacetime derivation remains open.
The [Cartesian fluid proofs](analysis/FLUIDS.md) add viscous-stress and momentum
identities for ME-077's partial specialization, plus ME-080's continuity
equivalence, an exact expanding-flow solution and counterexamples.
The [recursive Lagrangian proofs](analysis/RECURSIVE_LAGRANGIAN.md) derive
ME-011's state-space variation and Euler–Lagrange equation, establish the
autonomous energy law and distinguish its velocity-gap term from friction.
The [scalar action proofs](analysis/SCALAR_ACTION.md) establish the equivalence
between stationarity under compactly supported variations and the scalar field
equation for ME-009/013's fixed-background quadratic sector. They also expose
the source-sign condition needed to match ME-002; full gravitational and
quantum-gravitational action variations remain open.
The [linearized gravity proofs](analysis/LINEARIZED_GRAVITY.md) give ME-014/039
explicit differential operators, derive their contracted Bianchi identity,
reduce the equation in Lorenz gauge and prove necessary source conservation.
They also strengthen ME-015/040 with an actual scalar-stress divergence and
exchange law. These are flat linearized specializations; full nonlinear
geometry, quantum expectations and cognitive interpretations remain open.

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
