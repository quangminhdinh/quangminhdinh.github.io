---
title: "The bottleneck is rarely the model"
date: 2026-05-28
lastmod: 2026-06-22
description: "Across four very different projects, the thing that capped quality was almost never the network. It was a systems or representation cost hiding underneath."
status: "evergreen"
tags: ["engineering", "systems", "lesson"]
links: ["conditioning-is-an-assumption", "cheap-structure-beats-heavy-machinery"]
---

I keep running into the same surprise: I sit down to make a model better, and the lever that actually moves the result is somewhere else.

In [Text-Conditioned IMLE](/projects/text-conditioned-imle/), the whole study was gated by nearest-neighbor matching. Until FAISS and a fused distance made it cheap, no conditioning experiment was runnable at all. Then, the moment it was fast, the matching stopped being where the difficulty lived.

In [Dynamic Radiant Foam](/projects/dynamic-radiant-foam/), multi-view training never finished, and not because the motion model was wrong. Re-triangulating the Voronoi mesh every step, plus the quiet assumption that the whole video fits in memory, is what ran out the clock.

In [Virtual Ring Try-On](/projects/virtual-ring-tryon/), the jump from 5 to 30 FPS came from stabilization and deleting frame conversions, not from a better hand tracker.

The model is usually the part I understand best, so it draws my attention, while the constraint that actually caps me sits in the plumbing around it: the matching, the data structure, the latency budget. So I now try to find the binding constraint before touching the network. Often the boring fix is the big one, which is its own note: {{< wl "cheap-structure-beats-heavy-machinery" >}}. And when the model genuinely is the problem, it is usually the representation that is wrong rather than the capacity, the point behind {{< wl "conditioning-is-an-assumption" >}}.
