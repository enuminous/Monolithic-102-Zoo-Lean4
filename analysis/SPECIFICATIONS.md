# Explicit completions and limits

These conventions are authored mathematical specifications, adopted in response
to the request to resolve the missing definitions. They are not recovered facts
about an intended physical theory. The canonical 102 equations remain unchanged.
The acceptance tests are the exact Lean statements and the strict axiom audit.

- **ME-066:** choose finite complex coordinate spaces H and A. Embed H, A and
  their Kronecker tensor coordinates in disjoint blocks of H ⊕ A ⊕ (H ⊗ A).
  Normalize by the positive square root of the sum of squared complex moduli.
  Exclude the all-zero state when asserting unit norm. This resolves the
  previously ill-typed sum without identifying distinct state spaces.
- **ME-087:** choose the real coordinate algebra R^n with coordinatewise
  multiplication and its standard basis. Designated null pairs are exactly
  distinct basis indices. The basis consists of nonzero idempotents and sums
  to the multiplicative identity. This is a specific algebra with zero divisors;
  it is not an assertion about octonions or another division algebra.
- **Tensor entries:** use real four-index coordinate arrays. The inverse metric,
  metric, field gradient and additional tensors are explicit inputs. Symmetry,
  residual expansion and decoupling are algebraic results; calling an input G
  does not prove that it is Einstein curvature. R in ME-006 is an additional
  tensor and is not automatically Ricci curvature. No action variation or
  covariant conservation law is inferred from these identities.
- **ME-051–053:** use actual Frechet derivatives on a real Hilbert space.
  Positions and velocities in ME-052 are independent coordinates. Differentiating
  position holds velocity and the memory state fixed. Nonzero mass is the
  application domain of ME-053; Lean's total division is not a physical
  definition at zero mass.
- **ME-056:** use real density/coupling parameters and a nonzero scale factor.
  A real Hubble rate exists exactly when the specified right hand side is
  nonnegative. Neither a branch sign for H nor a cosmological evolution is
  supplied by an equation for H squared alone.

All new results are standard mathematical consequences of these conventions.
They do not establish empirical validity, novelty, consciousness, physical
forces or a universal theory. The coverage ledger retains the original
obligations and distinguishes models from partial coordinate specializations.

- **ME-009/010/013 scalar action:** the frozen target and exact proved scope
  are in [SCALAR_ACTION.md](SCALAR_ACTION.md). Use actual four-dimensional
  Cartesian derivatives, (+---), c=1, quadratic potential, a prescribed source
  independent of the varied scalar, and smooth compactly supported variations.
  Derive stationarity iff the classical scalar equation; keep the full metric
  and other-field variations open. Preserve the source-sign mismatch with
  ME-002 and the counterexample for a field-dependent source.

- **ME-084:** use a product of real unit circles, center (8,8,8), minor
  radius 8 and major radius 8*phi. Require phi>1 and prove injectivity. Other
  choices could also satisfy the historical descriptor; this one is explicit.
- **ME-012:** choose Cartesian c=1, (+---), six independent real components
  and their antisymmetric field tensor. Raising both indices yields the proved
  electric-minus-magnetic expression. This is standard electromagnetism.
- **ME-024:** freeze gap magnitudes and forcing in the deterministic sector;
  require positive relaxation time. The theorem derives potential dissipation
  from the actual trajectory derivative, without assuming energy decrease.
- **ME-036/037:** retain the homogeneous uncoupled cubic exactly. It grows
  above one, so a decay interpretation cannot be inferred from its appearance.
- **ME-054:** test the displayed plus-sign projector under the already frozen
  (+---) metric. The rest-frame counterexample rules out orthogonality in that
  convention. A different signature or sign is a different specification.

## Phase, current and Madelung targets (ME-018–021)

Fix real amplitude and phase fields on one time and one spatial coordinate,
with the explicitly stated first and second ordinary partial derivatives.
Use the existing complex wave `rho * exp(i*theta)`; derivatives in the new
theorems must be actual Mathlib derivatives, not independent formal symbols.

- **ME-018:** identify each lower-index phase-current component
  `rho^2 * partial(theta)` with `Im(conj(psi) * partial(psi))`. In the flat
  (+−), c=1 convention, raising the spatial index changes its sign.
- **ME-019:** derive `partial_t(rho^2*theta_t) -
  partial_x(rho^2*theta_x) = 0` from the real-potential Klein–Gordon equation
  `psi_tt - psi_xx + U*psi = 0`. This is a flat 1+1 specialization, with U
  real. It does not assert arbitrary curved-space covariance.
- **ME-020/021:** independently fix the Schrödinger equation
  `i*hbar*psi_t + hbar^2/(2*m)*psi_xx - V*psi = 0`, with V real and
  nonzero real hbar and mass. Set `S = hbar*theta`. At a nonzero amplitude,
  prove equivalence to the Hamilton–Jacobi equation with
  `Q = -(hbar^2/(2*m)) * rho_xx/rho` and the probability continuity equation
  `partial_t(rho^2) + (hbar/m)*partial_x(rho^2*theta_x) = 0`.

