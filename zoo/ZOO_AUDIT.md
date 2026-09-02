# Monolithic 102 — ZOO Audit v1.0

## Determination

The 102-item corpus survives as a **versioned research program**, not as 102 proved laws. The ZOO separates standard reductions, typed constructs, empirical claims, and open specifications. No item is promoted merely because it compiles.

## Coverage and disposition

- Canonical items audited: **102/102**
- Conditional standard survivors: **15**
- Structural/definitional survivors: **28**
- Empirical tests required: **12**
- Open specifications: **47**
- Typed in the compile-checked core: **53**
- Preserved in the canonical Lean catalog: **49**

## ZOO protocol

SALMON/TORTOISE freeze provenance; RAVEN identifies prior mathematics; WEAVER/SPIDER map structure and dependencies; WEASEL/CHAMELEON attack assumptions and representation dependence; DRAGON tests stability/attractors; OWL/CROCODILE test warning and causal claims; HEDGEHOG tests generalization; CAT checks consistency; PHOENIX/AXOLOTL test recovery; HUMMINGBIRD defines live monitoring; TURTLE retains only claims that survive at their proper evidence level.

## Per-equation register

| ID | Cluster | Result | Lean | Dependencies | Primary failure condition |
|---|---|---|---|---|---|
| ME-001 | Framework signature | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-002 | Field/action | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-003 | Field/action | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially regularity/boundary conditions. |
| ME-004 | Field/action | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-005 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-002, ME-004 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-006 | Field/action | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-007 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-006 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-008 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-006, ME-007 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-009 | Field/action | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-010 | Field/action | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-011 | Field/action | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-012 | Field/action | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-013 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-003, ME-010 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-014 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-013, ME-015 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-015 | Field/action | OPEN_SPECIFICATION | canonical_catalog | ME-010 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-016 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially symbol/domain freeze. |
| ME-017 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-016 | Fails as written if the claimed reduction breaks under frozen conventions, especially symbol/domain freeze. |
| ME-018 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-016 | Fails as written if the claimed reduction breaks under frozen conventions, especially regularity/boundary conditions. |
| ME-019 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-018 | Fails as written if the claimed reduction breaks under frozen conventions, especially regularity/boundary conditions. |
| ME-020 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-016, ME-021 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-021 | Quantum/Madelung | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-016 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-022 | Recursive control | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-023 | Recursive control | OPEN_SPECIFICATION | typed_core | ME-022 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-024 | Recursive control | OPEN_SPECIFICATION | canonical_catalog | ME-022, ME-023, ME-025, ME-026 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-025 | Recursive control | STRUCTURAL_SURVIVOR | typed_core | — | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-026 | Recursive control | OPEN_SPECIFICATION | canonical_catalog | ME-022, ME-023 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-027 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-022, ME-023, ME-026 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-028 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-024, ME-027 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-029 | Recursive control | STRUCTURAL_SURVIVOR | typed_core | ME-028 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-030 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-029 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-031 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-022, ME-023, ME-024 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-032 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-031 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-033 | Recursive control | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-032 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-034 | Recursive control | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | — | Fails as written if the claimed reduction breaks under frozen conventions, especially external validation and baseline dependence. |
| ME-035 | Recursive control | EMPIRICAL_TEST_REQUIRED | typed_core | ME-031 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-036 | Coupled nonlinear PDE | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-037 | Coupled nonlinear PDE | OPEN_SPECIFICATION | canonical_catalog | ME-036 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-038 | Coupled nonlinear PDE | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-039 | Coupled nonlinear PDE | OPEN_SPECIFICATION | canonical_catalog | ME-040 | Cannot advance until a complete specification resolves interpretive leap beyond mathematics; inconsistent specifications reject it. |
| ME-040 | Coupled nonlinear PDE | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-041 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | — | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-042 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | ME-041 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under special-number privilege/invariance. |
| ME-043 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | ME-041, ME-042 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under special-number privilege/invariance. |
| ME-044 | Phi/coherence | OPEN_SPECIFICATION | typed_core | ME-041 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-045 | Phi/coherence | CONDITIONAL_STANDARD_SURVIVOR | typed_core | ME-042, ME-043 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-046 | Phi/coherence | OPEN_SPECIFICATION | canonical_catalog | ME-041 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-047 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | ME-022, ME-023 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-048 | Phi/coherence | EMPIRICAL_TEST_REQUIRED | typed_core | ME-047 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-049 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | ME-047 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-050 | Phi/coherence | STRUCTURAL_SURVIVOR | typed_core | ME-049 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-051 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves regularity/boundary conditions; inconsistent specifications reject it. |
| ME-052 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | ME-027 | Cannot advance until a complete specification resolves regularity/boundary conditions; inconsistent specifications reject it. |
| ME-053 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-054 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | ME-053 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-055 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves regularity/boundary conditions; inconsistent specifications reject it. |
| ME-056 | Emergence/cosmology | OPEN_SPECIFICATION | canonical_catalog | ME-055 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-057 | Emergence/cosmology | EMPIRICAL_TEST_REQUIRED | canonical_catalog | ME-056 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-058 | Emergence/cosmology | STRUCTURAL_SURVIVOR | typed_core | ME-057 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-059 | Collapse/recursion/time | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves existence/uniqueness of optimizer; inconsistent specifications reject it. |
| ME-060 | Collapse/recursion/time | OPEN_SPECIFICATION | canonical_catalog | ME-059 | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-061 | Collapse/recursion/time | EMPIRICAL_TEST_REQUIRED | canonical_catalog | ME-060 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-062 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-063 | Collapse/recursion/time | STRUCTURAL_SURVIVOR | typed_core | ME-062 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-064 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | ME-047 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-065 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | ME-064 | Cannot advance until a complete specification resolves interpretive leap beyond mathematics; inconsistent specifications reject it. |
| ME-066 | Collapse/recursion/time | OPEN_SPECIFICATION | canonical_catalog | ME-065 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-067 | Collapse/recursion/time | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-068 | Collapse/recursion/time | OPEN_SPECIFICATION | canonical_catalog | ME-067 | Cannot advance until a complete specification resolves interpretive leap beyond mathematics; inconsistent specifications reject it. |
| ME-069 | Collapse/recursion/time | EMPIRICAL_TEST_REQUIRED | typed_core | ME-070 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-070 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-071 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | — | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-072 | Collapse/recursion/time | EMPIRICAL_TEST_REQUIRED | typed_core | ME-071, ME-047 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-073 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | ME-064 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-074 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | ME-073 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-075 | Collapse/recursion/time | STRUCTURAL_SURVIVOR | typed_core | ME-064 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-076 | Collapse/recursion/time | OPEN_SPECIFICATION | typed_core | ME-075 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-077 | Fluid/symbolic bases | OPEN_SPECIFICATION | canonical_catalog | — | Cannot advance until a complete specification resolves nonzero-denominator/domain conditions; inconsistent specifications reject it. |
| ME-078 | Fluid/symbolic bases | STRUCTURAL_SURVIVOR | typed_core | ME-077, ME-082 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-079 | Fluid/symbolic bases | STRUCTURAL_SURVIVOR | typed_core | ME-077 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-080 | Fluid/symbolic bases | CONDITIONAL_STANDARD_SURVIVOR | canonical_catalog | ME-077 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-081 | Fluid/symbolic bases | OPEN_SPECIFICATION | canonical_catalog | ME-077, ME-078 | Cannot advance until a complete specification resolves symbol/domain freeze; inconsistent specifications reject it. |
| ME-082 | Fluid/symbolic bases | STRUCTURAL_SURVIVOR | typed_core | ME-078 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-083 | Fluid/symbolic bases | STRUCTURAL_SURVIVOR | typed_core | — | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under special-number privilege/invariance. |
| ME-084 | Fluid/symbolic bases | OPEN_SPECIFICATION | canonical_catalog | ME-083, ME-041 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-085 | Fluid/symbolic bases | STRUCTURAL_SURVIVOR | typed_core | ME-041, ME-042 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under special-number privilege/invariance. |
| ME-086 | Fluid/symbolic bases | OPEN_SPECIFICATION | typed_core | ME-085 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-087 | Fluid/symbolic bases | OPEN_SPECIFICATION | canonical_catalog | ME-086 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-088 | Fluid/symbolic bases | OPEN_SPECIFICATION | typed_core | ME-085, ME-086 | Cannot advance until a complete specification resolves special-number privilege/invariance; inconsistent specifications reject it. |
| ME-089 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-047 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-090 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-047, ME-094 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under interpretive leap beyond mathematics. |
| ME-091 | Evaluation/epistemic | CONDITIONAL_STANDARD_SURVIVOR | typed_core | ME-045 | Fails as written if the claimed reduction breaks under frozen conventions, especially nonzero-denominator/domain conditions. |
| ME-092 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | canonical_catalog | — | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under nonzero-denominator/domain conditions. |
| ME-093 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | canonical_catalog | — | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-094 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-047 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-095 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-094 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under external validation and baseline dependence. |
| ME-096 | Evaluation/epistemic | EMPIRICAL_TEST_REQUIRED | typed_core | ME-072, ME-095 | Fails if preregistered held-out tests do not beat the declared baseline at matched error/compute budgets. |
| ME-097 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-098 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under existence/uniqueness of optimizer. |
| ME-098 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-047, ME-097 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under interpretive leap beyond mathematics. |
| ME-099 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-024, ME-026, ME-047 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under interpretive leap beyond mathematics. |
| ME-100 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-099 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under interpretive leap beyond mathematics. |
| ME-101 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-047, ME-072 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under interpretive leap beyond mathematics. |
| ME-102 | Evaluation/epistemic | STRUCTURAL_SURVIVOR | typed_core | ME-028, ME-029, ME-030 | Fails as a useful construct if it is undefined, non-invariant, or non-identifying under limit existence and topology. |

## Hard boundary

A successful `lake build` establishes parser/type/proof-kernel acceptance for the encoded objects only. It does not establish dimensional correctness, covariance, existence of physical solutions, empirical superiority, consciousness, legal validity, or a unified theory of nature.
