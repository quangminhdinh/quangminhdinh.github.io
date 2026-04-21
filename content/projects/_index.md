---
title: "Projects"
description: "Selected research and personal projects."
hidemeta: true
---

{{< project
  title="Real-Time Non-Verbal Interaction with Reachy Mini"
  venue="Rosie Lab · 2026"
  image="https://placehold.co/400x300/0a5582/fff?text=Reachy+Mini"
  links="project=https://quangminhdinh.github.io/nonverbal-reachy/"
>}}
A real-time human-to-robot interaction pipeline for Reachy Mini, combining head-and-arm mirroring, hand gesture recognition, facial emotion detection, and a locally hosted VLM that selects from 81 pre-recorded expressions via a priority scheduler. In our pilot, only 38% of participants could distinguish autonomous behaviour from human teleoperation.
{{< /project >}}

{{< project
  title="TrafficVLM"
  venue="AI City Challenge @ CVPR 2024 · 3rd place"
  image="https://placehold.co/400x300/1279aa/fff?text=TrafficVLM"
  links="paper=https://openaccess.thecvf.com/content/CVPR2024W/AICity/html/Dinh_TrafficVLM_A_Controllable_Visual_Language_Model_for_Traffic_Video_Captioning_CVPRW_2024_paper.html;code=https://github.com/quangminhdinh/TrafficVLM"
>}}
A controllable visual language model for dense, fine-grained captioning of traffic video events. Two Vid2Seq-based visual encoders model events at different levels of analysis, and a T5-Base decoder generates long descriptions for vehicle and pedestrian across traffic phases. Trained with a multi-task fine-tuning paradigm to align video and text features across phases.
{{< /project >}}

{{< project
  title="AdaIMLE (Text-Conditional)"
  venue="APEX Lab · Summer 2025"
  image="https://placehold.co/400x300/3e9dc8/fff?text=AdaIMLE"
  links="code=https://github.com/quangminhdinh/AdaIMLE"
>}}
Extended Implicit Maximum Likelihood Estimation to the text-conditional setting. Benchmarked four conditioning architectures — FiLM-style affine modulation, per-block residual injection, StyleGAN-based conditioning, and mapping-network concatenation — across Oxford 102 Flowers and CelebA Faces Captioned. Traced failures to latent-space mismatches between condition and output.
{{< /project >}}

{{< project
  title="Extended Loss"
  venue="Interspeech 2025"
  image="https://placehold.co/400x300/0a74ad/fff?text=Extended+Loss"
  links="project=https://quangminhdinh.github.io/ExtendedLoss/;paper=https://www.isca-archive.org/interspeech_2025/dinh25_interspeech.html"
>}}
A model-agnostic method that incorporates adjacent audio chunks into the loss calculation for real-time speech enhancement when frames are as short as 200ms. Yields 0.1–0.57 improvement in double-talk AECMOS echo and 5.69–24.18 ERLE gain on the AEC Challenge 2023 aligned blind set — with no inference-time cost.
{{< /project >}}

{{< project
  title="MirrorBrain"
  venue="Personal · 2023–2024"
  image="https://placehold.co/400x300/8fd3ee/333?text=MirrorBrain"
  links="code=https://github.com/quangminhdinh"
>}}
A Zettelkasten-style note-taking app augmented with LLMs for auto-generating text connections and contexts. Led a team of 5 across architecture, database, REST API, and Kanban delivery. Built with Next.js, TypeScript, Tailwind, BlockNote, FastAPI, Qdrant, and Convex. Reverse-engineered BlockNote's side-menu UI; replaced Qdrant vector search with Okapi BM25 for faster text retrieval.
{{< /project >}}

{{< project
  title="Mental Sprout"
  venue="Personal · 2022"
  image="https://placehold.co/400x300/7bbf6a/fff?text=Mental+Sprout"
  links=""
>}}
A platform connecting parents of autistic children with specialized professionals. Directed a team of 10 across architecture, Figma prototyping, and delivery. Built a web landing page + ERP dashboard in React, an Android app in React Native, and a Node.js/Express/PostgreSQL backend.
{{< /project >}}
