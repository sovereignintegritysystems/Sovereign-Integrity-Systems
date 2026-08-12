# Sovereign Integrity Systems — Public Publication Boundary

Status: **ACTIVE PUBLICATION POLICY**  
Authority effect: **NONE** — this document constrains publication; it does not create legal, technical, financial, certification, provider, or operational authority.

## 1. Role

`sovereignintegritysystems/Sovereign-Integrity-Systems` is the canonical public GitHub publication projection for Sovereign Integrity Systems.

Its job is to make approved public material easy to discover and cite without turning GitHub account ownership or a public README into semantic authority.

## 2. Default-deny publication rule

Material is not publishable here merely because it exists in GitHub, Google Drive, a chat, a draft, an issue, a PR, a local workspace, or a provider projection.

Publication requires an explicit `PUBLIC_SAFE` classification or an equivalent governed public-release decision tied to the exact artifact/currentness being released.

If classification is absent, ambiguous, stale, or contradicted by a stronger source, the artifact does not cross the boundary.

## 3. Allowed public classes

Subject to currentness and exact claim ceilings, this repository may contain:

- company identity, brand, mission, and public-safe institutional descriptions;
- public product/platform descriptions;
- published research, defensive publications, public standards mappings, and public technical notes;
- public grant/proposal summaries only where disclosure is allowed and proposal/application status is stated accurately;
- public announcements, events, opportunities, engagement material, public contact paths, and recruiting material;
- public release notes, public interfaces, or public code when a separate release decision authorizes them;
- sanitized evidence summaries where the underlying source allows publication and the summary does not inflate the claim.

## 4. Prohibited or restricted classes

Do not commit or publish:

- passwords, API keys, tokens, SSH material, signing keys, recovery codes, seed phrases, credentials, or secrets;
- nonpublic personal information or protected data;
- privileged legal advice, executed confidential legal instruments, private corporate records, private cap-table implementation, banking, tax, payroll, insurance, or nonpublic finance;
- NDA, customer-confidential, partner-confidential, government-confidential, controlled-technical, export-controlled, procurement-sensitive, or security-sensitive material;
- `NDA_ONLY`, `FILE_FIRST`, or `DO_NOT_DISCLOSE` material unless and until the exact artifact is reclassified through the governing process;
- enabling unfiled invention detail that has not received an explicit public-release decision;
- raw vulnerability, exploit, red-team, security-control, recovery, credential, infrastructure, or operational detail whose release increases risk;
- internal R&D/Engineering control state, raw evidence, or provider-operation detail that has not been explicitly sanitized and admitted for public release.

Private GitHub visibility is not a secret-management system. Credentials and secrets should not be committed to the internal repository either.

## 5. Claim preservation

A public projection may only narrow a claim; it may not strengthen one.

Examples:

- source present ≠ executed;
- executed ≠ integrated;
- integrated ≠ effective;
- internal verification ≠ independent validation;
- proposal submitted ≠ award or contract;
- draft invention material ≠ patent filing or patent pending;
- standards orientation ≠ certification;
- provider success ≠ semantic authority.

Missing evidence remains `UNOBSERVED`.

## 6. Promotion path

The normal promotion path is:

1. identify the authoritative internal source and exact current version;
2. determine disclosure classification and applicable legal/contractual restrictions;
3. remove or transform restricted content without changing the supported meaning;
4. preserve source provenance and claim ceiling;
5. review the public diff as a public artifact, not as a private mirror;
6. admit it to this repository;
7. read back the provider state and record currentness where the internal control architecture requires it.

No automatic private-to-public synchronization is authorized by default.

## 7. GitHub Actions exclusion

GitHub Actions is outside the current SIS architecture. Publication does not require or consume GitHub-hosted workflows, checks, runs, logs, artifacts, runners, billing state, quotas, or conclusions. None of those states may satisfy or block publication, review, evidence, currentness, release, or claim status.

SIS currently has no consistent GitHub Actions billing relationship and will not create an architectural dependency on it before outside funding is available. Outside funding does not automatically re-admit GitHub Actions; a future use would require an explicit owner decision and fresh provider-independence review.

Historical provider automation records are provenance only. GitHub source hosting remains separate from GitHub Actions.

## 8. Demotion and correction

If public material becomes stale, overbroad, unsafe, superseded, or inconsistent with a stronger source, correct or withdraw it promptly. Historical public artifacts may be retained where useful, but must be clearly marked as historical/superseded when current interpretation could otherwise be misleading.

## 9. Boundary owners

The public repository does not own the underlying facts. Company-truth, technical, research, engineering, legal, financial, evidence, and provider states remain owned by their exact governed sources. This repository owns only the public GitHub publication projection and its publication-state currentness.
