---
title: "A shared channel is not a shared world"
date: 2026-06-22
lastmod: 2026-10-24
description: "Generative agents live in an explicit town you can edit, but the town has no physics and their intentions only travel as text. That ceiling is the whole point."
status: "budding"
notekind: "concept"
tags: ["world-models", "multi-agent", "grounding"]
links: ["world-models", "multi-agent-grounding"]
---

The naive way to animate many agents is one big model with memory over everything, emitting each agent's behavior in turn. That's a puppeteer, not a society: the agents have no state of their own, they're projections of a single process, and it shows the moment the situation drifts outside what the puppeteer already knows how to stage.

*[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)* (Park et al., 2023) is the serious answer to this. Each of the twenty-five agents in their sandbox town keeps its own memory stream, retrieves from it, reflects experiences into higher-level beliefs, and plans from there. No central controller. And it works: coordination genuinely emerges, the canonical example being one agent deciding to throw a Valentine's party and the invitation propagating through the town until others show up.

But notice where the ceiling sits. In one sense the agents do share a world: the town is an explicit tree of areas and objects, and users can even change an object's state in plain language. That part is exactly right. What the town lacks is physics. When an agent uses the stove, the stove's new state is whatever the LLM is prompted to say it is. And everything about the agents themselves passes through natural language: memory written as text, intentions communicated as text. They share a *channel* for what they mean to do, not a world that holds it. So the coordination is only ever as rich as what survives the text bottleneck, which is exactly the limit I worry about in {{< wl "multi-agent-grounding" >}}.

That's why I read the subtitle literally. *Simulacra.* It's the mirror image of today's video world models. Those render a realistic world but keep its state implicit in the pixels. Generative Agents keeps an explicit state you can intervene on, but with no physics, no realism, and dynamics decided by an LLM's guesses. {{< wl "world-models" >}} needs both halves: a state that is explicit *and* physically grounded, with the agents' goals inside it.
