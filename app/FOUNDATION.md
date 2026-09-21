# SOULCINEMA APP — PHASE 1 FOUNDATION

Status: ACTIVE BUILD
Branch: soulcinema-app-v1
Source baseline: Mobile V2 Official Launch Master

## Isolation rule
- Production branch main is locked.
- App work stays on soulcinema-app-v1 until E.P. approves a release.
- No app experiment may modify public/mobile-v2.html on main.

## Foundation contract
1. Preserve SoulCinema identity: black, gold, warm white, dark walnut; cinematic light; restrained motion.
2. Preserve experience architecture: Gate → Grand Lobby → Screening Theater → Music → Live → Production → Story → Journal.
3. One navigation owner and one media owner. Room changes must terminate media owned by the previous room.
4. Re-entry must be deterministic: enter → exit → enter again without dead clicks, frozen rooms, duplicate players, or hidden audio.
5. Live, Theater, and Music remain isolated media surfaces.
6. Build app foundation before room-by-room polish.
7. No E.P. testing until C.D. completes the full Phase 1 internal pass.

## Phase 1 build gates
- App shell / safe-area layout
- Gate and Lobby route state
- Room router
- Bottom navigation
- Media ownership / teardown
- Theater surface
- Music surface
- Live surface
- Production / Story / Journal surfaces
- Back/re-entry behavior
- App lifecycle handling
- Full internal regression pass

## Release rule
Nothing is called LOCKED until the affected full sequence is verified.
