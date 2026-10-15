# Real and complex catalogue models

This separate Lean 4.28 / Mathlib package gives **15 of the 49 catalogue-only
entries explicit analytic models** and adds one **partial flat-Minkowski
specialization** of ME-003. The root Lean 4.19 package and its 53
discrete/structural entries are unchanged. ME-003's general covariant
formalization remains open; the specialization does not supply curved-spacetime
assumptions. The package does not certify the full scientific interpretation
of any entry.

The canonical source SHA-256 and exact formulas are locked in `coverage.json`.
The original per-equation obligations are retained there, including for the 33
entries without new analytic work. `CatalogueAnalysis.lean` is the acceptance
target. Read its hypotheses before applying a theorem.

| Entries | Fixed domain and mathematical result | Limits |
|---|---|---|
| 002, 004, 005 | Real C² scalar field on `Fin 4 → ℝ`, nonzero speed, signature (+---), actual Fréchet partial derivatives. Original and expanded solution predicates are equivalent. | Flat specialization; no curved metric, existence theorem, action derivation or physical source identification. The signs are preserved. |
| 003 | Real C² scalar field in physical-time Cartesian coordinates; explicit inverse metric diag(1/c², −1, −1, −1), vanishing Christoffel symbols, and the full metric contraction. Theorem: this flat specialization equals the existing ME-004 operator. | Partial specialization only, with c ≠ 0. General curved-spacetime covariance remains open; no curved geometry is assumed or proved. |
| 016, 017 | Real amplitude/phase, complex exponential; squared modulus equals amplitude squared. | No Schrödinger or Madelung dynamics follows. |
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

## Remaining specification and derivation work

The 33 entries without new analytic work are:

`006–015, 018–021, 024, 036–037, 039–040, 051–056,
066–068, 077, 080–081, 084, 087`.

ME-003 has a partial flat-space specialization; its complete covariant
formalization remains open. The ledger preserves each original obligation. In particular:

- Covariant tensors and action variations need a fixed Lorentzian geometry,
  field spaces, boundary conditions and a consistent sign/unit convention.
- Stochastic and nonlinear PDE claims need the noise law, solution notion,
  regularity and initial/boundary data.
- ME-059 now has a finite-state existence and stability model. Infinite domains and a physical selection or tie mechanism still need definitions.
- ME-066 adds vectors and a tensor product from different spaces; embeddings
  must be specified before that sum has a type.
- ME-084 does not define `Torus(B888, φ)`. ME-087 needs the algebra, multiplication
  table and exact designated null pairs. No Lean proof can select these meanings
  on behalf of the source.

Analytic models do not erase unresolved application obligations. In particular,
the flat ME-002 model is not a curved-space formalization, and the ME-003
specialization does not complete its general covariant treatment. The 15
analytic models and the partial ME-003 specialization are not complete physical
or operator semantics.

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
