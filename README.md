# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/SYOUTOUI/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/SYOUTOUI/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Sum up 23 November 2026's world news in one image.

Entry for https://make.fun/bounty/news-image-20261123
($100 prize pool, 50 places; deadline 2026-11-25 09:00 JST).

Run: `python3 main.py` — writes `/output/entry.png`.

Referral: https://make.fun/r/nde51zwq

## What the image shows

- **23 NOVEMBER 2026 — THE WORLD IN ONE DAY**
- NVIDIA brings back Huang — shares jump about 30% as Jensen Huang returns as CEO.
- Ukraine hits Russian ships — seven sea drones sink a warship off Libya; cargo ship Angara hit.
- COP31 ends with no deal — climate talks in Antalya collapse over fossil fuels.
- Belgium strike grounds flights — national strike cancels nearly all flights at Brussels and Charleroi.
- Houthis hit Saudi refinery — Yemen's Houthis claim an attack on a Red Sea oil refinery.
- Indonesia factory fire — 24 killed, 34 missing in a Banten candy factory fire.

Sources: public news coverage of 23 November 2026 (Daily Mirror,
Underlines, Broadcast Prism, Pollar, Seldon Report).

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled
image `asset/entry.png` to `/output/entry.png`. The output is byte-identical
on every run. `render.py` is the readable source the image was made from
(Pillow, render-time only — not used by `main.py`).

- Output: 1024 x 1024 px PNG (limit: 1024 x 1024, 1 MiB).
- Verified: two consecutive runs produce identical SHA-256.

## License

MIT — see LICENSE.
