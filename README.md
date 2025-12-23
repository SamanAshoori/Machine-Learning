# Data Mining and Machine Learning Implementations

## Overview
This repository functions as a monorepo containing source code, experiments, and visualizations for my Bachelor's degree module on Data Mining and Machine Learning.

It documents my progress in understanding the mathematical and logical foundations of standard classification and clustering algorithms.

## Project Philosophy
**Weka vs. Custom Implementation**

The official curriculum for this module utilizes the Weka workbench (Waikato Environment for Knowledge Analysis) for practical exercises. While Weka is an excellent tool for rapid prototyping and applying existing models, it abstracts away the internal logic of the algorithms.

To ensure a comprehensive understanding of the material, I am mirroring the course exercises by implementing the algorithms from scratch (primarily in Python). This approach allows me to:
1. Debug the mathematical steps (e.g., Entropy and Information Gain calculations).
2. Understand the specific limitations and edge cases of each model.

## Implemented Algorithms

### 1. ID3 (Iterative Dichotomiser 3)
A decision tree algorithm implemented to handle categorical data.
- **Key Concepts:** Entropy, Information Gain.
- **Current Status:** Implements recursive tree building. Handles discrete attributes.

