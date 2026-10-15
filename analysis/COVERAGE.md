# Real and complex catalogue models

This Lean 4.28 / Mathlib package tracks the 49 originally catalogue-only
entries: **19 explicit analytic models**, **22 partial specializations or
counterexample results**, and **8 without new analytic work**. The separate
root Lean 4.19 package and its 53 discrete/structural entries remain unchanged.
These categories are not a count of validated physical theories or fully
completed source obligations.

The canonical source SHA-256 and exact formulas remain locked in `coverage.json`.
Original obligations are retained. `CatalogueAnalysis.lean` and
`SpecifiedModels.lean` and `Madelung.lean` are the acceptance targets. The authored choices in
[SPECIFICATIONS.md](SPECIFICATIONS.md) resolve previously missing mathematical
definitions without attributing those choices to the historical source.

| Entries | Fixed domain and mathematical result | Limits |
|---|---|---|
| 002, 004, 005 | Real C² scalar field on `Fin 4 → ℝ`, nonzero speed, signature (+---), actual Fréchet partial derivatives. Original and expanded solution predicates are equivalent. | Flat specialization; no curved metric, existence theorem, action derivation or physical source identification. The signs are preserved. |
| 003 | Real C² scalar field in physical-time Cartesian coordinates; explicit inverse metric diag(1/c², −1, −1, −1), vanishing Christoffel symbols, and the full metric contraction. Theorem: this flat specialization equals the existing ME-004 operator. | Partial specialization only, with c ≠ 0. General curved-spacetime covariance remains open; no curved geometry is assumed or proved. |
| 016, 017 | Real amplitude/phase, complex exponential; squared modulus equals amplitude squared. | Dynamics does not follow from the polar identity alone; the separate ME-018–021 results state their evolution assumptions. |
| 018–021 | Actual polar-wave derivatives, the flat Klein–Gordon phase current and its conservation, and Schrödinger–Madelung equivalence with the quantum potential. | One time and one spatial coordinate; explicitly separate currents. Nonzero amplitude, hbar and mass for the Schrödinger equivalence; no arbitrary curved geometry or phase reconstruction. See [MADELUNG.md](MADELUNG.md). |
| 026 | Real inner-product space, positive regularizer; absolute closure is strictly below one by Cauchy–Schwarz. | The vectors must actually represent the intended derivative/rate; that application is not proved. |
| 033 | A nonzero perturbation's logarithmic norm-growth rate, an explicit exponential-orbit solution and its limit. A two-dimensional diagonal flow has unequal directional rates. | An arbitrary directional rate is not automatically the maximal exponent; general limit existence and maximization over directions are separate obligations. |
| 034 | Finite real mass table, natural logarithm, zero-mass term zero; entropy nonnegative on [0,1], point-mass entropy zero. | No inference from entropy to cognition or robustness. |
| 046 | Any real vector space and operator; exact expansion of the stated tiled operator. | No exceptional property of the golden ratio or arbitrary operator is assumed. |
| 057 | Four real density contributions; their sum is nonnegative when each is. | Identification of these terms and the cosmological equations remain open. |
| 059 | Nonempty finite state space, positive normalized probabilities and explicit divergence/reward. A minimizer exists; strict separation gives uniqueness, and a gap greater than twice uniform cost error preserves selection. | Infinite-state existence and physical collapse remain open. Constant cost disproves unconditional uniqueness; no tie rule is invented. |
| 060 | A bounded operator on a complex Hilbert space; the displayed adjoint/inner-product denominator equals the norm of the output. A nonzero output normalizes to norm one. | Zero output is excluded from the unit-norm result. Selection or physical interpretation of the operator remains open. |
| 061 | Finite complex amplitudes; squared-modulus weights are nonnegative and sum to one when an amplitude is nonzero. | The basis/operator interpretation and empirical Born-rule claim are not derived. |
| 092 | Finite normalized nonnegative distributions with support(P) contained in support(Q). KL is nonnegative and zero exactly when P=Q, including zero-mass entries. | Q=0 with P>0 requires extended-real divergence and remains excluded. |
| 093 | Finite normalized nonnegative joint distributions, including zero cells and marginals. Mutual information equals KL against the product of marginals, is nonnegative, and is zero exactly for independence. | This is finite probability mathematics, without an inference about cognition or empirical causality. |

The library does not import the separate EFMW-Lagrangian continuum package. Its
[existing bridge](https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/CONTINUUM_BRIDGE.md)
uses a different frozen action and signature; its minus-sign variational result
cannot silently replace the historical catalogue's equations.

## Additional explicit models and partial results

| Entries | Result | Scope |
|---|---|---|
| 012 | Antisymmetric electromagnetic tensor and the exact (electric² − magnetic²)/2 Lagrangian. | Flat Cartesian c=1, (+---); no Maxwell variation or dynamics. |
| 066 | Disjoint human/AI/tensor blocks; exact squared-norm formula; nonzero states normalize to squared norm one. | Finite complex coordinates and a specified Kronecker tensor realization. |
| 084 | Explicit centered torus map from a product of unit circles; injectivity for phi>1. | Authored center (8,8,8), radii 8*phi and 8; no claim that this is the uniquely intended source meaning. |
| 087 | Nonzero standard basis idempotents; product zero exactly at distinct indices; partition of unity. | Real coordinate algebra with zero divisors. |
| 006–008, 010, 015, 040, 067–068, 081 | Tensor symmetry, scalar-stress/Lagrangian relation, exact Einstein-residual expansion and decoupling. | Coordinate algebra only; arbitrary tensor inputs are not derived curvature or constitutive laws. |
| 024 | Actual derivative of the quartic potential and its dissipation along the specified ODE. | Constant gaps/forcing, positive relaxation time, deterministic sector; no stochastic existence result. |
| 036–037 | Homogeneous fixed points and positive growth above one. | Preserves the cubic sign; no unconditional damping or global PDE well-posedness is claimed. |
| 051–053 | Actual Hilbert-space gradients of the stated potentials. | Independent position/velocity coordinates; nonzero mass is the intended physical domain. |
| 054 | The plus-sign projector yields temporal force 2 for a unit rest vector/time gradient at beta=1. | A counterexample to orthogonal projection under (+---), not a silent sign repair. |
| 056 | Rotation term is nonnegative; a real H exists iff the right side is nonnegative. | No sign selection or cosmological evolution theorem. |

The 8 entries without new analytic work are:
`009, 011, 013–014, 039, 055, 077, 080`.
ME-003 still has only its flat specialization. Full curved-space covariance,
action variation, physical units, nonlinear/stochastic well-posedness and
implementation or empirical identification remain open where required by the
source obligations. The [Wright's Law field package](https://github.com/enuminous/Wrights-Law/blob/main/formal/PeriodicField.lean)
provides a separately specified periodic diffusion sector and constant-velocity
continuity equation; those theorems are not duplicated or relabeled as proofs of
all catalogue field equations.

## Verification

```sh
cd analysis
lake exe cache get
lake build
python3 scripts/check_coverage.py
lake env lean -DwarningAsError=true Audit.lean
python3 scripts/test_axiom_audit.py
```

The new workflow job checks this package separately from the root package. The
audit traverses every project declaration and permits only `propext`,
`Classical.choice` and `Quot.sound`; public/private axioms, placeholders and
native-reduction proof oracles must fail its controls. Coverage is demonstrated
only on a commit whose build and audits pass. These are standard mathematical
results under explicit assumptions, without a novelty or physical-validity claim.
