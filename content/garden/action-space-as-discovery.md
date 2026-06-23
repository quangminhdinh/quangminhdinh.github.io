---
title: "When discovering the action space is the game"
date: 2026-06-22
lastmod: 2026-06-22
description: "Text adventures let you guess at an open verb set; modern games hand you a closed one. The same tension shows up in agent action spaces."
status: "budding"
notekind: "source"
tags: ["world-models", "grounding", "game-design"]
links: ["world-models", "multi-agent-grounding"]
---

Jesse Schell makes an observation in *[The Art of Game Design: A Book of Lenses](https://en.wikipedia.org/wiki/The_Art_of_Game_Design:_A_Book_of_Lenses)* that I keep coming back to for reasons that have nothing to do with games.

Early text adventures supported hundreds of verbs, and part of playing was discovering which actions even existed. You found puzzles by guessing that you could "spin the fish" or "tickle the monkey." Modern visual games shrank that down to a small, fully known action set, because you can't render an arbitrary verb. Schell's twist is that the old openness was partly an illusion: for every verb the parser knew, there were thousands it didn't, and that mismatch was its own kind of frustration.

What I take from it: this is really about *action spaces*, and the trade has no free side. A large, open, discoverable action space is expressive but unbounded, hard to learn, and quietly fake at the edges. A small closed one is legible but caps what can emerge.

For {{< wl "world-models" >}} the interesting move is to refuse both. Instead of enumerating a verb list, can an agent *ground* its affordances in the world, so the action space is discovered from what the environment supports rather than handed over as a fixed menu? That reframes {{< wl "multi-agent-grounding" >}}: agents need to discover what they can do to each other, not just what they can say.
