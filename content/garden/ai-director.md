---
title: "A director, not a script"
date: 2026-10-24
lastmod: 2026-10-24
description: "The long-term half of my thesis: an agent that intervenes on the world state to make events happen, and learns cause and effect from the difference."
status: "seedling"
notekind: "concept"
tags: ["world-models", "causality", "research-agenda"]
links: ["world-models", "stories-nobody-wrote", "what-is-a-world-state"]
---

Games have had directors for a while. The AI Director in *Left 4 Dead* decides when and where to send enemies based on how the players are doing, so the same map plays out differently every time. Genie 3's "promptable world events" are a text version of the same idea: you describe an event and the world changes.

What I want is a director for a world model. It acts on the explicit state from {{< wl "world-models" >}}: send a pedestrian across the road, block a car's path, then let the world model play out what happens next. Then run the same moment again without the intervention and compare. The difference between the two rollouts is a causal effect. A director that makes enough of these interventions is running experiments on the world, not just watching it.

That's the part I find most interesting. In a game, the director exists to make the experience better. Here, the same move, making events happen and watching the consequences, is how the model learns the causal structure of the world. A model trained only on video it can't intervene on mostly learns what tends to follow what.

It's also useful for telling stories. A director doesn't write the outcome. It sets things in motion and lets the world decide what they lead to, which is what {{< wl "stories-nobody-wrote" >}} needs.

None of this works unless the state is explicit. You can't send a pedestrian across the road if the pedestrian only exists as pixels. It also needs a way to check that the renderer actually obeys the state after an intervention, and that's where CosmosAlign already showed a gap: the text prompt was our only way to direct the scene, and when it conflicted with the history frames, the frames won.

Open questions I don't have answers to yet: what makes an intervention worth making, and how do you measure whether a world model got the causal structure right? Consistency under interventions and counterfactual rollouts are my current guesses. And what the director acts on depends on {{< wl "what-is-a-world-state" >}}.
