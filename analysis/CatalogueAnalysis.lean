import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Module

/-! Real/complex realizations of the frozen catalogue. Domains and exclusions
are explicit in COVERAGE.md. These are standard mathematical results, not
empirical evidence for the catalogue's physical interpretations. -/

noncomputable section
open scoped BigOperators
namespace MonolithicAnalysis

namespace FlatScalar
abbrev Spacetime := Fin 4 → ℝ
def partialD (i : Fin 4) (f : Spacetime → ℝ) (x : Spacetime) : ℝ :=
  fderiv ℝ f x (Pi.single i 1)
def second (i : Fin 4) (f : Spacetime → ℝ) := partialD i (partialD i f)
def laplacian (f : Spacetime → ℝ) (x : Spacetime) : ℝ :=
  ∑ i : Fin 3, second i.succ f x
/-- ME-004: flat (+---) convention, with a nonzero speed in the solution domain. -/
def box (c : ℝ) (f : Spacetime → ℝ) (x : Spacetime) : ℝ :=
  second 0 f x / c ^ 2 - laplacian f x
/-- ME-002 specialized to the explicitly stated flat ME-004 operator. -/
def original (c α : ℝ) (f energy pressure : Spacetime → ℝ) (x : Spacetime) : ℝ :=
  box c f x - α ^ 2 / c ^ 2 * second 0 f x -
    (4 * Real.pi / c ^ 2) * (energy x + pressure x * c)
/-- ME-005, preserving the catalogue's signs. -/
def expanded (c α : ℝ) (f energy pressure : Spacetime → ℝ) (x : Spacetime) : ℝ :=
  ((1 - α ^ 2) / c ^ 2) * second 0 f x - laplacian f x -
    (4 * Real.pi / c ^ 2) * (energy x + pressure x * c)
theorem residual_eq (c α : ℝ) (f energy pressure : Spacetime → ℝ) (x : Spacetime) :
    original c α f energy pressure x = expanded c α f energy pressure x := by
  unfold original expanded box
  ring
def OriginalSolution (c α : ℝ) (f energy pressure : Spacetime → ℝ) : Prop :=
  c ≠ 0 ∧ ContDiff ℝ 2 f ∧ ∀ x, original c α f energy pressure x = 0
def ExpandedSolution (c α : ℝ) (f energy pressure : Spacetime → ℝ) : Prop :=
  c ≠ 0 ∧ ContDiff ℝ 2 f ∧ ∀ x, expanded c α f energy pressure x = 0
theorem solution_iff (c α : ℝ) (f energy pressure : Spacetime → ℝ) :
    OriginalSolution c α f energy pressure ↔ ExpandedSolution c α f energy pressure := by
  simp only [OriginalSolution, ExpandedSolution, residual_eq]
end FlatScalar

namespace Polar
/-- ME-016: a complex amplitude with real modulus parameter and phase. -/
def wave (ρ θ : ℝ) : ℂ := (ρ : ℂ) * Complex.exp (Complex.I * (θ : ℂ))
/-- ME-017 holds even when the real amplitude parameter is negative. -/
theorem norm_sq (ρ θ : ℝ) : ‖wave ρ θ‖ ^ 2 = ρ ^ 2 := by
  simp [wave, Complex.norm_exp, Complex.mul_re, Real.norm_eq_abs, sq_abs]
end Polar