The relativistic current's temporal component is `rho^2*theta_t`; the
Schrödinger probability density is `rho^2`. These are different objects.
The targets do not identify them or infer either evolution from the polar
identity alone. Zeros of the amplitude, global phase reconstruction, general
manifolds, PDE existence, boundary conditions and empirical interpretations
remain outside this specification. These are standard mathematical relations,
with no EFMW-specific novelty claim.

## Three-dimensional curl target (ME-055)

Fix real Cartesian three-space `Fin 3 -> Real` with the standard coordinate
basis and orientation (x,y,z). Define every partial derivative through the
actual Frechet derivative applied to the corresponding basis vector. Define
the gradient, divergence, cross product and curl by their usual Cartesian
components; the velocity field in ME-055 is an explicit input.

The acceptance targets are curl of a C² scalar gradient equals zero, divergence
of the curl of a C² vector field equals zero, linearity under the stated
differentiability assumptions, and the product rule for scalar multiplication
`curl(a*v) = grad(a) cross v + a*curl(v)`. Derive zero curl for the existing
ME-051/053 force forms when their coefficients are spatial constants and their
potentials are C². Check nonzero vorticity for rigid rotation and for a
spatially varying coefficient multiplying a gradient. These are actual
derivative statements, with Schwarz symmetry derived from C² regularity.

This is a Cartesian mathematical realization, not a theory of universal
rotation. No velocity field is identified with an observed universe, no curved
geometry or physical units are supplied, and zero local curl is not asserted
to imply a global potential on an arbitrary domain. The original ME-055 source
obligations remain visible in the coverage ledger.

## Cartesian fluid targets (ME-077, ME-080)

Reuse ME-055's actual Cartesian Fréchet partials on real three-space. Time
derivatives are ordinary Mathlib derivatives. Density, viscosity and pressure
are real fields; velocity has three real components. Keep the historical
equations and their signs unchanged.

- **ME-077:** author a nonrelativistic specialization with unhalved trace-free
  shear `sigma_ij = partial_j(u_i) + partial_i(u_j) - (2/3)*delta_ij*div(u)`
  and no bulk viscosity. Derive the divergence of this tensor using C² mixed
  partials, then the product rule for `div(eta*sigma)`. The source's `eta(t)`
  is spatially constant at each time. A spatially varying viscosity is an
  explicit extension requiring its derivative correction. Check nonnegative
  pointwise viscous work for nonnegative viscosity, the incompressible limit,
  and a strictly positive varying-viscosity counterexample to an unjustified
  Laplacian replacement. Define the momentum residual with actual material
  acceleration and derive conservative momentum transport using continuity.
- **ME-080:** derive equivalence of conservative and material continuity,
  including incompressible and nonzero constant-density special cases. Define
  a classical solution predicate that includes differentiability. Check the
  explicit three-dimensional expanding flow `u=a*x`, `rho=r*exp(-3*a*t)`,
  and the counterexample of constant density in a flow with nonzero divergence.

The [fluid proof catalogue](FLUIDS.md) records exact statements and exclusions.
No relativistic geometry or proper-time identification is implied by the
Cartesian acceleration. Full pressure closure, general nonlinear existence or
uniqueness, weak solutions, boundaries and integrated conservation or energy
laws remain open. A pointwise constitutive inequality is not a stability
theorem. These targets are standard mathematics; no empirical or novelty
claim is part of acceptance.

## Recursive Lagrangian target (ME-011)

Fix a real Hilbert state space. At each time, position q and velocity v are
independent arguments for variation; memory m, memory velocity w and the
environment are external inputs. The supplied function R is the slice
`q -> R(q,m,e)`. Both phi and R may depend on q, so the product-gradient term
must include both `R*grad(phi)` and `phi*grad(R)`. Along a trajectory, memory
velocity is the actual derivative of the prescribed memory path.

Retain ME-011's signs and coefficients:
`Lrec = lambda*phi(q)*R(q) - (kappa/2)*norm(q-m)^2 - (eta/2)*norm(v-w)^2`.
Define an explicitly authored mechanical extension by adding
`(M/2)*norm(v)^2`; setting M=0 recovers the original recursive term. Derive
position and velocity gradients and the Euler-Lagrange residual from actual
Mathlib derivatives. Never assume the desired equation of motion as a
derivative rule. Constants M, lambda, kappa and eta are time independent.

Acceptance targets: the exact momentum and Euler-Lagrange formula, inversion
only when `M-eta` is nonzero, canonical energy and its conservation for static
memory and time-independent fields, and counterexamples separating a negative
velocity-gap term from friction or positive kinetic energy. Any Rayleigh
dissipation function is a separate, explicitly added model. Its damping and
energy decrease must not be attributed to the source Lagrangian alone.

This is a partial state-space variational specialization. It does not vary
memory or environment as dynamical fields, identify memory with a function of
q during the position derivative, establish an action-stationarity equivalence
under boundary conditions, or supply relativistic covariance, physical units,
field equations for gravity or empirical validation. The continuum action
in EFMW-Lagrangian remains a separate frozen specification.
