---
title: "A shared channel is not a shared world"
date: 2026-06-22
lastmod: 2026-06-22
description: "Generative agents coordinate through language and memory, but they never share a world. That ceiling is the whole point."
status: "budding"
notekind: "concept"
tags: ["world-models", "multi-agent", "grounding"]
links: ["world-models", "multi-agent-grounding"]
---

The naive way to animate many agents is one big model with memory over everything, emitting each agent's behaviour in turn. That's a puppeteer, not a society: the agents have no state of their own, they're projections of a single process, and it shows the moment the situation drifts outside what the puppeteer already knows how to stage.

*[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)* (Park et al., 2023) is the serious answer to this. Each of the twenty-five agents in their sandbox town keeps its own memory stream, retrieves from it, reflects experiences into higher-level beliefs, and plans from there. No central controller. And it works: coordination genuinely emerges, the canonical example being one agent deciding to throw a Valentine's party and the invitation propagating through the town until others show up.

But notice where the ceiling sits. Every agent runs on the same frozen base model, and everything they share passes through natural language: memory written as text, intentions communicated as text. They share a *channel*, not a *world*. The town itself is authored, not something their representations co-evolve with. So the coordination is only ever as rich as what survives the text bottleneck, which is exactly the limit I worry about in {{< wl "multi-agent-grounding" >}}.

That's why I read the subtitle literally. *Simulacra.* You can get strikingly social behaviour out of per-agent memory plus a language channel and still not have agents that share a world. Closing that gap, a substrate the agents jointly maintain rather than a channel they message across, is what {{< wl "world-models" >}} has to be about.
