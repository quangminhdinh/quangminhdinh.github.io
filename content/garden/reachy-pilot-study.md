---
title: "Reachy pilot study: what 38% means"
date: 2026-03-01
lastmod: 2026-10-24
description: "Participants couldn't tell our autonomous robot from a teleoperated one, but the way they guessed mattered more than the number."
status: "budding"
tags: ["hri", "reachy", "reflection"]
links: ["world-models", "ai-director"]
---

In the pilot study for our Reachy Mini interaction system (17 participants), people guessed whether the robot they had just interacted with was autonomous or teleoperated. They were right only 38% of the time (8 of 21 judgments), no better than chance. The tempting read is that the autonomous system was convincing.

The breakdown says otherwise. The autonomous robot was identified correctly 6 times out of 10, close to chance. The striking errors went the other way: 9 of the 11 people who met the teleoperated robot judged it to be autonomous.

The interesting data is in *how* participants guessed. Many of them assumed autonomous behavior would feel **more** lifelike, and that teleoperation would feel **repetitive and constrained**. That's the exact inverse of what our system produced: our autonomous VLM tended to select generic, repetitive expressions, so the lively human operator was the one taken for the machine.

The VLM recognized the action in each keyframe. What it couldn't do was *infer what the participant wanted next*, or chain behavior across turns. No persistent scene model, no anticipation.

This is the small version of {{< wl "world-models" >}}. Every response the robot picks is an intervention on the person in front of it, and picking well means predicting how they will react. That prediction needs the person's goals to be part of the state the system keeps, not something re-inferred from three keyframes. It's also the smallest possible case of {{< wl "ai-director" >}}.

In the follow-up study, the Puppet Test (30 participants), 8 of 30 people (27%) judged the autonomous robot to be human-operated, close to the 30% error rate Turing predicted for his original imitation game.
