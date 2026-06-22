---
title: "What even is a world state?"
date: 2023-08-15
lastmod: 2026-06-22
description: "We talk about world models as if 'the state' were given. The representation is the hard part."
status: "seedling"
notekind: "concept"
tags: ["world-models", "research-agenda"]
links: ["world-models", "conditioning-is-an-assumption"]
---

Most discussion of world models treats "the world state" as a given object you read off and predict forward. I keep getting stuck one step earlier: what *is* a world state, concretely?

The open questions I can't yet answer cleanly:

- There's no uniform representation of a 3D world, and no uniform representation of its state. So which one do you commit to, and what does that choice quietly assume?
- Does the state have to be maintained in real time, or is it something you reconstruct on demand?
- Where does the data defining it even come from?

The reason this isn't just bookkeeping: the representation *is* the problem, not a detail you settle before the real work. That's the same lesson as {{< wl "conditioning-is-an-assumption" >}}, the encoding has to match the thing it's trying to steer. A "world state" you can't ground in a representation is just a word.

A seedling, deliberately. Back to {{< wl "world-models" >}}.
