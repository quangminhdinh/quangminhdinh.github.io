---
title: "Read the data before you add machinery"
date: 2026-06-15
lastmod: 2026-06-22
description: "Supervision and structure are often already in the dataset, hiding in plain sight. The second vehicle in a sentence was free labels."
status: "budding"
tags: ["research-practice", "lesson"]
links: ["the-test-distribution-is-the-only-one-that-counts"]
---

The best feature I built for [SNDA](/projects/symmetric-vehicle-retrieval/) cost nothing to collect. Many of the retrieval queries described two nearby vehicles, not one, so I mined that second vehicle's type and color as supervision the annotations were already handing me for free. Pairing `type` and `color` across the two vehicles was worth more than throwing every attribute at the model. In fact using *all* of the second vehicle's attributes hurt, because `size` and `motion` were too sparse to be reliable.

The same project had a second instance of this. Every camera was static, so the dataset quietly handed me a way to encode motion without any temporal model at all. That shortcut is also a {{< wl "cheap-structure-beats-heavy-machinery" >}} story.

What I take from this is a sequencing rule. Before designing a loss or reaching for a bigger backbone, spend real time looking at the raw data: word frequencies, what co-occurs, what the sensor setup makes constant. The structure you find there tends to beat the structure you impose, because it matches the actual distribution instead of your assumptions about it. The flip side is that quirks found this way can be split-specific, so anything you mine still has to survive {{< wl "the-test-distribution-is-the-only-one-that-counts" >}}.
