# SOULCINEMA APP — PHASE 1 INTERNAL CHECKPOINT

Branch: soulcinema-app-v1
Status: INTERNAL BUILD VERIFIED — RUNTIME PREVIEW URL + REAL-DEVICE VALIDATION REMAIN

## Verified structurally
- Isolated app shell exists at app/index.html.
- Production main branch is not used for app edits.
- 27 view destinations detected.
- 68 data-go navigation targets detected.
- 0 missing route destinations.
- 0 duplicate view IDs.
- Core routes present: Gate, Grand Lobby, Music, Theater, Live, Production, Story, Journal, Visual Bible, About, Contact.
- Single hardStop media governor.
- Single Live owner / teardown path.
- Single Discovery owner / teardown path.
- Route changes invoke media teardown.
- Music teardown occurs when leaving Music.
- Live teardown occurs when leaving Live.
- visibilitychange, pagehide, beforeunload and freeze lifecycle stops are present.
- App safe-area shell is present.
- App route-state and media-epoch guards are present.

## Real-device validation still required before LOCK
- Gate → Lobby
- global navigation / re-entry
- Theater playback and exit teardown
- Music Discovery playback, pause, autoplay and exit teardown
- Live mount, audio and exit teardown
- rapid room switching
- background → foreground lifecycle
- portrait / landscape behavior
- child-view back chains
- no hidden audio after room transitions

## Lock rule
Do not call Phase 1 100/100 or LOCKED until real-device validation passes.

## Packaging verification
- Install manifest linked from app shell.
- Standalone/mobile app metadata present.
- Service worker registered only for /app/ scope.
- Service worker cache restricted to same-origin /app assets.
- External media, SoundCloud and Live are not intercepted by the app cache.
- Navigation uses network-first behavior with app-shell fallback.
- Dedicated preview routing configuration exists separately from production config.
- Runtime package is mirrored exactly under public/app for Next/Vercel static serving.
- Manifest start_url is explicit: /app/index.html#gate.
- Service-worker shell cache v3 uses explicit /app/index.html and manifest entries.
- GitHub App V1 verifier passes source/runtime parity and production-isolation gates.
- Vercel status checks pass for both soulcinema-master and soul-cinema-studio.
- Branch audit confirms App V1 is ahead of main with no production-file drift.

## Next gate
Resolve the verified isolated preview runtime URL for soulcinema-app-v1, then perform the real-device validation matrix above. Do not infer or guess a hostname. Production main remains untouched.
