# Scalar action: variation and field equation

This round treats the scalar sector shared by ME-009, ME-010 and ME-013.
The canonical equations and signs remain unchanged. The target is a partial
specialization, not a formalization of gravity or quantum gravity.

## Conventions fixed before implementation

Use real Cartesian four-space, coordinates `(t,x,y,z)`, c=1 and signature
(+---), consistent with the existing catalogue analysis. Hold the metric,
matter, electromagnetic, memory and environment fields fixed. Specialize the
potential to `V(phi) = m2 * phi^2 / 2`, with a real coefficient m2, and the
recursive coupling to a prescribed continuous scalar source J multiplying phi.
For ME-013 this means J=lambda*I with lambda constant and I independent of phi.
For ME-009 it is an explicitly chosen scalar slice of Lrec, not a derivation
of a covariant coupling from the state-space ME-011 expression.

The scalar density is

`L = -1/2 * sum_mu s_mu*(partial_mu phi)^2 - m2/2*phi^2 + J*phi`,

where s=(1,-1,-1,-1), and every partial is an actual Frechet derivative.
The other sectors are independent of the varied scalar in this specialization.

## Acceptance targets

1. Derive the exact density expansion under phi -> phi + epsilon*h.
2. Define the integrated density difference for compactly supported smooth
   variations. Prove its integrability and actual epsilon derivative; do not
   assume differentiation under the integral or an integration-by-parts rule.
3. Derive integration by parts from Mathlib's proved Haar-measure theorem.
   Compact support supplies the absence of a boundary contribution.
4. Prove stationary action under every compactly supported smooth variation
   if and only if the classical residual `box(phi)-m2*phi+J` vanishes, with
   C2 regularity and continuous J. The reverse implication must use the
   fundamental lemma rather than assume a pointwise equation from a weak one.
5. Relate the density to the existing scalar Lagrangian and the existing
   d'Alembertian; check the source sign against ME-002 without changing it.
6. State the absolute-action result only under actual integrability assumptions.

The complete source obligations remain open: metric variation, curvature,
covariance on general manifolds, joint dynamics of the other sectors,
general nonlinear potentials, boundary geometries, physical units, general
PDE existence and uniqueness, quantization, and empirical interpretation.
These targets are standard calculus of variations, not a novelty claim.

## Mathematical result

`ScalarAction.lean` contains 35 explicit theorem statements in the namespace
`MonolithicAnalysis.ScalarAction`. Let phi be C2 on real Cartesian four-space
and J continuous. Let h be a smooth compactly supported real variation. Define

```text
Delta S(epsilon) = integral [L(phi + epsilon*h) - L(phi)] d4x
E(phi) = box(phi) - m2*phi + J
```

The integral defining Delta S is proved integrable for every real epsilon.
The exact expansion is

```text
Delta S(epsilon)
  = epsilon * integral [-sum_mu s_mu*(partial_mu phi)*(partial_mu h)
                       - m2*phi*h + J*h] d4x
    + epsilon^2 * integral L(m2, J=0, h) d4x.
```

Differentiating this proved polynomial gives the actual derivative at zero.
Integration by parts then gives

```text
Delta S'(0) = integral E(phi)*h d4x.
```

The main theorem proves both directions:

**The action is stationary under every smooth compactly supported variation
if and only if E(phi)=0 at every spacetime point.**

The necessity direction applies Mathlib's fundamental lemma to obtain
almost-everywhere vanishing, then uses continuity and the positive Lebesgue
measure of nonempty open sets to obtain pointwise vanishing. Neither
integration by parts nor the desired field equation is an assumed hypothesis.
The first-variation and integrability results need only C1 variations;
stationarity is tested against the smaller standard class of smooth compact
variations.

For a compactly supported C1 background scalar, the module also proves the
absolute action is integrable and derives its actual first derivative. For a
general C2 background, only the integrated density difference is used; a
possibly infinite unperturbed action is not assigned a finite physical value
through Lean's totalized integral. An arbitrary background density independent
of phi cancels before integration. This covers fixed other sectors, not their
equations of motion.

## Proof register

