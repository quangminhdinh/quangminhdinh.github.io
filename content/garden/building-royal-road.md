---
title: "What would it actually take to build Royal Road?"
date: 2026-06-22
lastmod: 2026-06-22
description: "Through a researcher's lens: the properties that make Royal Road great, how close today's LLM-driven games get, and the gap that remains."
status: "budding"
notekind: "concept"
tags: ["world-models", "emergence", "research-agenda"]
links: ["shared-channel-not-shared-world", "what-is-a-world-state", "action-space-as-discovery", "world-models", "phd-motivation"]
---

Strip away the fandom and read [Royal Road](https://the-legendary-moonlight-sculptor.fandom.com/wiki/Royal_Road) as a spec. Why is it great, and what would building it actually require?

Decomposed, the magic is four properties stacked: an open, discoverable action space; a world that absorbs your actions as lasting consequence; NPCs with their own memory and goals; and emergence, which is just what you get when the first three hold at once.

The honest status of each, in current terms:

- **Generating the world** is the closest. Shams et al. ([2023](https://arxiv.org/abs/2308.13548)), the Holodeck-style *Infinitia*, have LLMs and image models generate maps, quests, NPCs, and mechanics for an open-ended world from prompts alone.
- **Local emergence** works. Peng et al. ([2024](https://doi.org/10.1109/CoG60054.2024.10645607)) get player-driven, unscripted paths out of non-deterministic LLM NPCs inside a single mystery.
- **Small societies** work. AI Town and the [generative-agents](https://arxiv.org/abs/2304.03442) line get agents to coordinate, with the ceiling I describe in {{< wl "shared-channel-not-shared-world" >}}.

The gap is that nobody has these *at the same time, over one persistent world, at scale*. We can generate a world, or simulate a few dozen agents, or get one emergent storyline, but not all of it in a single shared substrate that thousands of agents and players alter together and that remembers what they did.

So "how to make it" isn't a content problem, it's a representation problem: {{< wl "what-is-a-world-state" >}} and {{< wl "action-space-as-discovery" >}} done well enough that {{< wl "world-models" >}} can carry a whole society. That's the part I think is {{< wl "phd-motivation" >}}.
