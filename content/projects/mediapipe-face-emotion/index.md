---
title: "Face Emotion Detection with Angular Encoding"
venue: "Research exploration"
date: 2022-06-01
description: "Classifying facial emotion from the angular geometry of MediaPipe landmarks instead of raw pixels — one of my earliest research experiments."
links: "Code=https://github.com/quangminhdinh/mediapipe-face-emotion-detection"
---

A fun, early experiment — one of my first attempts at reproducing a research idea end-to-end. Instead of feeding raw pixels to a network, this project classifies facial emotion from the **angular geometry of facial landmarks** detected by **MediaPipe**, replicating the preprocessing pipeline of a 2022 emotion-recognition paper.

## The idea

Raw-pixel emotion classifiers entangle identity, lighting, and pose with expression. The alternative explored here is **geometric**: detect the face mesh with MediaPipe, then encode the **angles** between facial landmarks as features. Those angle features feed classical classifiers — **KNN**, **SVM**, and an **auto-sklearn** AutoML baseline — trained on the **FER2013** expression dataset.

The pipeline is deliberately small and legible:

- `encode.py` — the angular feature encoding
- `preprocess.py` — data preparation
- `model.py` — classifier definitions
- `run.py` — a CLI, e.g. `python run.py fit --model svm --data fer2013`

## Results

On FER2013 (48×48 images), the models reached roughly **52% (auto-sklearn), 48% (KNN), and 40% (SVM)** accuracy — below the original paper, mainly because I **omitted the super-resolution enhancement step** the authors used before landmark detection. At 48×48, MediaPipe's landmarks are noisy, and the angular encoding inherits that noise.

## Takeaways

<div class="project-takeaways">

- **Resolution matters before geometry does.** The biggest gap to the paper came from skipping super-resolution — landmark-based features are only as good as the landmarks, and tiny inputs starve them.
- **Geometric features are interpretable but brittle.** Encoding angles strips away identity and lighting nicely, yet it's far more sensitive to detector error than a pixel CNN would be.
- **Reproducing a paper teaches you where its accuracy actually comes from** — often in an unglamorous preprocessing step the abstract barely mentions.

</div>

Code and the CLI are on [GitHub](https://github.com/quangminhdinh/mediapipe-face-emotion-detection).
