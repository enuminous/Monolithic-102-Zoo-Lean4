# Real and complex catalogue models

This separate Lean 4.28 / Mathlib package gives **13 of the 49 catalogue-only
entries explicit analytic models**. The root Lean 4.19 package and its 53
discrete/structural entries are unchanged. This is a new layer of coverage;
it does not certify the full scientific interpretation of an entry.

The canonical source SHA-256 and exact formulas are locked in `coverage.json`.
The original per-equation obligations are retained there, including for the 36
entries without an analytic model. `CatalogueAnalysis.lean` is the acceptance
target. Read its hypotheses before applying a theorem.

| Entries | Fixed domain and mathematical result | Limits |
|---|---|---|
| 002, 004, 005 | Real C² scalar field on `Fin 4 → ℝ`, nonzero speed, signature (+---), actual Fréchet partial derivatives. Original and expanded solution predicates are equivalent. | Flat specialization; no curved metric, existence theorem, action derivation or physical source identification. The signs are preserved. |
| 016, 017 | Real amplitude/phase, complex exponential; squared modulus equals amplitude squared. | No Schrödinger or Madelung dynamics follows. |
| 026 | Real inner-product space, positive regularizer; absolute closure is strictly below one by Cauchy–Schwarz. | The vectors must actually represent the intended derivative/rate; that application is not proved. |
| 034 | Finite real mass table, natural logarithm, zero-mass term zero; entropy nonnegative on [0,1], point-mass entropy zero. | No inference from entropy to cognition or robustness. |
| 046 | Any real vector space and operator; exact expansion of the stated tiled operator. | No exceptional property of the golden ratio or arbitrary operator is assumed. |
| 057 | Four real density contributions; their sum is nonnegative when each is. | Identification of these terms and the cosmological equations remain open. |
| 060 | A bounded operator on a complex Hilbert space; the displayed adjoint/inner-product denominator equals the norm of the output. A nonzero output normalizes to norm one. | Zero output is excluded from the unit-norm result. Selection or physical interpretation of the operator remains open. |
| 061 | Finite complex amplitudes; squared-modulus weights are nonnegative and sum to one when an amplitude is nonzero. | The basis/operator interpretation and empirical Born-rule claim are not derived. |
| 092 | Finite normalized distributions, nonnegative P and strictly positive Q; KL divergence is nonnegative and vanishes on identical distributions. | Q=0 with P>0 requires extended-real divergence and is excluded. Equality characterization is not claimed. |
| 093 | Finite joint table and its two marginals; the entropy formula is symmetric under exchange. | Probability validity, information nonnegativity and independence characterization are separate results. |

The library does not import the separate EFMW-Lagrangian continuum package. Its
[existing bridge](https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/CONTINUUM_BRIDGE.md)
uses a different frozen action and signature; its minus-sign variational result
cannot silently replace the historical catalogue's equations.

## Remaining specification and derivation work

The 36 entries without a new analytic model are:

`003, 006–015, 018–021, 024, 033, 036–037, 039–040, 051–056,
059, 066–068, 077, 080–081, 084, 087`.

The ledger preserves each original obligation. In particular:

- Covariant tensors and action variations need a fixed Lorentzian geometry,
  field spaces, boundary conditions and a consistent sign/unit convention.
- Stochastic and nonlinear PDE claims need the noise law, solution notion,
  regularity and initial/boundary data.
- Optimizers need the state domain, objective and existence/tie conventions.
- ME-066 adds vectors and a tensor product from different spaces; embeddings
  must be specified before that sum has a type.
- ME-084 does not define `Torus(B888, φ)`. ME-087 needs the algebra, multiplication
  table and exact designated null pairs. No Lean proof can select these meanings
  on behalf of the source.

Analytic models do not erase unresolved application obligations. In particular, the flat ME-002 model is not a curved-space
formalization. This report does not relabel all 13 as fully completed semantics.

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
