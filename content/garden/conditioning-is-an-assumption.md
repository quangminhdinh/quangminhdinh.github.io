---
title: "Every conditioning choice is a hidden assumption"
date: 2026-01-15
lastmod: 2026-10-24
description: "Lessons from extending IMLE to text-conditional generation: failures almost always traced to latent mismatch."
status: "evergreen"
tags: ["generative-models", "imle", "lesson"]
links: ["world-models"]
---

At APEX Lab, I spent a summer benchmarking conditioning architectures for text-to-image IMLE: FiLM affine modulation, per-block residual injection, StyleGAN-style conditioning, mapping-network concatenation. Most of them overfit.

Each failure traced back to a single thing: a mismatch in the latent representation between the condition space and the output space.

Concrete example. Unit-normalizing CLIP embeddings *collapsed diversity and made overfitting worse*. On paper this is fine: cleaner conditioning should help. In practice, normalized embeddings were overwhelmed by the latent noise drawn from the prior, so the condition lost its grip on the output.

> Every architectural choice implies an assumption about *how a conditioning signal is encoded to steer what it controls*.

This generalizes beyond IMLE: a signal can only control what it acts on. If we want a player, a text prompt, or a director to steer a world model, we first have to decide what in the world the signal should change. That's why, in {{< wl "world-models" >}}, controls act on an explicit state instead of competing with the pixels.
