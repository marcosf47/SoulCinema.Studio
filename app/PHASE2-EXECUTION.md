# SOULCINEMA APP — PHASE 2 EXECUTION

Branch: soulcinema-app-v1
Baseline: Phase 1 validated / locked

## Mission
Harden the validated Mobile V2-based App shell for installable mobile-app behavior without redesigning the approved experience.

## Non-negotiable locks
- Do not modify production main, public/index.html, or public/mobile-v2.html.
- Preserve Mobile V2 room architecture and black/gold cinematic identity.
- Preserve single-owner navigation/media model.
- Preserve SoundCloud as Music Discovery engine.
- Preserve Theater and Live portrait/landscape behavior.
- No parallel router or media governor.
- Draft PR remains unmerged without explicit E.P. authorization.

## Phase 2 gates
- install/standalone shell integrity
- safe-area behavior
- portrait/landscape app behavior
- lifecycle/background media teardown
- re-entry/state recovery
- offline shell fallback only; external media remains network-owned
- source/runtime parity
- CI + Vercel Preview green
- final consolidated device validation before Phase 2 lock

## Workflow
Build → internal/static verification → Preview/CI verification → single E.P. device checkpoint.
No micro-test requests.


## Android / Play packaging checkpoint
- Capacitor packaging identity: `studio.soulcinema.app` / `SoulCinema`.
- Web runtime source for native packaging: `public/app`.
- Android packaging commands are defined in `package.json`.
- CI now gates Capacitor identity, required dependencies, runtime path and packaging scripts.
- Both Vercel deployment statuses passed after the Android packaging CI gate.
- Production `main`, `public/index.html`, and `public/mobile-v2.html` remain outside the App V1 packaging work.
- Native Android project generation and signed Play release remain separate release-build gates; do not claim an AAB exists until that build is actually generated.


## Play Store release line
- Android native generation and debug Gradle build: PASS.
- Release AAB Gradle build: PASS.
- CI artifact publication: PASS; release AAB artifact produced.
- Play package identity: `studio.soulcinema.app`.
- Initial Play release metadata: versionCode `1`, versionName `1.0.0`.
- Secure signing path is wired to GitHub Secrets; no private signing material is stored in the repository.
- Release artifact integrity gate verifies the AAB exists, is non-empty, and records SHA-256 before upload.
- Remaining external release gates: actual upload signing credentials / Play App Signing enrollment, Play Console app record and required listing/policy declarations, then internal-track validation and production submission.
