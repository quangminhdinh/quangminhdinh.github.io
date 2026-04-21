---
title: "World models as shared substrate"
date: 2026-03-10
lastmod: 2026-04-14
description: "Why a common representation of the world is upstream of believable multi-agent behaviour."
status: "budding"
tags: ["world-models", "research-agenda"]
links: ["multi-agent-grounding", "reachy-pilot-study"]
---

Recent work on world models can already generate photorealistic streams in which a single agent wanders freely. But *multi-agent* social interaction is still clumsy. Scripts paper over the gap; agents don't feel like they share a world.

My claim: the gap isn't in the policy, it's in the representation. If two agents don't have a common substrate describing *what is happening and what might happen next*, they can't coordinate — they can only imitate coordination.

The {{< wl "reachy-pilot-study" >}} is one concrete example of this in miniature. Even with good perception, our VLM picked generic expressions because it lacked a persistent scene model of the human it was engaging with.

Related: {{< wl "multi-agent-grounding" >}}.
