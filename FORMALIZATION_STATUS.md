# Formalization status

## Root archive coverage

- Canonical catalog: **102/102**
- Lean namespace files: **102/102**
- ZOO dispositions encoded in Lean: **102/102**
- Typed discrete/structural core: **53/102**
- Canonical-only pending semantics: **49/102**
- Kernel-checked structural theorems: **16**
- Axioms/placeholders in build target: **0**

## Why the typed core is discrete

The source does not yet freeze one shared analytic foundation for spacetime,
tensors, derivatives, measures, state-vector normalization, PDE boundary
conditions, or physical units. The compile-checked core therefore uses integer
discrete abstractions and explicit numerator/denominator records where division
conditions are unresolved. This makes the structural content checkable without
silently choosing physics on the author's behalf.

## What remains for theorem-level promotion

1. A dimensioned-units layer and sign/index conventions for ME-002–015.
2. Complex fields, smoothness, and measure/probability foundations for ME-016–021 and ME-059–061.
3. Normed state spaces, noise models, and existence/stability hypotheses for ME-022–035.
4. Function spaces and boundary/initial conditions for ME-036–040 and ME-077–082.
5. Invariance or necessity tests for φ/23/46/888 constructions.
6. Preregistered external datasets and baselines for empirical equations.

`needsSpecification` and `openSpecification` are not failures of the archive.
They are explicit proof obligations that prevent a source formula from being
mistaken for a theorem.

## Analytic overlay

The separate [analysis ledger](analysis/COVERAGE.md) tracks the 49 root catalogue
entries with 21 analytic models, 23 partial specializations/counterexamples and
5 entries without new analytic work. ME-018–021 now have the explicitly scoped
[phase-current and Madelung results](analysis/MADELUNG.md). The root archive counts above describe
its unchanged discrete layer. They do not supersede the newer overlay or claim
all source proof obligations are complete.

ME-055 now has a [Cartesian curl model](analysis/VORTICITY.md), including the
zero-curl and divergence identities, the product rule for scalar multiplication and explicit
rotation/coupling examples. Its physical source obligations remain open.

ME-077 now has a [partial Cartesian fluid specialization](analysis/FLUIDS.md)
with viscous-stress identities, pointwise nonnegative viscous work and the
continuity condition for conservative momentum. ME-080 has a three-dimensional
analytic continuity model and an explicit classical expanding-flow solution.
General fluid existence, relativistic geometry and empirical identification
remain open; the untouched entries are ME-009, ME-011, ME-013, ME-014 and ME-039.
