---
title: "Why now"
date: 2026-02-01
lastmod: 2026-10-24
description: "A personal note on the path from audio processing at Huawei to wanting to spend six years on world models."
status: "evergreen"
tags: ["personal", "research-agenda"]
links: ["world-models", "conditioning-is-an-assumption", "ai-director"]
---

I didn't come into research wanting to work on world models. I came into research because, at Huawei, a problem I knew nothing about (acoustic echo cancellation on audio frames as short as 10 ms) turned out to have a beautiful fix borrowed from classical signal processing, and nobody had tried it. That was enough to convince me research was a thing I could do, and wanted to keep doing.

Then the AI City Challenge 2024 happened, and I noticed our caption model couldn't keep two agents' descriptions from conflicting. Sharing features between the two descriptions wasn't enough, because nothing in the model held one account of what happened. That pushed me toward {{< wl "world-models" >}}.

Then IMLE happened, and I learned that {{< wl "conditioning-is-an-assumption" >}}: a signal can only control what it acts on. That pushed me toward caring about how we *encode* worlds, not just generate them.

Then the Reachy Mini pilot happened. The robot couldn't anticipate the person in front of it, because their goals weren't part of anything it kept track of. That showed me the whole argument in a single Wizard-of-Oz setup.

Then CosmosAlign happened. We won the challenge and the videos looked great, but the pedestrians often did something other than what really happened, and the text prompt couldn't direct them. That's when the pieces became one claim: world models need an explicit, shared state, and something that can direct it, which is {{< wl "ai-director" >}}.

By the time I was writing the SoP, the question had stopped being *whether* to do a PhD and started being *which lab*. That's roughly when you know.
