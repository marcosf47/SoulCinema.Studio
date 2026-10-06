# SOULCINEMA APP V1 — PLAY RELEASE CHECKLIST

Status: PRE-RELEASE HARDENING
Branch: soulcinema-app-v1
Production main: UNTOUCHED

## Verified technical gates
- Mobile V2-based App V1 experience baseline preserved.
- Source/runtime parity verified by CI.
- Capacitor Android clean bootstrap verified.
- Java 21 Android toolchain verified.
- Gradle debug App Bundle build verified.
- Exactly one debug AAB required by CI.
- AAB SHA-256 emitted by CI.
- AAB retained as CI artifact.
- Production isolation gate verified.
- Vercel preview checks verified.

## Release gates still required
- Google Play developer identity/contact verification complete: PASS (E.P. verified email and phone in Play Console on 2026-09-22).
- Final Android application identity/versioning confirmed by CI: studio.soulcinema.app / versionCode 1 / versionName 1.0.
- Release signing / Play App Signing path configured (pending; no secrets stored in repository).
- Signed release AAB generated and verified (pending signing credentials / Play App Signing path).
- Store icon, feature graphic, screenshots and listing copy prepared.
- Play Console app-content declarations completed.
- Internal testing release uploaded and validated.
- Production rollout only after E.P. approval.

## Hard locks
- Do not modify main or public/mobile-v2.html for App packaging.
- Do not merge draft PR #1 without explicit E.P. authorization.
- Do not label debug AAB as Play production release.
- Do not commit keystores, passwords, signing secrets or service-account credentials.

## Play Console creation handoff — 2026-09-22
Repository-controlled preflight is green (App V1 Preview Verify #134 + both Vercel checks).
Use these locked values when creating the Play Console app record:
- App name: SoulCinema
- Default language: English (United States)
- App or game: App
- Free or paid: Free for initial release
- Android package/application ID after first AAB upload: studio.soulcinema.app
- Initial versionCode: 1
- Initial versionName: 1.0
- Release format: Android App Bundle (AAB)

Do not create a merchant account for this initial free release. Do not change package identity. Do not upload the debug CI AAB as a production release. Play App Signing / secure signed release artifact remains the next release gate.
