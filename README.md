# TalentMatch
### Resume–Job Matching & Recommendation Platform

---

# 1. Project Overview

**TalentMatch** is a production-grade Resume–Job Matching & Recommendation platform designed to analyze resumes and job descriptions, compute relevance scores, and recommend the best matches.

The system focuses on:

- Document ingestion (PDF resumes & job descriptions)
- Intelligent matching algorithms
- Skill extraction and gap analysis
- Explainable matching results
- Modular and scalable architecture

This project is designed as a **flagship system-level project** demonstrating real-world software engineering practices.

---

# 2. High-Level Architecture

```
Frontend (Web UI)
      ↓
Backend API (FastAPI)
      ↓
Core Matching Engine
      ↓
Evaluation & Results
```

All intelligence of the system is implemented inside the **core engine**.

---

# 3. Subjects Integrated in This Project

This project integrates concepts from multiple subjects in this semester.

---

## Information Retrieval (IR)

This is the **core academic concept** of the project.

Concepts used:

- Text preprocessing
- Vector representation (TF-IDF)
- Similarity computation
- Ranking algorithms
- Document retrieval

Modules responsible:

```
core/preprocessing
core/representation
core/matching
```

Example tasks:

- Resume parsing
- Job description processing
- Cosine similarity computation

---

## Full Stack Development

Full stack concepts are used to build the **user-facing application**.

Components:

Frontend
- Web UI for uploading resumes and job descriptions

Backend
- REST API using **FastAPI**
- Handles requests and returns matching results

Modules responsible:

```
frontend/
backend/api.py
backend/file_handler.py
```

---

## DevOps

DevOps concepts are used to create a **consistent development environment** and automate deployment.

Technologies used:

- Docker
- Docker Compose
- Git
- GitHub

Features implemented:

- Containerized backend
- Portable development environment
- Version control workflow

Files responsible:

```
Dockerfile
docker-compose.yml
.gitignore
```

---

## Software Testing

Testing ensures the reliability of the system.

Concepts used:

- Unit testing
- Evaluation metrics
- Functional verification

Modules responsible:

```
tests/
evaluation/evaluator.py
```

---

## Cloud Computing (Future Extension)

The system is designed so it can be deployed to the cloud easily.

Potential deployment targets:

- AWS EC2
- Azure App Services
- Google Cloud Run

Cloud architecture would include:

```
User
 ↓
Cloud Hosted API
 ↓
Matching Engine
 ↓
Cloud Storage
```

---

# 4. Quick Start (Recommended Setup)

The project runs inside Docker to ensure a consistent environment for all team members.

---

## Step 1 — Install Docker Desktop

Download from:

https://www.docker.com/products/docker-desktop/

---

## Step 2 — Clone the Repository

```bash
git clone https://github.com/melonpan1007/resume-job-matching-engine.git
cd resume-job-matching-engine
```

---

## Step 3 — Run the Project

```bash
docker compose up --build
```

---

## Step 4 — Open the API

Backend API:

```
http://localhost:8000
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

## Step 5 — Stop the Server

Press:

```
CTRL + C
```

or run:

```bash
docker compose down
```

---

# 5. Team Roles

The project is divided so each member works on separate modules.

---

## Affaan — Core Architecture

Responsible for:

- preprocessing
- similarity scoring
- explainability engine
- system integration

Modules:

```
core/preprocessing
core/matching
core/explainability
```

---

## Sayali — Representation & Evaluation

Responsible for:

- feature representation
- vectorization
- evaluation metrics

Modules:

```
core/representation
evaluation
```

---

## Vivan — Skills & Recommendation

Responsible for:

- skill extraction
- recommendation logic
- frontend/backend integration

Modules:

```
core/skills
core/recommendation
frontend
backend
```

---

# 6. Git Workflow

Each team member works on a **separate branch**.

Never push directly to `main`.

---

## Create a Branch

```bash
git checkout -b your-name-feature
```

Example:

```
git checkout -b sayali-vectorizer
```

---

## Commit Changes

```bash
git add .
git commit -m "Describe your changes"
```

---

## Push Changes

```bash
git push origin your-branch-name
```

---

## Create Pull Request

1. Go to GitHub
2. Click **Compare & Pull Request**
3. Add description
4. Merge after review

---

# 7. Development Rules

To avoid conflicts:

- No direct push to `main`
- Work only in assigned folders
- Pull latest main before starting work
- Make small commits
- Follow project structure

---

# 8. Using ChatGPT to Assist Development

Each team member can use ChatGPT to help implement their assigned module.

Before starting development, copy the entire README and paste it into ChatGPT together with the prompt below.

These prompts assume you **have not installed anything yet** and will guide you step-by-step.

---

## Prompt for Affaan (Core Architecture)

```
I am Affaan working on the TalentMatch project.

I have not installed anything or set up the project yet.

Below is the README of our project.

Please help me step-by-step to:

1. install the required tools (Git, Docker, etc.)
2. clone and run the project
3. understand the project structure
4. start implementing my modules

My role in the project is Core Architecture.

My modules are:

core/preprocessing
core/matching
core/explainability

Please guide me step-by-step and help implement these modules.
```

---

## Prompt for Sayali (Representation & Evaluation)

```
I am Sayali working on the TalentMatch project.

I have not installed anything or set up the project yet.

Below is the README of our project.

Please help me step-by-step to:

1. install the required tools (Git, Docker, etc.)
2. clone and run the project
3. understand the project structure
4. start implementing my modules

My role is Representation & Evaluation.

My modules are:

core/representation
evaluation

Please help me implement TF-IDF vectorization and evaluation metrics for resume-job matching.
```

---

## Prompt for Vivan (Skills & Recommendation)

```
I am Vivan working on the TalentMatch project.

I have not installed anything or set up the project yet.

Below is the README of our project.

Please help me step-by-step to:

1. install the required tools (Git, Docker, etc.)
2. clone and run the project
3. understand the project structure
4. start implementing my modules

My role is Skills & Recommendation.

My modules are:

core/skills
core/recommendation
frontend
backend

Please help me implement skill extraction and recommendation logic.
```

---

# 9. Project Structure

## 📁 Project Structure

```
TALENTMATCH
│
├── backend
│   ├── __pycache__
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   └── file_handler.py
│
├── core
│   ├── explainability
│   │   ├── __init__.py
│   │   └── explanation.py
│   │
│   ├── ingestion
│   │   ├── __init__.py
│   │   └── extractor.py
│   │
│   ├── matching
│   │   ├── __init__.py
│   │   └── similarity.py
│   │
│   ├── preprocessing
│   │   ├── __init__.py
│   │   └── cleaner.py
│   │
│   ├── recommendation
│   │   ├── __init__.py
│   │   └── recommender.py
│   │
│   ├── representation
│   │   ├── __init__.py
│   │   └── vectorizer.py
│   │
│   ├── skills
│   │   ├── __init__.py
│   │   └── skill_engine.py
│   │
│   └── __init__.py
│
├── docs
│
├── evaluation
│   ├── __init__.py
│   └── evaluator.py
│
├── frontend
├── scripts
├── tests
│
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

# 10. Future Extensions

Planned improvements:

- Cloud deployment
- advanced semantic embeddings
- LLM-based resume analysis
- scalable job recommendation engine