---
title: "MirrorBrain"
venue: "KaleidoAI · New Venture Challenge (Ethos Fund) · 2023–2024"
date: 2024-01-15
description: "An LLM-augmented, Zettelkasten-style note-taking app. A startup attempt through the Ethos Fund New Venture Challenge, and an honest post-mortem on execution."
links: "code=https://github.com/KaleidoAI/mirror-brain-v0;system design=/projects/mirrorbrain/architecture.jpg;db schema=/projects/mirrorbrain/schema.jpg;ux design=/projects/mirrorbrain/wireframe.jpg;milestones=/projects/mirrorbrain/prototype.jpg"
---

**MirrorBrain** was an LLM-augmented, **Zettelkasten-style** note-taking app: an Obsidian-like graph of atomic notes where the model auto-generates the connections, context, and metadata between ideas. It was the flagship product of **KaleidoAI**, my startup attempt through the **[Ethos Fund](https://www.ethosfund.vc/) New Venture Challenge**. I led a team of 5, building on Next.js/TypeScript, FastAPI, Convex, and Qdrant.

It did not succeed, and the reason was **execution, not idea**. I'm keeping it here precisely because the post-mortem taught me more than a polished win would have.

## The concept

The product centered on a few interlocking ideas:

- **Notes** with an Obsidian-style structure, editable like Notion, linkable to knowledge sources, and quick to scaffold from a short description.
- **Knowledge sources** ingested from PDFs, docs, slides, websites, YouTube, and podcasts, then auto-summarized into chapter summaries, Q&A, related works, and tags.
- **A glossary** that auto-builds definitions and related concepts from terms extracted out of your notes.
- **A chat interface** that retrieves across your notes and their attached sources, behind a fast, Notion-like command bar.

It began life as a browser extension for capturing notes on the fly, then grew into a full workspace: editable block-based pages, a knowledge graph that suggests links and extrapolates context, and an AI-powered editor with continue and grammar assists. The buttons above open full-resolution versions of each design.

<figure>
  <img src="wireframe.jpg" alt="MirrorBrain UX wireframe">
  <figcaption>The UX wireframe: routing from auth, the note/source/term pages, and a Notion-style command bar wired to the API.</figcaption>
</figure>

## What I built and led

The stack was **Next.js + TypeScript + Tailwind** with **[BlockNote](https://www.blocknote.dev/)** as the editor, a **FastAPI** backend, **Convex** for real-time data, and **Qdrant** for vector search. The system fanned out into four paths: ingestion (Tavily/SerpAPI lookups plus context-aware, block-level chunk splitting), search and RAG, block-level injection back into pages, and a websocket chat scoped to a note's attached sources.

<figure>
  <img src="architecture.jpg" alt="MirrorBrain system architecture">
  <figcaption>System architecture: the ingestion, search/RAG, block-injection, and chat paths over the Next.js, FastAPI, and storage layers.</figcaption>
</figure>

The data model stayed deliberately small: pages typed as *note*, *source*, or *topic*, assembled from a linked list of blocks, with each block mirrored into Qdrant by id.

<figure>
  <img src="schema.jpg" alt="MirrorBrain database schema">
  <figcaption>The data model: pages, blocks, sources, and users in Convex, each block synced to a Qdrant payload by id.</figcaption>
</figure>

Two engineering details I'm still fond of:

- **Reverse-engineering BlockNote's side-menu UI** to bend the editor into the linked-note interactions the product needed.
- **Replacing Qdrant vector search with Okapi BM25** for the text-retrieval path: for our note-sized corpus, lexical BM25 was *faster and good enough*, and it removed an entire moving part from the hot path.

<figure>
  <img src="prototype.jpg" alt="MirrorBrain milestone roadmap">
  <figcaption>The milestone roadmap: how the extension, note structure, editor, and chat were meant to evolve from v0.1 to v0.3.</figcaption>
</figure>

## Post-mortem

<div class="project-takeaways">

- **The idea wasn't the problem; execution was.** We over-invested in product surface and architecture before pressure-testing demand and shipping cadence: the classic founder trap.
- **Sometimes the boring choice wins.** Swapping a vector DB for BM25 was a small reminder that the simplest tool that clears the bar beats the impressive one that doesn't.
- **Leading five people taught me delivery discipline** (Kanban, scoping, and saying no) more than any single technical task did.

</div>

Code for the v0 build lives in the [KaleidoAI repo](https://github.com/KaleidoAI/mirror-brain-v0).
