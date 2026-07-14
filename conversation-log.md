# LiamGame — Conversation & Design Log

> A record of the design discussions and technical work on the DC/Marvel
> chase-tag fighting game (Pygame Zero). Saved 2026-06-02.

---

## The Game (overview)

A competitive **chase-tag fighting game** themed on DC (base roster) and Marvel
("echo" variants). 1v1 and team (e.g. 3v3) chase-tag: players alternate
offense/defense, tag to eliminate/swap roles. Built in **Pygame Zero** (Python).

- Roster target: ~10 DC characters + ~10 Marvel echoes.
- **Marvel echoes** are unlocked by playing the DC base character. Echoes are
  "different, not better."
- **Currency:** the word **"Victor"** (earlier candidates: Vici, Victorium,
  Strides — to test with playtesters).
- **Ability system:** Each character has **5 selectable abilities + 3 passives**.
  Players **unlock** abilities with currency and **select 2–3 per match** based
  on matchups (solves the keyboard-key-limit problem). Players start with 2
  simple abilities. Passives are separate: 1 default + 1–2 unlockable.

---

## Character Designs

### Superman
1. Ice Breath
2. Laser Vision
3. Haymaker (punch)
4. Heightened Senses + X-Ray (reveals hidden/invis, Among Us-style arrow +
   footstep trail)
5. Super Breath

**Passives:** Man of Steel (50% knockback resistance, default) · Solar Energy
(faster recharge in open areas) · Heightened Reflexes (auto-dodge first tag
attempt).

### Batman
1. Batarang
2. Smoke Bomb (AOE slow)
3. Grappling Hook
4. Explosive Batarang
5. Cape Stun

**Passives:** Utility Belt (20% shorter cooldowns + see enemy cooldowns,
default) · Detective (see where enemies used abilities) · **Contingency Plan**
(chosen — if stunned, next ability after recovery has no cooldown).

### Flash
1. Dash
2. Phase
3. Blitz (dashes across pre-marked points that appear/disappear every 5s)
4. Lightning Bolt (electrifies walls it hits)
5. Vortex (toggleable pull/push ring)

**Passives:** Recharged (lightning gives +5% speed 2s, no max) · Accelerating
(+0.5%/s speed, max +7.5%, resets on stop, afterimage at max) · Not There Just
Yet (rewind to position 2s ago).

### Boxer / Papa (boxer who also manufactures furniture)
1. Flying Punch (held key, -30% outside vision)
2. Desk Trap (halves map, pushes)
3. Not Desperation (throws walls as projectiles)
4. Never Done (5 punches, slight knockback)
5. Heavyweight (20% knockback resist + speed burst after hit)

**Passives:** Bouncy Legs (quick decaying acceleration) · Hunkered Down (3s
stationary = no knockback + dodges every 4th frontal hit, canceled by back
hits) · Adrenaline (stat boosts after landing hit/tag).

### Joker (partial — passives deferred)
- Card Throw
- Truckload of What? (exploding goon truck)
- House of Cards (suit selection: heart=buff, diamond=cutting card,
  clover=homing, spade=shovel stun/slow/confuse; card-number scaling proposed as
  4 tiers × 4 suits = 16 outcomes)
- Better than the Bat (laughing gas confuse)
- Hallucinations (fake attacks/clones)

Design intent: "chaotic and unpredictable, but the passives make him a bit more
skilled." **Passives not finalized — come back later.**

### Lex Luthor (transforms to Doomsday with R; one character slot)
1. Kryptonite Beam (turning beam, max 90°)
2. Lex Smash (leap + smash, destroys walls, buries = full stun)
3. Envious Fury (ram, takes no damage, -5% stat nerf stacking, vanishes on
   cooldown)
4. Force Field (360° shield, shots bounce, only he passes)
5. Great Chemistry Alone (summon fire + blots out sun, leaves kryptonite zone)
6. With This Treasure (summons Doomsday who kills Lex — **mandatory** 3rd move)

**Passives:** Optimized for Annihilation (whiffed ability = -10% cooldown) ·
Sore Stalemate (charges energy from hits, survives lethal once + brief
immunity) · 1A! (3x/round set last ability cooldown to 0 at 75% effectiveness —
references the 2025 Superman DCU movie).

### Doomsday (boss form; stronger, especially in FFA)
No optional moves. Losing = 3-tag kill.
1. Unneeded Hail Mary (pickup/throw; boss: wall stun)
2. Sponging Damage (block next attack; boss: permanent immunity to it)
3. Are You Dead Yet ×3 (punch combo; combos with ability 4)
4. It's a bird it's a plane it's a bird (vertical soar + slowing shockwave;
   boss: stun + launch up)
5. Death Charge (charge, destroys walls, carries enemies; boss: -40% damage)

**Passives:** Superman's a What Trick Pony (3 hits of same non-melee ability =
immune; boss: enemy loses ability for round) · Moving a Mountain (no knockback)
· Moved by a Mountain (push by walking) · cooldown-punch passive (on-cooldown
ability press = punch; boss: 3 on cooldown = uppercut) · I'm Losing And I Don't
Like That (enrage when hit without landing moves; boss: CC immune).
Status chain: stuns→slows→slows→confusions→confusions→knockback.

