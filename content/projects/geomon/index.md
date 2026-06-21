---
title: "GeoMon"
venue: "CMPT 362 · Mobile Application Development · SFU, Fall 2025"
date: 2025-12-01
description: "A location-based, Pokémon-style Android RPG with real-time multiplayer duels and an AI monster companion."
links: "Code=https://github.com/quangminhdinh/geomon_cmpt362;Demo Site=https://quangminhdinh.github.io/geomon/;Course=https://www.sfu.ca/outlines.html?2025/fall/cmpt/362/d100"
---

**GeoMon** is a lightweight, location-based RPG for Android: players explore real-world maps, encounter monsters spawned around their GPS location, battle and capture them, duel other players in real time, and chat with their active monster powered by an LLM. It was my team's project for **CMPT 362: Mobile Application Development**, and my focus was the map, location service, spawning, capture, multiplayer, and the Firebase real-time backend.

## Demos

<div class="video-grid">
  <div class="video-embed"><iframe src="https://www.youtube.com/embed/O8q0oeOwNfc" title="GeoMon Demo 1" allowfullscreen></iframe></div>
  <div class="video-embed"><iframe src="https://www.youtube.com/embed/kmky_mS402U" title="GeoMon Demo 2" allowfullscreen></iframe></div>
</div>

There's also a downloadable [walkthrough recording](https://drive.google.com/file/d/1uIQKGibYHKj9n446kfQ_-h_WOfwIi4Z3/view?usp=sharing) on Google Drive.

<figure>
  <img src="screenshot.jpg" alt="GeoMon map screenshot">
  <figcaption>The live map: the blue marker is the player, green markers are wild monsters, red markers are other online players.</figcaption>
</figure>

## What it does

- **Location-based map.** A GPS-backed location service tracks the player and streams updates to the UI through a bound service and message handler (modelled after the classic Android "MyRuns" pattern).
- **Monster spawning.** If fewer than 10 monsters exist within a radius of the player, the system spawns new ones with random species. As you move, fresh monsters appear — and all wild monsters are **synchronised across players** through the Firebase real-time database.
- **Capture & battle.** Tap a monster to fight; the first full-HP monster in your Pokedex leads. Capture probability scales with the target's remaining HP, so you whittle it down before throwing.
- **Real-time PvP duels.** One player sends a `DuelRequest`; on accept, both devices launch the battle and share a single `BattleState` object in Firebase. Each move is applied locally first, then written to `BattleState`; the turn field flips and the opponent's listener replays the change. A heartbeat of timestamps marks players online so nearby duelists show up on the map.
- **AI companion chat.** Players talk to their active monster through the **Gemini API**, with all network calls isolated on the IO thread.

## Architecture

The app leans hard on Android's threading and persistence primitives. The UI thread owns the map, markers, and battle screens; a **Room** database caches parsed species/skill/item data so monsters can be instantiated anywhere without re-parsing JSON; and a `Monster` data class acts as the bridge between Firebase's remote representation and the local objects (mapping sprites from stored URIs along the way). Authentication uses Firebase **anonymous auth** per device, and a user object in the realtime DB holds each player's monster IDs — any monster *without* an owner ID is, by definition, a wild monster.

<figure>
  <img src="mvvm.jpg" alt="GeoMon MVVM and threading diagram">
  <figcaption>The MVVM + threading design: UI thread, IO/Room persistence, Firebase worker pools, and the location service.</figcaption>
</figure>

## Takeaways

<div class="project-takeaways">

- **Real-time multiplayer is mostly a state-synchronisation problem.** A single shared `BattleState` with listener-driven turns is far simpler to reason about than ad-hoc message passing.
- **"Optimistic local, then sync" keeps duels feeling instant** even with network latency — apply the move locally, write to Firebase, let listeners reconcile.
- **Caching reference data in Room** removes a surprising amount of friction: monsters can be spawned anywhere in the app without touching the JSON seed again.

</div>

Full source, slide decks, and video scripts are in the [GitHub repo](https://github.com/quangminhdinh/geomon_cmpt362), and the [demo site](https://quangminhdinh.github.io/geomon/) collects everything in one place.
