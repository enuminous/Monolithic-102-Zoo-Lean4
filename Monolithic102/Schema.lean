namespace Monolithic102

inductive FormalStatus where
  | formalized
  | partiallyFormalized
  | needsSpecification
  | sourceOnly
  deriving Repr, DecidableEq, Inhabited

structure EquationSpec where
  number : Nat
  canonicalId : String
  title : String
  sourceTag : String
  sourceExpression : String
  descriptor : String
  status : FormalStatus
  note : String := ""
  deriving Repr, Inhabited

inductive ZooDisposition where
  | conditionalStandardSurvivor
  | structuralSurvivor
  | empiricalTestRequired
  | openSpecification
  deriving Repr, DecidableEq, Inhabited

inductive ProofBoundary where
  | theoremCandidate
  | definitionOnly
  | empiricalOnly
  | blockedBySemantics
  deriving Repr, DecidableEq, Inhabited

structure AuditSpec where
  number : Nat
  canonicalId : String
  disposition : ZooDisposition
  proofBoundary : ProofBoundary
  typedCore : Bool
  dependencies : List Nat := []
  deriving Repr, Inhabited

end Monolithic102
