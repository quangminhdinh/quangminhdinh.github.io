---
title: "Build on the representation that already travels"
date: 2026-06-18
lastmod: 2026-06-22
description: "PedroVerse stylized 3D assets by editing only their UV maps, because UV maps render everywhere. Choosing the substrate that is already universal buys portability for free."
status: "budding"
tags: ["engineering", "reflection"]
links: ["world-models", "read-the-data-first"]
---

[PedroVerse](/projects/pedroverse/) stylized hyper-realistic 3D assets into non-photorealistic looks without writing a single engine-specific shader. The trick was to operate only on the asset's UV maps, the albedo and object-space normal maps that almost every asset already ships with and that render cheaply on every engine and in VR. A shader built in Blender does not export; a post-process effect does not generalize; but a restyled UV map travels anywhere.

The decision that mattered was not an algorithm, it was choosing the representation that was already universal and defining every operation in that space. Portability then came for free, because the substrate was shared to begin with.

That choice has a sharp edge, though. The normal map encodes physics: shift its colors carelessly and you change the direction light bounces, so stylizing it without breaking lighting forced most of the real engineering (gradient-aware brush strokes, low SLIC compactness, a UV-space mask). Editing a representation that encodes how the world behaves is harder than editing one that only encodes how it looks.

I keep coming back to this when I think about {{< wl "world-models" >}}: a representation many agents can share is worth more than a cleverer one only you can read, and the universal one is often already sitting in the data, the engineering cousin of {{< wl "read-the-data-first" >}}.