| Theorems | Result |
|---|---|
| `partial_perturb`, `pairing_expansion`, `density_expansion` | Actual partial derivatives and exact quadratic variation. |
| `partial_contDiff`, `partial_compact`, `integrable_product` | Regularity, support and integrability infrastructure. |
| `pairing_integrable`, `variation_integrable`, `density_integrable`, `change_integrable` | Explicit existence of each integral used in the derivation. |
| `action_change_expansion`, `action_change_hasDerivAt` | Integrated polynomial and actual epsilon derivative. |
| `box_eq_sum`, `residual_continuous` | Agreement with the existing d'Alembertian and continuous classical residual. |
| `partial_integration_by_parts`, `pairing_integration_by_parts`, `first_variation_eq_residual` | Proved compact-variation integration by parts and Euler-Lagrange first variation. |
| `stationary_iff_firstVariation_zero`, `stationary_iff_residual_zero` | Actual stationarity, weak form and pointwise equation are equivalent under the stated regularity. |
| `absolute_action_difference`, `absolute_action_hasDerivAt`, `fixed_background_cancels` | Absolute-action derivative when integrable, and cancellation of independent sectors before integration. |
| `contraction_eq_pairing`, `density_eq_catalogue_scalar` | Bridge to the existing ME-010 scalar Lagrangian at c=1. |
| `prescribed_source_stationary_iff`, `dependent_source_derivative`, `dependent_source_counterexample` | Exact ME-013 prescribed-source specialization and a check of the omitted product term if the source depends on phi. |
| `massless_source_match` | Exact condition for matching ME-002 in the c=1, alpha=0, massless sector. |
| `time_quadratic_smooth`, `time_quadratic_partial`, `time_quadratic_second`, `time_quadratic_box` | An explicit C-infinity spacetime field with computed actual derivatives. |
| `positive_source_counterexample`, `positive_source_is_stationary`, `positive_source_not_original_solution` | A stationary scalar-action background that fails ME-002 when the same positive source is identified without the required sign change. |

## Source and coupling checks

With J=lambda*I independent of phi, ME-013's scalar variation yields
`box(phi)-m2*phi+lambda*I=0`. In contrast, the existing ME-002 at c=1 and
alpha=0 is `box(phi)-4*pi*(energy+pressure)=0`. In the massless sector the
two residuals agree when `J=-4*pi*(energy+pressure)`. This is a proved
conditional identification, not a change to either historical equation.

For the counterexample take `phi(t,x,y,z)=-2*pi*t^2`, m2=0 and J=4*pi.
The field is stationary for the compact-variation scalar action. Its ME-002
residual at energy=1, pressure=0, c=1, alpha=0 is `-8*pi`, so it is not a
solution of that equation. The field need not have a finite absolute action;
its local action changes have the integrability proved above.

If I depends on phi, the coupling derivative is instead
`lambda*(I(phi)+phi*I'(phi))`. At lambda=1 and I(phi)=phi, the actual
derivative at phi=1 is 2, while retaining I alone would give 1. Jointly varied
fields and derivative-dependent information functionals need further terms
and are not represented by the prescribed-source result.

## Evidence and remaining obligations

- **Demonstrated:** the 35 Lean statements, including the four-dimensional
  compact-variation equivalence, under the frozen definitions and hypotheses.
- **Supported but incomplete:** ME-009 and ME-013 now have a partial scalar
  action specialization. ME-010 gains a variational treatment for this sector.
- **Rejected in this convention:** automatic identification of the positive
  action source with ME-002's positive right-hand-side source, and omission of
  the product derivative when the source depends on the varied field.
- **Unresolved:** the complete action, general covariance, metric variation,
  the remaining coupled fields, quantization, physical interpretation and the
  source obligations stated above. ME-014 and ME-039 remain catalogue-only.

No field equation is used as an assumption to prove its equivalence with
stationarity. No experimental data, fitted coefficients or claims of
independent replication enter these mathematical proofs. The results use
standard calculus of variations and are not claimed as new physical laws.

Primary mathematical dependencies are the pinned Mathlib
[integration-by-parts theorem](https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Analysis/Calculus/LineDeriv/IntegrationByParts.lean)
and [fundamental lemma for smooth test functions](https://github.com/leanprover-community/mathlib4/blob/8f9d9cff6bd728b17a24e163c9402775d9e6a365/Mathlib/Analysis/Distribution/AEEqOfIntegralContDiff.lean).
The module is a default build target, is included in the declaration audit,
and is checked by the existing GitHub Actions analysis job. Only the ordinary
Lean axioms `propext`, `Classical.choice` and `Quot.sound` are permitted.
