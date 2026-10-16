# Linearized curvature and source balance

This round gives ME-014 and ME-039 an explicit, partial differential model.
Keep the canonical equations and previous assumptions unchanged. Use Cartesian
real four-space, c=1, and the same (+---) flat metric as the scalar-action
round. A symmetric real tensor field h represents a metric perturbation.
All partial derivatives are actual Frechet derivatives.

## Target fixed before implementation

Define the standard linearized Ricci and Einstein differential operators from
h and its actual second derivatives. The linearized operator is an explicit
authored specialization; a derivative of the full nonlinear Einstein tensor
with respect to a variable metric is not assumed to have been proved.

Acceptance targets:

1. Derive symmetry, the four-dimensional trace-reversal identities, and the
   linearized contracted Bianchi identity from C3 regularity and Schwarz
   commutation, rather than assuming zero divergence.
2. Relate the operator to its standard wave form in Lorenz gauge.
3. Prove that a solution with nonzero constant coupling requires a conserved
   total source. Preserve explicit counterexamples for a nonconserved source
   and for omitting the derivative of a spatially varying coupling.
4. Apply this necessity theorem to ME-014's sum of expectation, scalar and
   recursive stress, and to ME-039's thought and recursive stress. Treat the
   expectation as an externally supplied classical tensor; do not claim a
   construction of quantum observables, a state, or renormalization.
5. Where tractable, connect ME-015/040's scalar stress divergence to the
   previously proved scalar equation and derive the required exchange balance
   with other source terms.

ME-039's use of the same operator is an authored candidate geometry, not an
identification of cognition with spacetime curvature. Neither source
conservation nor a successful Lean build establishes existence, uniqueness,
stability, general covariance, a nonlinear Einstein equation, quantization,
or an empirical interpretation. These remain open obligations.

## Definitions and proved scope

[LinearizedGravity.lean](LinearizedGravity.lean) contains 60 explicit theorem
declarations, including derivative and regularity lemmas. It reuses the
previous scalar action's coordinate partials and signature. Set
`eta = diag(1,-1,-1,-1)`, `tr(h) = eta^{ij} h_ij`,
`div(h)_j = partial^i h_ij`, and `box = partial^i partial_i`. The operators are:

$$
R^{(1)}_{ij}(h)=\tfrac12\bigl(
\partial_i\operatorname{div}(h)_j+
\partial_j\operatorname{div}(h)_i-
\Box h_{ij}-\partial_i\partial_j\operatorname{tr}(h)\bigr),
\qquad
G^{(1)}_{ij}(h)=R^{(1)}_{ij}(h)-\tfrac12\eta_{ij}\operatorname{tr}(R^{(1)}(h)).
$$

These formulas define the linearized operators in this package. They do not
assert a construction of a variable metric, its connection, or its nonlinear
curvature. The name `ricci` refers to this linearized operator throughout.
Schwarz commutation is proved from the actual C2 Fréchet Hessian. C3 regularity
then yields the differential identity `div(einstein(h)) = 0`.

Trace reversal is `bar(h) = h - eta*tr(h)/2`; in four dimensions its trace is
`-tr(h)` and applying it twice returns `h`. Under the explicitly assumed
Lorenz/de Donder condition `div(bar(h))=0`, the equation
`einstein(h)=coupling*T` is equivalent to
`box(bar(h))=-2*coupling*T`. This proves a reduction under a gauge condition,
not the existence of a transformation that reaches that condition.

`Solves coupling T h` requires a C3 symmetric perturbation and the pointwise
linearized equation. For C1 source components and nonzero constant coupling,
it implies `div(T)=0`. For ME-014 the coupling is `8*pi*G` and the source is
the sum of expectation, scalar and recursive tensors; for ME-039 it is `chi`
times thought plus recursive tensors. Conservation of the total is necessary;
it does not assert that each contribution is separately conserved or that a
solution exists for every conserved source.

## Scalar stress and exchange

ME-015 and ME-040's existing algebraic stress construction is now connected
to actual derivatives of a real C2 scalar. Take `V(phi)=m2*phi^2/2`, where
`m2` is an arbitrary real coefficient, and retain the catalogue signs:

