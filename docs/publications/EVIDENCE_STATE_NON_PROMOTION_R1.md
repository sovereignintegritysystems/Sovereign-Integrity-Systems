# Evidence-State Non-Promotion

**Public technical note R1 — 14 August 2026**  
Sovereign Integrity Systems (SIS), Saskatchewan, Canada

Status: **PUBLIC_SAFE technical contribution**. This note describes a general assurance method. It is not a certification, standard, legal opinion, customer result, security approval or claim that SIS invented every underlying assurance concept.

## Abstract

High-assurance work often fails at the boundary between a true observation and the stronger conclusion people want to draw from it. Source code exists, therefore it is treated as executed. A test passed, therefore a deployed system is treated as effective. A simulation behaved well, therefore a physical system is treated as validated. A proposal was acknowledged, therefore interest or adoption is inferred.

Evidence-state non-promotion is a simple rule for preventing that class of error:

> **An observation may satisfy only the evidence state it actually demonstrates. A stronger state requires its own evidence.**

The method is deliberately domain-neutral. It can be applied to software assurance, physical testing, scientific measurement, AI governance, procurement, organizational controls and public claims.

## 1. The state ladder

A useful generic ladder is:

`CLAIMED → SOURCE_PRESENT → EXECUTED → INTEGRATED → EFFECTIVE → INDEPENDENTLY_REPRODUCED → QUALIFIED_OR_CERTIFIED`

Not every domain needs every state and some domains require additional states, but the direction matters: evidence can move a proposition only as far as the observation justifies.

Examples:

- `SOURCE_PRESENT` means relevant source or configuration exists at an exact identity/current version.
- `EXECUTED` means an identified implementation actually ran under an identified execution context.
- `INTEGRATED` means the result or component was admitted into the intended larger system or workflow.
- `EFFECTIVE` means it produced the intended effect under the conditions relevant to the claim.
- `INDEPENDENTLY_REPRODUCED` means a sufficiently distinct observer, producer or institution reproduced the relevant result.
- `QUALIFIED_OR_CERTIFIED` exists only where an authorized qualification/certification process actually establishes it.

A system may be very strong at one state and genuinely `UNOBSERVED` at the next.

## 2. Why non-promotion matters

The rule protects against several common reasoning errors.

### Source-to-runtime promotion

A source review, static proof or generated artifact cannot establish that the exact production/runtime path executed correctly. It may strongly reduce uncertainty, but runtime evidence is a separate observation.

### Simulation-to-physical promotion

A simulation can validate mathematics, sensitivity, control logic or experiment design. It is not a physical measurement and cannot establish field effectiveness by itself.

### Internal-to-independent promotion

A second internal review can be valuable without being independent. Shared people, models, datasets, prompts, tools or assumptions can create common-mode reasoning. Independence should be defined by the claim, not by the number of documents produced.

### Process-to-outcome promotion

A mature process can increase the likelihood of good outcomes without proving a specific outcome. A quality system is not a substitute for the acceptance evidence of a particular product, and one successful product is not proof that a quality system is effective over time.

### Contact-to-adoption promotion

An application, meeting, acknowledgement, press mention or exploratory discussion is not an award, customer relationship, endorsement, adoption or policy influence unless the counterparty evidence establishes that stronger state.

## 3. `UNOBSERVED` is a valid state

A missing observation is not automatically failure.

`UNOBSERVED` means the evidence required to make the stronger proposition has not been admitted. It should be accompanied by:

1. the proposition that remains unobserved;
2. the observation capable of resolving it;
3. the producer or authority capable of making that observation;
4. the exact evidence class required;
5. any dependency that must be completed first.

This makes uncertainty operational rather than rhetorical.

## 4. Evidence identity

Evidence should be bound tightly enough that it cannot silently drift to a different subject.

For software or digital systems this may include:

- source or configuration identity;
- toolchain/runtime identity;
- target or execution context;
- input/candidate identity;
- authority ceiling;
- timestamp/currentness;
- result and receipt identity.

For physical measurement this may instead require:

- specimen/sample identity and custody;
- instrument and calibration state;
- method;
- environmental conditions;
- uncertainty;
- raw-data custody;
- observer/institution identity.

The identity tuple should fit the proposition. Extra identifiers that do not protect meaning are bookkeeping; missing identifiers that allow the subject to change are an assurance defect.

## 5. Reuse without cross-credit

One evidence object can support several decisions, but each decision must interpret it through its own evidence gate.

For example, a successful target test may simultaneously support:

- the runtime-execution record;
- a product-readiness review;
- a quality-management review;
- a customer diligence packet.

It does **not** mean those four states are equivalent. The shared evidence is reused; the semantics are not collapsed.

## 6. Falsifiable conformance tests

An organization claiming to use evidence-state non-promotion should pass at least these hostile tests.

### Test A — missing runtime

Give the process a complete source implementation and extensive static evidence but no execution receipt.

**Expected result:** source/static states may advance; runtime state remains `UNOBSERVED`.

### Test B — successful simulation

Give the process a highly successful simulation with no physical observation.

**Expected result:** simulation/model evidence advances; physical-effect state remains `UNOBSERVED`.

### Test C — internal consensus

Give the process several agreeing internal analyses generated by the same people/tools.

**Expected result:** confidence may change, but independent-validation state does not advance without producer/institution-distinct evidence.

### Test D — external acknowledgement

Give the process proof that a proposal or inquiry was received but no substantive adoption or award evidence.

**Expected result:** submission/receipt state advances; customer/adoption/award state does not.

### Test E — stale evidence

Give the process a valid result for an old source/configuration after a relevant material change.

**Expected result:** historical evidence remains preserved but current-state promotion is blocked until equivalence/currentness is established.

A process that fails these tests is vulnerable to evidence inflation even if its underlying engineering is strong.

## 7. Correction and negative evidence

Negative evidence should not disappear merely because it weakens a preferred story.

Useful records include:

- failed experiments;
- invalidated assumptions;
- stale or superseded evidence;
- rejected hypotheses;
- disagreement between independent reviewers;
- predictions that did not resolve as expected;
- corrective actions that failed their effectiveness check.

An assurance system should become more credible when it exposes and correctly bounds its failures.

## 8. Where the method is most useful

Evidence-state non-promotion is especially useful when a program mixes evidence classes that are easy to confuse:

- high-assurance or safety-critical software;
- cybersecurity and cryptography;
- AI-assisted decision systems;
- physical R&D and measurement;
- critical infrastructure and operational technology;
- procurement and technical qualification;
- standards and conformity work;
- institutional governance and public claims.

## 9. What would falsify or weaken this method?

This method should not be accepted because SIS published it. Useful criticism includes:

- a domain where the proposed separation creates systematic false negatives or unnecessary duplicate evidence;
- a stronger formal model that preserves the same non-promotion property with less operational cost;
- evidence that a listed state distinction is semantically invalid in a particular domain;
- a case where evidence reuse can safely collapse two states under clearly specified equivalence conditions;
- a demonstration that the method causes measurable assurance theatre rather than better decisions.

SIS welcomes substantive criticism, competing formulations and examples where the method should be narrowed.

## 10. Public claim boundary

This note is a public, falsifiable contribution. Publication establishes only that the contribution is public and attributable at this revision. It does **not** establish originality over all prior art, peer review, independent validation, standards adoption, policy influence or thought-leader status.

Contact for technical critique or independent application: **cgust.dev@gmail.com**.
