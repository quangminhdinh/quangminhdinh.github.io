---
title: "Projects"
description: "Selected research, course, and personal projects. Click a title to read the full write-up. For peer-reviewed work, see [publications](/publications/)."
hidemeta: true
---

{{< project
  title="GeoMon"
  venue="CMPT 362 · Mobile Application Development · Fall 2025"
  image="/images/projects/geomon.jpg"
  page="/projects/geomon/"
  links="website=https://quangminhdinh.github.io/geomon/;code=https://github.com/quangminhdinh/geomon_cmpt362;apk=https://drive.google.com/file/d/1uIQKGibYHKj9n446kfQ_-h_WOfwIi4Z3/view?usp=sharing;slide=/projects/geomon/final-presentation.pdf;demo 1=https://www.youtube.com/watch?v=O8q0oeOwNfc;demo 2=https://www.youtube.com/watch?v=kmky_mS402U;presentation=https://www.youtube.com/watch?v=0FHlLX5ixUo"
>}}
A location-based, Pokémon-style Android RPG: explore real-world maps, battle and capture GPS-spawned monsters, duel other players in real time, and chat with your monster via the Gemini API. I built the map, location service, spawning, capture, and the Firebase real-time multiplayer backend.
{{< /project >}}

{{< project
  title="Text-Conditioned IMLE"
  venue="APEX Lab · SFU · Summer 2025"
  image="/images/projects/text-conditioned-imle.jpg"
  page="/projects/text-conditioned-imle/"
  links="code=https://github.com/quangminhdinh/AdaIMLE;W&B=https://wandb.ai/quangminhdinh/AdaptiveIMLE?nw=nwuserquangminhdinh"
>}}
Extending Adaptive IMLE to **text-to-image** generation. Across 100+ runs on Flowers, CelebA, and ImageNet, I benchmarked conditioning architectures (FiLM, conditional StyleGAN, concatenation), CLIP/L2 losses, and text representations, and made the IMLE matching cheap with **FAISS** + fused distances. The recurring obstacle was diversity collapse under conditioning; the strongest fix was initialising from a strong unconditional prior.
{{< /project >}}

{{< project
  title="Dynamic Radiant Foam"
  venue="CMPT 469 · Rendering & Visual Computing for AI · Spring 2025"
  image="/images/projects/dynamic-radiant-foam.jpg"
  page="/projects/dynamic-radiant-foam/"
  links="code=https://github.com/quangminhdinh/CMPT469-Final;slide=/projects/dynamic-radiant-foam/slides.pdf;report=/projects/dynamic-radiant-foam/report.pdf"
>}}
An ambitious attempt to extend **Radiant Foam**, a real-time Voronoi ray-tracing radiance field, from static to *dynamic* scenes. I modelled per-point temporal density, polynomial motion, and 4D spherical harmonics, and tamed training instability with frame-time noise and an SSIM loss (≈30× faster convergence). It didn't fully succeed, but the failure modes were the lesson.
{{< /project >}}

{{< project
  title="PedroVerse"
  venue="CMPT 461 · Computational Photography · Spring 2025"
  image="/images/projects/pedroverse.jpg"
  page="/projects/pedroverse/"
  links="code=https://github.com/quangminhdinh/pedroverse"
>}}
A **Blender add-on** that stylizes 3D assets into non-photorealistic looks by editing only their albedo and object-space normal maps, with no engine-specific shaders. Combines lightweight style transfer, palette recoloring, and four geometric-abstraction filters in a modular UV-space pipeline that travels across engines and VR.
{{< /project >}}

{{< project
  title="MirrorBrain"
  venue="KaleidoAI · New Venture Challenge (Ethos Fund) · 2023–2024"
  image="/images/projects/mirrorbrain.jpg"
  page="/projects/mirrorbrain/"
  links="code=https://github.com/KaleidoAI/mirror-brain-v0;system design=/projects/mirrorbrain/architecture.jpg;db schema=/projects/mirrorbrain/schema.jpg;ux design=/projects/mirrorbrain/wireframe.jpg;milestones=/projects/mirrorbrain/prototype.jpg"
>}}
An LLM-augmented, Zettelkasten-style note-taking app, and the flagship of my startup attempt through the Ethos Fund New Venture Challenge. I led a team of 5, building on Next.js/TypeScript, FastAPI, Convex, and Qdrant. A failed venture (*execution, not idea*) and the post-mortem that taught me the most.
{{< /project >}}

{{< project
  title="Symmetric Network with Dual-vehicle Attributes Augmentation"
  venue="7th AI City Challenge @ CVPR 2023 · Track 2 · 7th place"
  image="/images/projects/symmetric-vehicle-retrieval.jpg"
  page="/projects/symmetric-vehicle-retrieval/"
  links="code=https://github.com/quangminhdinh/Dual-Vehicle-Aug-Symmetric-Net"
>}}
My first large-scale solo research project: natural-language tracked-vehicle retrieval. A symmetric cross-modal network (RoBERTa + EfficientNet, InfoNCE) with a **dual-vehicle attribute-augmentation** system that mines a second vehicle in each query as free supervision. 35.44% MRR, 7th place, and an early, hard lesson in the validation/test domain gap.
{{< /project >}}

{{< project
  title="Face Emotion Detection with Angular Encoding"
  venue="Research exploration · 2022"
  image="/images/projects/mediapipe-face-emotion.jpg"
  page="/projects/mediapipe-face-emotion/"
  links="code=https://github.com/quangminhdinh/mediapipe-face-emotion-detection"
>}}
One of my earliest research experiments: classifying facial emotion from the **angular geometry** of MediaPipe landmarks rather than raw pixels, with KNN/SVM/AutoML classifiers on FER2013. A reproduction study whose accuracy gap traced back to a single skipped super-resolution step.
{{< /project >}}

{{< project
  title="Virtual Ring Try-On"
  venue="YITEC · Machine Learning Engineer · 2020–2021"
  image="/images/projects/virtual-ring-tryon.jpg"
  page="/projects/virtual-ring-tryon/"
  links="demo=https://www.youtube.com/watch?v=fMoTa7qCFho;code=https://github.com/quangminhdinh/Virtual-Ring-TryOn"
>}}
Vietnam's first real-time hand-tracking AR ring try-on mobile app, built with MediaPipe, Unity AR Foundation, and ARCore. Derived the placement/lighting maths and pushed the frame rate from 5 to 30 FPS. On par with or better than FPT and Viettel at the time, and the foundation for one of YITEC's later core businesses.
{{< /project >}}
