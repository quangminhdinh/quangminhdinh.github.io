---
title: "The loss decides what the model ignores"
date: 2026-06-20
lastmod: 2026-06-20
description: "Two projects where the objective, not the architecture, dictated what the model paid attention to and what it left blank."
status: "seedling"
tags: ["generative-models", "training", "lesson"]
links: ["bottleneck-is-rarely-the-model", "conditioning-is-an-assumption"]
---

A model optimizes exactly what you wrote down, including the blind spots you wrote in by accident.

In [Dynamic Radiant Foam](/projects/dynamic-radiant-foam/), the model leaned on color gradients to learn temporal correspondence, so it poured its capacity into bright, high-intensity regions and left large parts of the scene blank. Nothing in the architecture said "ignore the dim areas." The L1 objective did, implicitly. Adding an SSIM term, which scores local structure rather than per-pixel intensity, made it reconstruct the whole frame uniformly and converge far faster (iteration ~500 instead of 12,000–16,000).

In [Text-Conditioned IMLE](/projects/text-conditioned-imle/), the CLIP alignment loss was a cliff, not a dial: gentle and paired with L2 it helped, but turned up it craters quality. Classifier-free guidance behaved the same way, collapsing the model entirely when its dropout rate dropped from 0.3 to 0.1.

The seedling thought: a loss is an attention-allocation policy in disguise. When a model "fails to learn" some region or some mode, my first question now is what the objective is implicitly telling it to neglect, before I blame capacity. That connects to {{< wl "bottleneck-is-rarely-the-model" >}}, and to the deeper point that every such choice is a hidden assumption about what matters: {{< wl "conditioning-is-an-assumption" >}}.
