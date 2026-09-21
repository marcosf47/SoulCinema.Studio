# SOULCINEMA APP — PHASE 1 INTERNAL CHECKPOINT

Branch: soulcinema-app-v1
Status: ISOLATED PREVIEW IDENTIFIED — REAL-DEVICE VALIDATION REMAINS

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

## Isolated preview checkpoint
- Vercel deployment for commit 844de00 is Ready in Preview on branch soulcinema-app-v1.
- Exact branch preview hostname was identified from Vercel deployment details: soulcinema-master-git-soulcinema-app-v1-soul-cinema-studio.vercel.app.
- Share-link access was enabled for preview validation.
- Automated connector fetch remains blocked at Vercel access tooling; this is not recorded as an app runtime pass or failure.

## Next gate
Perform the real-device validation matrix above against the isolated Preview. Production main remains untouched.


## Final internal gate
- Route graph re-audited: 68/68 data-go targets resolve, 0 missing destinations, 0 duplicate IDs.
- Core rooms re-audited: Gate, Home, Theater, Music, Live, Production, Story, Journal, Visual Bible, About, Contact all present.
- Media ownership re-audited: route hardStop, Music teardown, Live mount/teardown all present.
- Lifecycle re-audited: visibilitychange, pagehide, beforeunload, popstate and freeze guards all present.
- Source/runtime parity re-audited: index, manifest and service worker match exactly.
- Automated verifier and both Vercel deployment checks are green on the hardened App V1 branch.

Internal/static validation is complete. Phase 1 remains UNLOCKED until the single consolidated real-device validation pass succeeds.


## Consolidated E.P. device pass
Run this only after C.D. declares TEST:
1. Open isolated App V1 Preview at /app/index.html#gate.
2. Gate → Lobby → Theater; play media; HOME; confirm media stops.
3. Music → play → pause → autoplay/next; HOME; confirm no hidden audio.
4. Live → confirm picture/audio; MUSIC; confirm Live audio stops immediately.
5. Production → child view → back → re-enter; repeat for Story and Journal.
6. Rapid switch: HOME → FILMS → HOME → MUSIC → HOME → LIVE → HOME → PRODUCTION → HOME.
7. Background app, return foreground, then re-enter a media room.
8. Rotate portrait ↔ landscape in Theater and Live, then return HOME.
9. Re-enter Theater, Music and Live after exits; confirm no frozen controls or duplicate playback.
10. Final sweep: Gate/Home and all bottom-nav destinations remain clickable; no hidden audio.

Pass rule: every step must pass in one consolidated session before Phase 1 can be called 100/100 or LOCKED.


## C.D. handoff gate
- Internal/static build verification: COMPLETE.
- Source/runtime parity: PASS.
- Route/media/lifecycle verifier: PASS.
- Vercel deployment checks: PASS.
- Production main/mobile-v2 isolation: PASS.
- Draft validation PR remains unmerged.
- Remaining acceptance gate: one consolidated real-device pass by E.P.

C.D. may now issue the single TEST checkpoint. Phase 1 remains UNLOCKED until that device pass succeeds.


## Music teardown defect closure
- E.P. real-device observation: SoundCloud Search/Discovery audio continued after leaving Music.
- Root cause isolated to the SoundCloud iframe owner, which was outside the audio/video-only hardStop path.
- App V1 fix now pauses and seeks the SoundCloud widget to 0, blanks/removes its iframe, clears the end watcher, and resets the Discovery owner on room exit.
- Source/runtime App V1 copies match after the fix.
- GitHub App V1 Preview Verify run #26: SUCCESS.
- Both Vercel deployment status checks after the fix: SUCCESS.
- Production main/mobile-v2 remained untouched.

Acceptance status: internal closure complete; consolidated real-device pass remains the final lock gate.
