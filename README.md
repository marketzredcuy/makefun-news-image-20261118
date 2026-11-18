# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/marketzredcuy/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/marketzredcuy/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of Wednesday 18 November 2026:
a classic newspaper front page with 42 stories — a globe icon +
"THE WORLD'S NEWS" masthead + dark-blue nav bar, 12 main story cards
(Iran striking Kuwait and Bahrain, the US strike on Qeshm Island,
Ukraine hitting the Kerch Bridge again, Xi hosting Putin before the
Trump trilateral, Trump meeting Marcos on his way to China, Houthi
drones at the Saudi pipeline, Democrats winning Alaska and the Senate,
Ebola more than doubling in Congo, Nvidia beating earnings with
revenue doubled, Israel electing a new speaker, Cyclone Xavier hitting
the Cook Islands, the Anthropic IPO pricing), each with a numbered
tag + category ribbon + image + headline + explainer, plus 30 more
stories in the "ALSO ON WEDNESDAY" list in 3 columns, and a
world-landmarks skyline strip at the bottom. All facts verified
against real reporting of the day.

`main.py` copies the pre-composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies size, format and
dimensions (at most 1 MiB and 1024x1024, and square).

## Stories

Twelve main stories, each illustrated with its own photo:

1. Iran strikes Kuwait and Bahrain after the US hit Qeshm Island.
2. US jets strike a Revolutionary Guard missile site on Qeshm.
3. Ukraine hits the Kerch Bridge for a second day in a row.
4. Xi Jinping hosts Vladimir Putin in Shenzhen before the Trump talks.
5. Trump meets Marcos Jr. and flies on to China for APEC.
6. Houthi drones target the Saudi East-West pipeline near Riyadh.
7. Democrats win Alaska and take the Senate 56-44.
8. The Ebola outbreak in Congo more than doubles.
9. Nvidia beats earnings as revenue doubles to $115.8B.
10. Israel's parliament elects Matan Kahana as speaker.
11. Category 5 Cyclone Xavier slams the Northern Cook Islands.
12. The Anthropic IPO prices ahead of its Thursday debut.

Thirty more stories fill the "ALSO ON WEDNESDAY" list: the Board of
Peace rebuking Israel and Hamas, Putin ruling out serious peace
talks, Xi against protectionism, Myanmar reviewing ASEAN, a US
officer held for spying for Russia, an AI-found flaw in Java, the US
losing measles-free status, cold killing in Gaza tents, NSA outages,
a Russian plane crash killing 19, oil slipping, the World Court on
Myanmar, Trump's Iran report, British sanctions, COP31 rows, two
Hamas commanders killed, Russia's 20-million-drone plan, a US MQ-9
shot down near Hormuz, Patriot systems targeted in Kuwait, quakes
in Papua New Guinea and Romania, a solar flare, South Korea leaning
to Beijing, NATO's new communications plan, the EU carbon tax, gold
below $3,800, Target's best sales in five years, Slay the Spire 2
nearing 8 million sales, Xiaomi's Paris launch, and Alonso and Loeb
joining Aston Martin for Dakar.

## Design

The front page follows the classic broadsheet: a globe icon and the
"THE WORLD'S NEWS" masthead, a dark-blue navigation bar, a 4x3 grid
of twelve illustrated story cards with numbered tags and category
ribbons, a three-column "ALSO" list, and a golden-hour strip of
world landmarks above the footer bar. Every headline and date was
checked against real reporting from Wednesday 18 November 2026.

## Run it

```sh
python3 main.py
```
