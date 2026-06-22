---
title: "Shared state is a tiny world model"
date: 2026-06-21
lastmod: 2026-06-21
description: "A multiplayer game restated my research agenda in miniature: two agents can only coordinate when they agree on one authoritative model of the world."
status: "seedling"
tags: ["world-models", "engineering", "reflection"]
links: ["world-models", "multi-agent-grounding"]
---

I did not expect a course project on mobile development to restate my research agenda, but [GeoMon](/projects/geomon/) did. The hardest part of the game was the real-time PvP duels: getting two phones to agree on whose turn it was and what had happened, without the turn order ever desyncing. The fix was a single authoritative `BattleState` in Firebase, applied optimistically on each device and reconciled through listeners. Ad-hoc message passing between the two clients never held together; a shared source of truth did.

That is the {{< wl "world-models" >}} thesis in miniature. Two agents cannot coordinate on what they do not jointly represent. In a turn-based game the shared state is small and discrete, so the engineering is tractable. For social agents the shared state is rich, continuous, and partly about each other's intentions, which is exactly why {{< wl "multi-agent-grounding" >}} is hard: the substrate they would need to agree on does not fit in a `BattleState` object.

What stays with me is that the failure mode is identical at both scales. When two clients disagree, you get desync. When two agents lack a common model, you get behavior that only imitates coordination. The open question I like is what the `BattleState` has to become once the world stops being a game.
