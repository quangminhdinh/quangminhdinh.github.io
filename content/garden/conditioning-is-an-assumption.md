---
title: "Every conditioning choice is a hidden assumption"
date: 2026-01-15
lastmod: 2026-02-25
description: "Lessons from extending IMLE to text-conditional generation: failures almost always traced to latent mismatch."
status: "evergreen"
tags: ["generative-models", "imle", "lesson"]
links: ["world-models"]
---

At APEX Lab, I spent a summer benchmarking conditioning architectures for text-to-image IMLE — FiLM affine modulation, per-block residual injection, StyleGAN-style conditioning, mapping-network concatenation. Most of them overfit.

Each failure traced back to a single thing: a mismatch in the latent representation between the condition space and the output space.

Concrete example. Unit-normalising CLIP embeddings *collapsed diversity and made overfitting worse*. On paper this is fine — cleaner conditioning should help. In practice, normalised embeddings were overwhelmed by the latent noise drawn from the prior, so the condition lost its grip on the output.

> Every architectural choice implies an assumption about *how a conditioning signal is encoded to steer what it controls*.

This generalizes beyond IMLE. Designing a shared world representation for multiple agents is the same problem scaled up: the encoding has to match the thing it's trying to steer. Back to {{< wl "world-models" >}}.
