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
