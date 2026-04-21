---
title: "Grounding signals beyond language"
date: 2026-02-20
lastmod: 2026-03-30
description: "If we want agents to share more than what can be said, the grounding signal has to be richer than text."
status: "seedling"
tags: ["world-models", "grounding", "research-agenda"]
links: ["conditioning-is-an-assumption"]
---

Natural language is a powerful interface, but it's a lossy projection of what agents need to coordinate on. Intentions, timing, attention, and affect all matter, and most of them don't survive the text bottleneck.

Open question: what does a grounding signal look like if we stop privileging text? Some candidates I want to think through —

- **Embodied state traces**: position, velocity, gaze direction as first-class citizens.
- **Attention as a signal**: what an agent *isn't* looking at is as informative as what it is.
- **Counterfactual rollouts**: a short imagined future as part of the message.

Prof. Freda Shi's work on how grounding actually emerges inside model computations is a useful empirical handle on this — it suggests the signal we need may already be latent in models we have, if we knew where to look.

See also: {{< wl "conditioning-is-an-assumption" >}}.
