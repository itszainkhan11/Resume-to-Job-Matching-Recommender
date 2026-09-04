# Resume-to-Job Matching Recommender

## Overview

Resume-to-Job Matching Recommender is an AI/ML project that recommends relevant job opportunities for a candidate based on the semantic similarity between their resume and available job descriptions.

The project uses Sentence-Transformers to convert resume and job-description text into numerical embeddings and uses cosine similarity to rank the most relevant jobs.

## Problem Statement

Traditional job matching can depend heavily on exact keyword matches. This project uses semantic embeddings so that resumes and job descriptions can be compared based on meaning rather than only identical keywords.

## Objectives

- Convert resumes into semantic embeddings.
- Convert job descriptions into semantic embeddings.
- Calculate similarity between resume and job embeddings.
- Rank jobs from most relevant to least relevant.
- Provide a simple interface for non-technical users.
- Evaluate the matching system using test resumes.
- Handle invalid and empty inputs safely.

## Technology Stack

- Python
- Sentence-Transformers
- scikit-learn
- pandas
- Streamlit

## Model

The project uses:

`all-MiniLM-L6-v2`

The model generates embeddings for resume and job-description text.

## Workflow

```text
Resume
   |
   v
Text Preprocessing
   |
   v
Sentence-Transformer
   |
   v
Resume Embedding
   |
   +-----------------------------+
   |                             |
   v                             v
Job 1 Embedding              Job N Embedding
   |                             |
   +-------------+---------------+
                 |
                 v
        Cosine Similarity
                 |
                 v
        Ranking / Top Jobs
