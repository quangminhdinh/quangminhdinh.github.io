---
title: "Cheap structure beats heavy machinery"
date: 2026-06-12
lastmod: 2026-06-22
description: "The simplest mechanism that clears the bar keeps winning over the impressive one that doesn't. A pattern across a startup, a challenge entry, and a rendering project."
status: "budding"
tags: ["engineering", "lesson"]
links: ["read-the-data-first"]
---

A standing temptation in ML work is to reach for the heaviest tool available. The opposite has paid off more often for me.

In [SNDA](/projects/symmetric-vehicle-retrieval/) I skipped the video transformer. Every camera in the dataset was static, so I collapsed each track into a single motion map: average the frames into a clean background, then paste the cropped vehicle from each frame back on top. Cheap structure carried most of the result, on one GPU.

In [MirrorBrain](/projects/mirrorbrain/) I replaced Qdrant vector search with Okapi BM25 on the text-retrieval path. For a note-sized corpus, lexical BM25 was faster, good enough, and it removed an entire moving part from the hot path.

In [Dynamic Radiant Foam](/projects/dynamic-radiant-foam/), every pruning scheme I tried made training worse, so I fell back to plain densification that just fills large empty cells.

The thread is not that simple is virtuous. It is that the impressive method usually buys a capability I do not yet need, at a cost I pay immediately: a transformer's data hunger, a vector DB's operational surface, pruning's instability. The boring choice clears the bar and keeps the system legible, and legibility is what lets me keep moving. It is the same observation as {{< wl "bottleneck-is-rarely-the-model" >}}, seen from the solution side. The natural precursor is to check whether the data already hands you the structure for free, which is {{< wl "read-the-data-first" >}}.
