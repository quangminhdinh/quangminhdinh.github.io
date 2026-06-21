---
title: "Reachy pilot study: what 38% means"
date: 2026-03-01
lastmod: 2026-04-05
description: "Our autonomous HRI pilot fooled participants 62% of the time, but the way it failed mattered more than the number."
status: "budding"
tags: ["hri", "reachy", "reflection"]
links: ["world-models"]
---

In the pilot study for our Reachy Mini interaction system, only 38% of participants could distinguish autonomous behaviour from human teleoperation. The knee-jerk reaction is to celebrate the 62% fooling rate.

The interesting data is in *how* participants guessed. Many of them assumed autonomous behaviour would feel **more** lifelike, and that teleoperation would feel **repetitive and constrained**. The exact inverse of what our system produced: our autonomous VLM tended to select generic, repetitive expressions.

The VLM recognized the action in each keyframe. What it couldn't do was *infer what the participant wanted next*, or chain behaviour across turns. No persistent scene model, no anticipation.

This is the micro-version of the argument in {{< wl "world-models" >}}: you can't pick a good response if you don't have a shared model of the thing you're responding to.