$$
S_{ij}=\partial_i\phi\,\partial_j\phi
-\eta_{ij}\left(\tfrac12\partial_k\phi\,\partial^k\phi
+\tfrac{m2}{2}\phi^2\right),
\qquad
\partial^i S_{ij}=(\Box\phi-m2\,\phi)\partial_j\phi.
$$

The exact bridge to `TensorModels.scalarStress` is proved. If the previously
specified scalar action is stationary with continuous prescribed source J,
its already proved equation is `box(phi)-m2*phi+J=0`. Hence
`div(S)_j=-J*partial_j(phi)`. A solution of ME-014's specialized equation
requires `div(expectation)_j+div(recursive)_j=J*partial_j(phi)`.
ME-039 with ME-040's real scalar specialization requires
`div(recursive)_j=J*partial_j(phi)`. These statements link two formal models;
they do not derive stress by metric variation or identify a scalar with thought.

## Acceptance theorem register

All names below are in `MonolithicAnalysis.LinearizedGravity`.

| Theorems | Mathematical content |
|---|---|
| `second_partial_eq`, `mixed_partials`, `partial_wave` | Actual Hessian representation, C2 Schwarz symmetry and C3 commutation with the wave operator. |
| `ricci_symmetric`, `einstein_symmetric` | Symmetry of the differential tensors for a C2 symmetric perturbation. |
| `trace_reverse_trace`, `trace_reverse_involution` | Four-dimensional trace reversal identities. |
| `scalar_curvature_formula`, `divergence_ricci`, `contracted_bianchi` | Trace formula, contracted Ricci identity and zero divergence of the Einstein operator. |
| `lorenz_gauge_iff`, `einstein_in_lorenz_gauge`, `lorenz_field_equation_iff` | Equivalent gauge condition and trace-reversed wave form. |
| `source_conservation`, `semiclassical_balance`, `cognitive_balance` | Necessary source conservation for nonzero constant couplings. |
| `divergence_variable_mul` | Product rule with the explicit gradient of a varying coupling. |
| `time_source_divergence`, `nonconserved_source_no_solution` | The smooth symmetric source with only `T_00(x)=x_0` has divergence component 1 and admits no C3 solution at nonzero coupling. |
| `varying_coupling_counterexample` | The constant tensor with only `T_00=1` has zero time-divergence component; multiplying by `a(x)=x_0` makes that component 1. |
| `spatial_coupling_counterexample` | A constant metric tensor has zero divergence; multiplying by the spatial coordinate `a(x)=x_1` gives divergence component 1. |
| `scalar_stress_eq_catalogue`, `scalar_stress_divergence` | Exact catalogue bridge and off-shell scalar stress divergence. |
| `stationary_scalar_exchange` | Scalar action stationarity supplies the source exchange law. |
| `semiclassical_scalar_exchange`, `cognitive_scalar_exchange` | Other source sectors must balance that exchange in the coupled equation. |

## Coverage, verification and remaining work

ME-014 and ME-039 move from catalogue-only to **partial specialization**.
ME-015 and ME-040 remain partial, with stronger differential results. The
analytic overlay now has 21 explicit models and 28 partial results across all
49 of its entries; the root package retains its separate 53 structural or
discrete encodings. Zero catalogue-only entries does not mean that all 102
historical source obligations are complete.

The new module is a Lake build target and is included in the declaration-wide
axiom audit. The [verification workflow](../.github/workflows/lean.yml) builds
both Lean packages, checks canonical correspondence and all eight analytic
module registrations, and tests the rejection of public/private axioms,
`sorry` and native proof oracles. Dependency pins and canonical formulas are
unchanged. Reproduce with the commands in [COVERAGE.md](COVERAGE.md#verification).

The standard reference for the operator identities and gauge reduction is
David Tong's [General Relativity, section 5.1](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S5.html).
Tong uses the opposite metric signature; this package retains the catalogue's
explicit (+---) convention in every contraction. These are standard
mathematical results, without a novelty claim.

Remaining obligations include deriving these operators by linearizing full
nonlinear geometry, curved covariance, full coupled action and metric
variation, quantum observables/states and renormalization, gauge-fixing
existence, boundary data, general solution existence/uniqueness and stability,
nonquadratic scalar potentials, physical units and empirical identification.
The expectation and cognitive labels alone discharge none of these obligations.
