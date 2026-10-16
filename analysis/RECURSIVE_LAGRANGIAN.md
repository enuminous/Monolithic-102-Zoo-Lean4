# Varying the recursive Lagrangian: ME-011

[RecursiveLagrangian.lean](RecursiveLagrangian.lean) contains **30 explicit
theorem statements** for a specified state-space interpretation of ME-011.
It derives actual gradients, a simultaneous first variation, the
Euler–Lagrange residual and conditional energy laws. The historical equation
and its original obligations are retained in [coverage.json](coverage.json).

## Frozen domain and independent variables

Use a real Hilbert state space with position q and velocity v as independent
arguments. At each time, memory m, memory velocity w and environment e are
external inputs to the position variation. R denotes the slice
$q\mapsto R(q,m,e)$. Both $\phi$ and R may depend on q; neither is silently
treated as spatially constant. Along a path, $v=\dot q$ and $w=\dot m$ are
actual Mathlib derivatives.

The source expression is preserved:

$$L_{\rm rec}=\lambda\phi(q)R(q)
-\frac{\kappa}{2}\lVert q-m\rVert^2
-\frac{\eta}{2}\lVert v-w\rVert^2.$$

For comparison with ordinary mechanics, define the explicit extension

$$L=\frac M2\lVert v\rVert^2+L_{\rm rec}.$$

This added kinetic term is an authored modeling choice. **M=0 recovers the
source recursive term.** Parameters M, lambda, kappa and eta are real time
constants. Phi, R and prescribed memory may vary with time in the general
Euler–Lagrange calculation. Varying memory or environment jointly with q,
or making them functions of q during this variation, requires additional
chain-rule terms and is outside this specification.

## Actual variation and equations of motion

The proved derivatives are

$$\partial_qL=
\lambda\bigl(R\nabla\phi+\phi\nabla R\bigr)-\kappa(q-m),$$

$$p=\partial_vL=Mv-\eta(v-w)=(M-\eta)v+\eta w.$$

`first_variation` differentiates the actual map
$\varepsilon\mapsto L(q+\varepsilon\,\delta q,v+\varepsilon\,\delta v)$
at zero, obtaining

$$\delta L=\langle\partial_qL,\delta q\rangle
+\langle\partial_vL,\delta v\rangle.$$

The Euler–Lagrange residual is defined through those actual derivatives,
$\mathcal E(L)=\frac{d}{dt}\partial_vL-\partial_qL$. Its proved expansion is

$$\mathcal E(L)=(M-\eta)\ddot q+\eta\ddot m
-\lambda\bigl(R\nabla\phi+\phi\nabla R\bigr)+\kappa(q-m).$$

Consequently, a zero residual is equivalent to

$$ (M-\eta)\ddot q=
\lambda\bigl(R\nabla\phi+\phi\nabla R\bigr)-\kappa(q-m)-\eta\ddot m.$$

`acceleration_eq` divides by $M-\eta$ only under an explicit nonzero
hypothesis. The model's `Solves` predicate includes twice differentiable
state and memory paths and differentiable phi/R slices along the state path;
the totalized derivative at a nondifferentiable point cannot by itself qualify
a path as a classical solution. These hypotheses do not assert that a
solution exists for arbitrary data.

The module also proves an exact link to the existing
[ME-052 discrepancy definition](SpecifiedModels.lean): with its recursion
function chosen as $\phi R$ and its reward coefficient chosen as $2\lambda$,
$L_{\rm rec}=-D/2$. This parameter-matched identity does not identify the
Euler–Lagrange equation with an unrestricted negative position-gradient flow.

## Canonical energy and a separate damping model

For **static memory** and **time-independent phi and R**, the canonical
energy $\langle v,p\rangle-L$ is

$$H=\frac{M-\eta}{2}\lVert v\rVert^2
+\frac{\kappa}{2}\lVert q-m\rVert^2-\lambda\phi(q)R(q).$$

The actual time derivative satisfies

$$\frac{dH}{dt}=\langle\dot q,\mathcal E(L)\rangle.$$

Therefore H is constant along every classical solution of the autonomous,
static-memory Euler–Lagrange equation. The proof establishes the derivative
identity before using the equation of motion. It neither assumes conservation
in a derivative rule nor extends it to moving memory or time-dependent fields.

When lambda is zero, H is nonnegative for $M\geq\eta$ and $\kappa\geq0$.
For $M>\eta$ and $\kappa>0$, H is zero exactly when $v=0$ and $q=m$.
No analogous positivity is asserted for an arbitrary coupling potential.