### Two-Face (coin flip built into every ability; heads=power, tails=utility)
Per-ability streaks, blind betting, wrong guess nerfs that variant for 2 uses.
1. But Guns Are Legal In This State Right Harvey? (gun: heads=bigger bullet,
   tails=spread)
2. I'll Be Nice Harvey (coin throw w/ shrapnel: heads=4 ricochets, tails=curves)
3. Which Side Did They See Harvey (teleport + knife stab: heads=random,
   tails=random "evil" target = whoever last hit him + designated villains like
   Lex/Joker)
4. Which Side Did You See Harvey (flips result, resets streak to lowest positive)
5. It Landed Straight Down The Middle (both heads+tails on next ability, then
   resets streak)

**Passives:** We're Getting Good Harvey (+2%/correct, max 8%) · I'm Used To It
(right side -10% damage, left side +10%) · No No Again (every 4th wrong =
70/30 reflip; right=streak continues, wrong=4-use nerf).

### Green Lantern (Hal Jordan) — IN PROGRESS, not finalized
Aggressive zoner. Constructs have individual durability but share a **construct
pool** (each ability beyond the 1st = -1 pool slot); multiple constructs
allowed; constructs vanish when stunned (not when confused/slowed); hammer can't
destroy his own walls; airplane needs one extra function (explode/bombs).

Proposed kit: 1) No Fear (wall) · 2) Emerald Hammer · 3) Air Corps (plane +
bomb) · 4) Emerald Cage (trap enemy) · 5) Oan Power Battery (restore pool).
Proposed passives: Fearless / Emerald Willpower / Test Pilot. **Not confirmed.**

### Other roster notes
- Wonder Woman, Aquaman also exist (kits not yet designed). Aquaman: trident
  throw/recall, wave push, sea creatures (partial).
- **Marvel echo pairings:** Superman→Iron Man (armor break) · Bane→Hulk (rage) ·
  Cyborg→War Machine · Batman→Black Panther · Flash→Quicksilver ·
  Wonder Woman→Captain America (bouncing shield + Rally Cry/Shield Bash) ·
  Green Arrow→Hawkeye (homing arrows + Light Feet) · Nightwing→Spider-Man.

---

## Technical Work

### Files
- **tag-game-vs-player.py** — main game (~4937 lines). Requires `import pgzrun`
  at top and `pgzrun.go()` at the very bottom to run as a standalone script.
- **tag-game-vs-bot.py** — single-player/tutorial + wave-mode foundation
  (Superman vs a distance-chasing bot). Intended to grow: diagonal movement,
  abilities, 3 difficulty levels, "tag in waves" (more/harder bots each round).

### Building a Windows .exe (solved)
Used **PyInstaller** with `--onefile`. Fixes discovered:
1. Run the .exe from a command prompt so error messages stay visible.
2. Add `import pgzrun` / `pgzrun.go()` so Pygame Zero initializes (`Actor`
   NameError otherwise).
3. Bundle pgzero's internal data:
   `--add-data "...\.venv\Lib\site-packages\pgzero;pgzero"`
   (fixes `FileNotFoundError: pgzero\data\icon.png`). **Confirmed working.**

### Cross-computer sync via GitHub (done)
Zip transfer failed ("unsupported binary/text coding"), so we used the existing
repo **https://github.com/liamnyc20-png/LiamGame.git** (branch `main`).
- Added `build/`, `dist/`, `*.spec`, `game.zip` to `.gitignore`.
- Committed source code + all new image assets + Luthor/Two-Face files; pushed
  to `main`.

**Everyday workflow:** `git pull` before starting · `git add -A` →
`git commit -m "..."` → `git push` when finished. Pull before, push after.

**School computer setup:** `git clone https://github.com/liamnyc20-png/LiamGame.git`
then File → Open Folder → LiamGame. Needs Python + `pip install pgzero` to run.

---

## Next Direction: Web Game (planned)

Goal: turn the game into a **browser game** so anyone can play from a link — no
Python, no install, works on locked-down school Chromebooks.

- **Tool:** `pygbag` — compiles Pygame / Pygame Zero to WebAssembly.
- **Hosting:** itch.io (easiest) or GitHub Pages (uses existing repo).
- **Main work item:** the game loop must become **async**, and heavy use of
  `time.time()` (cooldowns/stuns) needs reworking for the web runtime.
- **Plan:** best done at home where the game already runs, testing each change.

---

## Pending Tasks
- Finalize Green Lantern's abilities/passives.
- Design Aquaman's and Wonder Woman's full kits.
- Finalize Joker's passives.
- Design remaining Marvel echoes.
- Improve `tag-game-vs-bot.py`: diagonal movement, abilities, 3 difficulties,
  wave mode.
- Finish cooldowns for abilities.
- Web deployment (pygbag → itch.io / GitHub Pages).

---

## Working-style notes
- During design phases: talk/discuss, **no code unless explicitly asked**.
- Prefer being **shown proposed changes before they're applied**.
