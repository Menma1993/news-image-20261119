# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Menma1993/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Menma1993/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry v1 for make.fun bounty `news-image-20261119`: sums up Thursday 19 November 2026's world news in one 1024×1024 image — a cream broadsheet front page with 45 verified stories: 3 illustrated leads, 10 cards, a numbers strip, a world map with numbered pins, 28 numbered briefs and a sources footer.

## The image

`entry.png` — 1024×1024 PNG, a cream newspaper front page:

- **Masthead:** "Thursday 19 November 2026" — the only date printed anywhere in the image. Sub-line: "45 STORIES · 6 CONTINENTS · ONE DAY", plus a DATE-CHECKED badge: every story was first reported on Thursday 19 November 2026.
- **3 illustrated leads:** Trump, Xi and Putin open the first US–China–Russia trilateral summit in Shenzhen; Ukraine hits the Kerch bridge a third time; Iran strikes back across the Gulf.
- **10 illustrated cards:** ICJ rules on the Rohingya case; Bangladesh burns as Yunus home torched; COP31 ministers race to unblock talks in Antalya; Anthropic's $83 IPO sets a record; Cyclone Akvan nears Odisha; US and Venezuela sign a defence pact; Israel raids beyond Gaza's yellow line; troops mass on the Ethiopia–Eritrea border; IMF warns world debt nears 100% of GDP; North Korea expands uranium enrichment.
- **By the numbers strip (stories 14–17):** $81.3bn Anthropic raise, 50,000 evacuated in Odisha, 4.7% world inflation, $1tn South Korea exports.
- **Where it happened:** world map with numbered pins for the 12 mapped stories and a full region legend.
- **Briefs 18–45:** 28 one-line briefs in two columns, numbered continuously.
- **Sources footer:** "Every story was first reported on Thursday 19 November 2026. Sources: Reuters, AP, AFP, BBC, Al Jazeera and others. Original drawings."

The image was drawn programmatically (Pillow) from the verified story list; see `draw_20261119.py` in the builder's workspace (`news-image-20261119-work/`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=grvy5k3b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
