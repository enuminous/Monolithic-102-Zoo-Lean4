# Cartesian fluid identities for ME-077 and ME-080

[Fluids.lean](Fluids.lean) extends the existing [Cartesian derivative
operators](Vorticity.lean) with actual Fréchet spatial derivatives and ordinary
time derivatives. It contains **38 explicit theorem statements**. The source
equations and their original obligations remain unchanged in
[coverage.json](coverage.json).

## Frozen specification

Space is `Fin 3 → ℝ`; density, pressure and viscosity are real functions, and
velocity is a three-component real field. Coordinates are Cartesian. The dot
product and all contractions below are explicit sums of component products;
no identification with Lean's default function-space norm is used.

For ME-077, this is an authored **nonrelativistic specialization**, not a
derivation from the source's relativistic equation. We choose the unhalved,
trace-free strain convention, without bulk viscosity:

$$\sigma_{ij}=\partial_j u_i+\partial_i u_j
-\frac23\delta_{ij}\,\nabla\cdot u,
\qquad F_i=\sum_j\partial_j(\eta\sigma_{ij}).$$

In this convention the material acceleration is
$D_tu=\partial_tu+(u\cdot\nabla)u$, and the momentum residual is

$$\rho D_tu+\nabla P-F-f_{\rm ext}.$$

The signs match the displayed force balance. Proper time, Lorentzian index
raising, relativistic projectors and a derivation of this Cartesian model as a
relativistic limit are not supplied. The choice of strain is explicit because
the source does not fix its normalization or constitutive law.

For ME-080, retain exactly the standard continuity equation:

$$\partial_t\rho+\nabla\cdot(\rho u)=0.$$

`SolvesContinuity` includes time differentiability of density and spatial
differentiability of density and velocity. A totalized derivative at a
nondifferentiable point therefore cannot by itself certify a classical solution.

## Verified identities

| Result | Lean theorem | Assumptions and scope |
|---|---|---|
| Shear is symmetric and has zero trace. | `shear_symmetric`, `shear_trace_zero` | Exact component algebra for the stated convention. |
| Divergence of the symmetric gradient is `laplacian(u) + grad(div(u))`. | `symmetric_gradient_divergence` | C² velocity; mixed-partial symmetry follows from Mathlib's Schwarz theorem. |
| Divergence of the trace-free shear is `laplacian(u) + grad(div(u))/3`. | `shear_divergence` | C² velocity in three dimensions. |
| Varying viscosity contributes an additional derivative term. | `viscous_force_product` | C² velocity and differentiable viscosity at the point. |
| Spatially constant viscosity factors out; the incompressible operator is `eta * laplacian(u)`. | `viscous_force_constant`, `incompressible_viscous_force` | The latter requires divergence zero as a field, not merely at one point. |
| The source's time-only viscosity gives the stated momentum-residual expansion. | `momentum_residual_constant_viscosity` | C² spatial velocity at the fixed time; this spatial identity needs no time derivative of viscosity. |
| Shear work is half the sum of squared shear components and is nonnegative for nonnegative viscosity. | `shear_work`, `viscous_work_nonnegative` | Pointwise constitutive algebra, not an integrated energy or stability theorem. |
| Conservative and material continuity forms are equivalent. | `continuity_material`, `continuity_iff_material` | Spatial differentiability; no division by density. |
| Incompressible continuity is material constancy of density. | `incompressible_continuity_iff` | Zero divergence at the point. |
| For nonzero constant density, continuity is equivalent to zero divergence. | `nonzero_constant_density_iff` | Excludes zero density for this converse. |
| Conservative momentum differs from density times acceleration by velocity times the continuity residual. | `momentum_transport`, `momentum_of_continuity` | Density and velocity differentiable in time and space at the point; the second result additionally imposes continuity. |
| An expanding flow admits an explicit classical density solution. | `expanding_solution`, `expanding_density_positive`, `expanding_density_initial` | Any real expansion rate; positive initial density for positivity. |

The viscosity identity is

$$F_i=\eta\left(\Delta u_i+\frac13\partial_i\nabla\cdot u\right)
+\sum_j(\partial_j\eta)\sigma_{ij}.$$

The source writes viscosity as $\eta(t)$, so it is spatially constant at each
fixed time and the last term vanishes. The varying-viscosity theorem is an
explicit extension; it does not suggest a missing term in that time-only case.

The two transport identities are

$$\partial_t\rho+\nabla\cdot(\rho u)
=D_t\rho+\rho\nabla\cdot u,$$

$$\partial_t(\rho u_i)+\nabla\cdot(\rho u_i u)
=\rho D_tu_i+u_i\bigl(\partial_t\rho+\nabla\cdot(\rho u)\bigr).$$

These product rules are proved before using the continuity equation. Mass
conservation is an explicit hypothesis of the subsequent momentum corollary,
not an assumed conclusion hidden inside the derivative calculation.

## Exact examples and failed shortcuts

For $u(t,x)=a x$, the divergence is $3a$ and the shear is zero. The density

$$\rho(t,x)=r\exp(-3at)$$

solves continuity classically, equals $r$ at time zero, and stays positive
when $r>0$. This demonstrates compressible mass transport, not a solution of
every fluid equation. Its spatially uniform density has infinite total mass
on all of real three-space when $r>0$; no finite-total-mass claim is made.
With the same expanding velocity at $a=1$, constant density one gives a
continuity residual of **3**, not zero
(`constant_density_expansion_counterexample`).

For linear shear $u=(y,0,0)$, both the divergence and component Laplacian
vanish. Choose viscosity $\eta=y^2+1$, which is strictly positive everywhere.
At $(0,1,0)$ the actual viscous force is **(2,0,0)**. Thus even for an
incompressible smooth velocity, replacing varying-viscosity force by
$\eta\Delta u$ fails (`varying_viscosity_counterexample`).

## Evidence boundary and reproduction

**Demonstrated:** the exact derivative identities, pointwise inequalities,
classical continuity solution and counterexamples above. These are standard
vector-calculus and Newtonian-fluid results, without an EFMW-specific novelty
claim. No Zoo animal operation, empirical fit or simulation is used as a
substitute for a proof.

**Supported but incomplete:** ME-077 has a partial Cartesian specialization.
Relativistic geometry, physical constitutive identification, units, pressure
closure, boundaries, integral energy balances and general nonlinear fluid
existence or uniqueness remain open. ME-080 has an explicit analytic model;
weak solutions, arbitrary-flow existence, boundary fluxes and integral mass
conservation remain separate obligations. This work does not identify the
mathematical fields with observed physical quantities.

The separate [Wright's Law transport
proofs](https://github.com/enuminous/Wrights-Law/blob/main/formal/PeriodicField.lean)
provide one-dimensional constant-velocity transport, uniqueness and periodic
mass conservation. This module reuses the catalogue's three-dimensional
operators and addresses variable velocity and viscous stress; it does not copy
those transport proofs or reclassify them as full fluid dynamics.

Run the [standard verification commands](COVERAGE.md#verification). The
[workflow](../.github/workflows/lean.yml) builds all five analytic modules,
checks the unchanged canonical formulas and module roster, audits every safe
project declaration and tests rejection of public axioms, private axioms,
placeholders and native proof oracles. Acceptance requires a successful build
and audit of the exact published commit.
