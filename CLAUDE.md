# CLAUDE.md

Guide for any Claude (or person) picking up this project. Read it before changing a game.

## What this is

Three small browser games designed by John's young child, who comes up with the ideas and asks for
changes in plain kid words ("make it more realistic", "need things less frequently"). John (the
parent, GitHub `jsholmes`) sometimes writes too. The games were built in claude.ai as **Artifacts**
(single HTML pages), and this repo is where their source lives.

How to work with them:
- The kid often writes the requests. Reply simply, kindly and encouragingly, in small visible steps.
- Do what the kid asks literally first (they notice details: "only the leaves should wiggle", "animals
  walk down the path, not up"). If something is unsafe or can't be done, offer a fun swap.
- Kid safety: no personal info in the games (no hometown, school, last name, photos). Everything is
  saved only in the browser (`localStorage`); nothing is sent anywhere. The repo is public, so keep the
  child's name out of committed files too.
- Ask John before anything that can't be undone (new repos, deleting saves, publishing elsewhere).

## Layout

| Path | What |
|---|---|
| `index.html`, `manifest.json`, `icon.png`, `icon-512.png`, `.nojekyll` | **The live GitHub Pages site** (Best Tree Friends, iPad/standalone build). Generated, don't hand-edit `index.html`. |
| `talking-tree/index.html` | Best Tree Friends **source** (the claude.ai artifact page). Edit this one. |
| `talking-tree/build-ipad.py` | Builds the root `index.html` from the source. |
| `little-wings/index.html` | Little Wings source (bird game). |
| `ferns-spa/index.html` | Fern's Spa source (salon game). |

Every page is one self-contained HTML file (inline CSS + JS, only Google Fonts from outside). No
build tools, no dependencies. The source files are artifact *fragments* (they start with `<title>`,
no `<html>`/`<head>`): claude.ai wraps them when publishing, and browsers also open them fine as is.

## The games

### 1. Best Tree Friends (`talking-tree/`)
Grow-your-own talking tree. First name → pick a place (meadow, beach, canyon) → 7-question quiz →
one of 6 trees (oak, cherry, willow, apple, pine, maple) → name it → care for it (water, sun, hug,
sing, pull weeds; needs drop in real time) → 6 growth stages. The tree chats with written-in keyword
replies (no live AI); Wise Willow is the "smart" one (calculator, spelling, facts). Quiz animal friend
visits; wild animals wander in; real-clock sky, sun times, moon phase, seasons by date, holiday
decorations, tap-the-weather buttons (pages can't read real weather or location), sleep mode, lullabies,
tutorial, multiple worlds, grow a forest (plant another tree once one is fully grown), 8 special unlockable
trees (Rainbow → Star), merge worlds. Saves: `localStorage` key `talking-tree-worlds`.
- claude.ai artifact: https://claude.ai/artifact/3zgbaH8WnPqkt3RnYTAJvV (declares the `tts` capability).
- Live iPad version: https://jsholmes.github.io/best-tree-friends/ (Safari → Share → Add to Home Screen).

### 2. Little Wings (`little-wings/`)
Bird survival + territory. Pick a real species (robin, bluebird, cardinal, blue jay, goldfinch, house
sparrow), name it, pick a home in a 3×3 map of places. Grow Nestling → Fledgling → Juvenile → Adult →
Top Bird by eating; Tummy, Water and Rest bars; cats, snakes, hawks, owls at night; rivals peck you in
their land; win a place by sitting on its stump. Day/night every 5 minutes, sleep in the nest, lily pads
to drink in the pond, multiple worlds. WebAudio chirps only. Saves: `localStorage` key `little-wings-worlds`.
- claude.ai artifact: https://claude.ai/artifact/FgkAR2NYNePcxwYqWTLzpv

### 3. Fern's Spa (`ferns-spa/`)
Nail and hair salon. Customers (girls and boys) arrive with an order; do nails (soak, file, polish,
designs, top coat), hair (wash, dye, style), makeup, clothes, extras; ~75% arrive with a feeling and a
need (water, tea, cookie, blanket, kind words…) shown in a Care tab with a mood meter. Earn coins, buy
unlocks and salon places, hire helpers (Sam cleans, Kai front desk, Lulu DJ), clean floor messes, close/open
shop. Only customers are shown on the stage (the kid asked to hide you and the helpers). WebAudio chimes only.
Saves: `localStorage` key `sparkle-salon-v1`.
- claude.ai artifact: https://claude.ai/artifact/AsavkkFtxBC1G14bRHKNRY

## Voice rules (important)

- **Never use the browser's built-in `speechSynthesis` voice.** John asked for this; the kid finds it robotic.
- In the claude.ai artifact, Best Tree Friends talks with the artifact `tts` capability
  (`window.claude.use("tts")`; tree voice `rounded`, animal voice `airy`). If `tts` is missing (Safari,
  mobile apps, GitHub Pages) the game stays silent with speech bubbles and shows a one-time toast.
- So the GitHub Pages / iPad version is silent. Only add the device voice there if John explicitly opts in.
- Little Wings and Fern's Spa have no speech at all, only synthesized sound effects.

## Build and deploy

Best Tree Friends:
1. Edit `talking-tree/index.html`.
2. `python3 talking-tree/build-ipad.py` → rewrites root `index.html` (adds iPad meta tags, manifest,
   icons, safe-area padding, and swaps a kid-name comment for "you").
3. Commit both files and push `main`. GitHub Pages (Settings → Pages → Deploy from branch `main`, `/` root)
   publishes in a minute or two. Pages was enabled by hand by John; Claude cloud sessions usually can't
   reach the Pages API or `*.github.io`, so the live site can't be checked from there.
4. If you have claude.ai artifact access, republish the source to the same artifact URL so both stay in sync.

Little Wings and Fern's Spa: edit the file, commit, push. They are **not** linked from the site and have no
iPad wrapper yet, but because Pages serves the whole branch they are reachable at
`https://jsholmes.github.io/best-tree-friends/little-wings/` and `.../ferns-spa/`. If the kid wants them
as iPad home-screen apps, do what `build-ipad.py` does (meta tags, a manifest, icons) for each.

Testing: open the file in a browser, or `python3 -m http.server` in the repo and load it with Playwright.
There are no automated tests. Dev hooks in the tree game: `HOLI_TEST` (month) and `SEASON_TEST`.

## Where the canonical copy lives

The original project (claude.ai project "Addie's Game") kept working copies in its shared folder
(`talking-tree/`, `bird-game/`, `salon-game/`) and published them as the artifacts above. On 2026-11-24
all three were checked: the project files, the published artifacts and this repo matched. From now on,
**treat this repo as the source of truth**: after any change elsewhere, copy it back here and push.

## In progress / open ideas

Nothing is half-built. All three games were working and up to date on 2026-11-24. Loose ends:
- Little Wings and Fern's Spa aren't set up as iPad home-screen apps (only if the kid or John asks).
- Saves are per device and per browser; syncing between devices would need a backend (not done on purpose).
- Best Tree Friends still has unused avatar code from an avatar feature the kid asked to remove.
- The tree source's latest version notes (v1 to v74) live in the old project memory; the code itself is the
  real record, with comments marking each feature.
