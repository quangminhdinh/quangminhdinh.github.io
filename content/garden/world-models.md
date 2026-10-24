---
title: "World models need an explicit world state"
date: 2026-03-10
lastmod: 2026-10-24
description: "My research thesis: simulate the world through an explicit, shared state that controls act on, a generative model renders, and a director can intervene on."
status: "budding"
notekind: "concept"
tags: ["world-models", "research-agenda"]
links: ["what-is-a-world-state", "conditioning-is-an-assumption", "ai-director", "reachy-pilot-study", "shared-channel-not-shared-world"]
---

Recent world models can generate photorealistic video in which a single agent wanders freely through an open world. What they don't keep is the world itself. Where things are, how they behave physically, and where each agent is trying to go only exist implicitly in the frames the model generates. The Genie 3 team calls its consistency "an emergent capability," and lists "accurately modeling complex interactions between multiple independent agents in shared environments" as an open challenge.

My claim is that the state should be explicit. A world model should keep one shared world state, holding the 3D layout and appearance of the scene, its physical properties, and the positions and goals of the agents in it, and a generative model should render that state into video. Three things follow:

- **State.** Every agent reads from and acts on the same state, so there is one account of what happened. What exactly goes into it is {{< wl "what-is-a-world-state" >}}.
- **Control.** Player inputs, text, and trajectories act on the state instead of competing with the pixels. A signal can only control what it acts on, which is the lesson from {{< wl "conditioning-is-an-assumption" >}}.
- **Direction.** Once the state is explicit, something can intervene on it and compare what happens with and without the intervention. That's the long-term goal: {{< wl "ai-director" >}}.

Multi-agent interaction isn't the headline, it's the test. It's where implicit state breaks first. The Matrix (Feng et al., 2024), a real-time world generator trained on game footage, says it directly: "In order to avoid overly complicated situations, we removed the NPCs and running vehicles in the game."

My own projects kept running into the same wall. In [CosmosAlign](https://quangminhdinh.github.io/CosmosAlign/), the generated videos stayed sharp, but the pedestrians often behaved differently from what actually happened, and whenever the history frames conflicted with the text prompt, the frames won. The model rendered the environment, not the agents, and the text, our only way to direct the scene, couldn't change that. The {{< wl "reachy-pilot-study" >}} is the same failure at desk scale, and {{< wl "shared-channel-not-shared-world" >}} is the opposite trade-off: an explicit world you can intervene on, but no physics.

A shared state on its own is no longer a new idea; several 2026 multi-agent world models keep one, mostly as latent tokens. The part I care about is a state that is physically grounded, that you can inspect, and that something can intervene on.
