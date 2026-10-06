# SOULCINEMA APP V1 — RELEASE METADATA

Status: PRE-RELEASE

- App name: SoulCinema
- Android application ID: studio.soulcinema.app
- Package version: 1.0.0
- Android versionCode: 1
- Android versionName: 1.0
- Web runtime: public/app
- Android scheme: https
- Distribution target: Google Play
- Release artifact target: Android App Bundle (.aab)

## Release integrity
CI must verify source/runtime parity, native package identity, Android manifest security, App Bundle archive integrity, embedded SoulCinema payload parity, and production isolation before an artifact is accepted.

## Signing boundary
Release signing credentials are intentionally not stored in this repository. A signed Play release remains pending until the signing / Play App Signing path is configured securely.

## Production boundary
App packaging work must not modify main or public/mobile-v2.html. Draft PR #1 remains unmerged unless E.P. explicitly authorizes merge.