A separate Rayleigh function is defined as

$$\mathcal R(v)=\frac\gamma2\lVert v-w\rVert^2,
\qquad -\partial_v\mathcal R=-\gamma(v-w).$$

For static memory, adding this force means imposing
$\mathcal E(L)+\gamma\dot q=0$. The derived energy law becomes

$$\frac{dH}{dt}=-\gamma\lVert\dot q\rVert^2.$$

For nonnegative gamma, H is nonincreasing along such a path. This Rayleigh
term is **additional dynamics**, not a consequence of the source's negative
velocity-gap term. Decrease of a possibly indefinite H is not a general
stability or global-existence theorem.

## Counterexamples retained in the proof catalogue

| Shortcut being tested | Checked example and result | Lean theorem |
|---|---|---|
| Keep only `phi * grad(R)` when varying the coupling. | On the real line, phi(q)=q and R=1 give position gradient 1 at q=0 when lambda=1 and kappa=eta=0. | `varying_coherence_counterexample` |
| Treat the source's velocity-gap term as friction. | With M=lambda=kappa=0, eta=1 and static memory, q(t)=t has zero Euler–Lagrange residual. A separately added unit Rayleigh force at the same velocity is −1. | `velocity_gap_is_not_drag` |
| Assume the recursive velocity term supplies positive kinetic energy. | M=0, eta=1, zero coupling/stiffness, q=m=0 and v=1 give canonical energy −1/2. | `negative_kinetic_energy_counterexample` |
| Drop memory acceleration from the equation. | q=0, m(t)=t², M=lambda=kappa=0 and eta=1 give Euler–Lagrange residual 2. | `accelerating_memory_counterexample` |
| Infer energy conservation for time-dependent fields. | With M=lambda=1, kappa=eta=0, phi(t,q)=t, R=1 and q=m=0, the residual is zero but the canonical energy derivative is −1. | `time_dependent_energy_counterexample` |
| Divide by M−eta or assume uniqueness at degeneracy. | At M=eta, zero coupling/stiffness and zero memory, every regular path solves the equation. Paths 0 and t² share position and velocity at time zero but differ at time one. | `degenerate_residual`, `degenerate_classical_solution`, `degenerate_nonuniqueness` |

## Theorem map

| Mathematical result | Lean declarations |
|---|---|
| Recursive term and the earlier discrepancy | `recursive_discrepancy` |
| Actual gradients and first variation | `recursive_position_gradient`, `recursive_velocity_gradient`, `position_gradient`, `velocity_gradient`, `first_variation` |
| Momentum and Euler–Lagrange equations | `momentum_eq`, `momentum_hasDerivAt`, `euler_lagrange_eq`, `euler_lagrange_iff`, `acceleration_eq`, `static_residual_eq` |
| Canonical energy, its actual derivative and conservation | `energy_eq_canonical`, `energy_hasDerivAt`, `energy_derivative`, `energy_conserved` |
| Uncoupled energy positivity and its zero set | `uncoupled_energy_nonnegative`, `uncoupled_energy_zero_iff` |
| Separate Rayleigh dynamics and monotonicity | `rayleigh_gradient`, `rayleigh_force`, `damped_energy_derivative`, `damped_energy_antitone` |

## Coverage and evidence boundary

**Demonstrated:** the exact Hilbert-space derivative identities, conditional
energy laws, positivity statements and explicit counterexamples above.
These are standard Euler–Lagrange and Rayleigh results applied to the stated
model, without an EFMW-specific novelty claim. No animal operation, empirical
fit or simulation substitutes for the Lean proofs.

**Partial:** ME-011 now has a state-space variational specialization. It does
not prove that stationary points of an integrated action are exactly these
solutions under boundary conditions. Joint memory/environment dynamics,
relativistic covariance, physical units, gravitational or continuum field
equations, general existence or uniqueness, and observational identification
remain open. The [EFMW-Lagrangian continuum
bridge](https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/CONTINUUM_BRIDGE.md)
uses a different frozen action; its results are not duplicated or silently
identified with this state-space construction.

The [verification workflow](../.github/workflows/lean.yml) builds this module
alongside the other analytic modules. The [coverage checker](scripts/check_coverage.py)
locks the original formulas and build/audit roster; the
[declaration audit](Audit.lean) permits only the standard `propext`,
`Classical.choice` and `Quot.sound` axioms. All four rejection controls must
pass, and acceptance requires successful verification of the exact commit.