namespace Closure
/-- ME-026: inner-product closure with a strictly positive regularizer. -/
def value {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (u v : E) (ε : ℝ) : ℝ := inner ℝ u v / (‖u‖ * ‖v‖ + ε)
theorem abs_lt_one {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (u v : E) (ε : ℝ) (hε : 0 < ε) : |value u v ε| < 1 := by
  have hd : 0 < ‖u‖ * ‖v‖ + ε := by positivity
  rw [value, abs_div, abs_of_pos hd, div_lt_one hd]
  exact (abs_real_inner_le_norm u v).trans_lt (by linarith)
end Closure

namespace Information
/-- ME-034: finite Shannon entropy in nats; zero-mass terms are zero. -/
def entropy {ι : Type*} [Fintype ι] (p : ι → ℝ) : ℝ :=
  - ∑ i, p i * Real.log (p i)
theorem entropy_nonneg {ι : Type*} [Fintype ι] (p : ι → ℝ)
    (h0 : ∀ i, 0 ≤ p i) (h1 : ∀ i, p i ≤ 1) : 0 ≤ entropy p := by
  apply neg_nonneg.mpr
  exact Finset.sum_nonpos fun i _ =>
    mul_nonpos_of_nonneg_of_nonpos (h0 i) (Real.log_nonpos (h0 i) (h1 i))
theorem entropy_point_mass {ι : Type*} [Fintype ι] [DecidableEq ι] (j : ι) :
    entropy (fun i => if i = j then 1 else 0 : ι → ℝ) = 0 := by
  simp [entropy]
/-- ME-092 on finite distributions with strictly positive reference mass. -/
def kl {ι : Type*} [Fintype ι] (p q : ι → ℝ) : ℝ :=
  ∑ i, p i * Real.log (p i / q i)
theorem kl_self {ι : Type*} [Fintype ι] (p : ι → ℝ) : kl p p = 0 := by
  apply Finset.sum_eq_zero
  intro i _
  by_cases h : p i = 0
  · simp [h]
  · simp [h]
theorem kl_nonneg {ι : Type*} [Fintype ι] (p q : ι → ℝ)
    (hp : ∀ i, 0 ≤ p i) (hq : ∀ i, 0 < q i)
    (hps : ∑ i, p i = 1) (hqs : ∑ i, q i = 1) : 0 ≤ kl p q := by
  have hterm (i : ι) : p i - q i ≤ p i * Real.log (p i / q i) := by
    rcases (hp i).eq_or_lt with h | h
    · simp only [← h, zero_sub, zero_div, zero_mul]
      exact neg_nonpos.mpr (hq i).le
    · have hlog := Real.log_le_sub_one_of_pos (div_pos (hq i) h)
      have hm := mul_le_mul_of_nonneg_left hlog h.le
      rw [Real.log_div (ne_of_gt (hq i)) (ne_of_gt h)] at hm
      rw [Real.log_div (ne_of_gt h) (ne_of_gt (hq i))]
      have hc : p i * (q i / p i) = q i := mul_div_cancel₀ _ (ne_of_gt h)
      nlinarith
  have hs := Finset.sum_le_sum (s := Finset.univ) (fun i _ => hterm i)
  simpa [kl, Finset.sum_sub_distrib, hps, hqs] using hs
/-- ME-093 for a finite joint table. Probability normalization is a separate
domain condition; this definition itself does not assert independence. -/
def mutualInformation {ι κ : Type*} [Fintype ι] [Fintype κ]
    (p : ι × κ → ℝ) : ℝ :=
  entropy (fun i => ∑ j, p (i, j)) + entropy (fun j => ∑ i, p (i, j)) - entropy p
theorem mutualInformation_swap {ι κ : Type*} [Fintype ι] [Fintype κ]
    (p : ι × κ → ℝ) :
    mutualInformation (fun z : κ × ι => p (z.2, z.1)) = mutualInformation p := by
  unfold mutualInformation entropy
  simp only [Fintype.sum_prod_type]
  rw [Finset.sum_comm (f := fun j i => p (i, j) * Real.log (p (i, j)))]
  ring
end Information

namespace Tiling
/-- ME-046 over a real vector space, for any chosen operator and real scale. -/
def apply {E : Type*} [AddCommGroup E] [Module ℝ E] (A : E → E) (φ : ℝ) (x : E) : E :=
  A (φ • x) + (φ - 1) • (x - A (φ • x))
theorem expansion {E : Type*} [AddCommGroup E] [Module ℝ E]
    (A : E → E) (φ : ℝ) (x : E) :
    apply A φ x = (2 - φ) • A (φ • x) + (φ - 1) • x := by
  unfold apply
  module
end Tiling

namespace Density
/-- ME-057 is a sum of four real density contributions. -/
def effective (matter field recursion rotation : ℝ) := matter + field + recursion + rotation
theorem nonneg (m f r o : ℝ) (hm : 0 ≤ m) (hf : 0 ≤ f) (hr : 0 ≤ r) (ho : 0 ≤ o) :
    0 ≤ effective m f r o := by unfold effective; positivity
end Density

namespace Born
/-- ME-060's normalization after an operator has been applied.
The zero-vector exclusion is essential. -/
def normalize {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (v : E) : E :=
  (‖v‖ : ℝ)⁻¹ • v
theorem normalized_norm {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (v : E) (hv : v ≠ 0) : ‖normalize v‖ = 1 := by
  simp [normalize, norm_smul, norm_ne_zero_iff.mpr hv]
theorem zero_normalization {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] :
    normalize (0 : E) = 0 := by simp [normalize]
/-- ME-060's displayed adjoint denominator on a complex Hilbert space. -/
def normalizeOperator {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [CompleteSpace E] (A : E →L[ℂ] E) (ψ : E) : E :=
  (Real.sqrt (RCLike.re (inner ℂ ψ ((A.adjoint ∘L A) ψ))))⁻¹ • A ψ
theorem operator_eq_normalize {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [CompleteSpace E] (A : E →L[ℂ] E) (ψ : E) :
    normalizeOperator A ψ = normalize (A ψ) := by
  rw [normalizeOperator, ← A.apply_norm_eq_sqrt_inner_adjoint_right ψ]
  rfl
theorem operator_norm {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [CompleteSpace E] (A : E →L[ℂ] E) (ψ : E) (h : A ψ ≠ 0) :
    ‖normalizeOperator A ψ‖ = 1 := by
  rw [operator_eq_normalize]
  exact normalized_norm (A ψ) h
/-- ME-061: probabilities of a finite family of complex amplitudes. -/
def probability {ι : Type*} [Fintype ι] (a : ι → ℂ) (i : ι) : ℝ :=
  Complex.normSq (a i) / ∑ j, Complex.normSq (a j)
theorem probability_nonneg {ι : Type*} [Fintype ι] (a : ι → ℂ) (i : ι) :
    0 ≤ probability a i := by
  exact div_nonneg (Complex.normSq_nonneg _) (Finset.sum_nonneg fun j _ => Complex.normSq_nonneg _)
theorem probability_sum {ι : Type*} [Fintype ι] (a : ι → ℂ)
    (ha : ∃ i, a i ≠ 0) : ∑ i, probability a i = 1 := by
  have hsum : 0 < ∑ i, Complex.normSq (a i) := by
    obtain ⟨i, hi⟩ := ha
    exact Finset.sum_pos' (fun j _ => Complex.normSq_nonneg _) ⟨i, Finset.mem_univ _, by
      exact lt_of_le_of_ne (Complex.normSq_nonneg _) (Ne.symm (by simpa using hi))⟩
  simp only [probability, ← Finset.sum_div]
  exact div_self (ne_of_gt hsum)
end Born
end MonolithicAnalysis
