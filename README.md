# news-image-20261118 — Wednesday 18 November 2026

A classic newspaper front page summing up the world's news of
Wednesday 18 November 2026: **35 stories, 6 continents, one day**.

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/marketzredcuy/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/marketzredcuy/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

`main.py` copies the pre-composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies size, format and
dimensions (at most 1 MiB and 1024x1024, and square).

## Stories

Twelve main stories, each illustrated with its own flat icon:

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

Twenty-three more stories fill the "ALSO ON WEDNESDAY" list: the Board
of Peace rebuking Israel and Hamas, Putin ruling out serious peace
talks, Xi against protectionism, Myanmar reviewing ASEAN, a US officer
held for spying for Russia, an AI-found flaw in Java, the US losing
measles-free status, cold killing in Gaza tents, NSA outages, a
Russian plane crash killing 19, oil slipping, the World Court on
Myanmar, Trump's Iran report, British sanctions, COP31 rows, two Hamas
commanders killed, Russia's 20-million-drone plan, a US MQ-9 shot
down near Hormuz, Patriot systems targeted in Kuwait, a quake in
Papua New Guinea, a solar flare, South Korea leaning to Beijing, and
gold below $3,800.

## Design

The front page follows the classic broadsheet: a globe icon and the
"THE WORLD'S NEWS" masthead, a dark-blue navigation bar, a 4x3 grid
of twelve illustrated story cards with numbered tags and category
ribbons, a "WHERE IT HAPPENED" world map with numbered dots marking
where each main story happened (the map is a real Natural Earth 110m
land silhouette with the dots placed at the true locations), a
three-column "ALSO" list, and a sources line at the bottom. Every
headline and date was checked against real reporting from Wednesday
18 November 2026.

## How the image was made

The page was rendered from an HTML layout (build_newspaper.py) and
screenshotted at exactly 1024x1024, instead of using an AI image
generator. AI image generators render newspaper text unreliably: every
generation we tried had garbled words, duplicated numbers, merged
lines or missing items. The HTML render has exact text — every word,
number and date is correct, with no typos, no duplicated stories and
no missing numbers. The map dots sit on the true locations; the three
Gulf dots are nudged a few pixels apart so their circles do not hide
each other, which is standard practice for clustered map points.
