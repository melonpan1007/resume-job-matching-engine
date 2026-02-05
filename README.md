
# TalentMatch  
### Resume–Job Matching & Recommendation Platform

---

## 1. Project Overview

**TalentMatch** is a production-grade Resume–Job Matching & Recommendation platform designed to analyze resumes and job descriptions, compute relevance scores, and recommend the best matches.

The system focuses on:
- Real-world document ingestion (PDF resumes & JDs)
- Intelligent matching using multiple strategies
- Explainability (why a match happened)
- Modular, scalable architecture

This project is designed as a **flagship, market-ready system**, not just an academic prototype.

---

## 2. Key Features

- Upload resumes and job descriptions (PDF / DOCX / TXT)
- Robust text extraction and preprocessing
- Multiple matching strategies (similarity + skills)
- Skill gap analysis
- Resume → Job and Job → Resume recommendations
- Explainable matching results
- Clean UI with backend APIs
- Production-style Git workflow, testing, and CI readiness

---

## 3. High-Level Architecture

```
Frontend (Web UI)
   ↓
Backend API (HTTP / REST)
   ↓
Core Matching Engine (Python)
   ↓
Evaluation, Logs & Results
```

**Design Principle:**  
All intelligence lives inside the `core/` engine.  
UI and backend only call interfaces — they never re-implement logic.

---

## 4. Repository Structure

```
talentmatch/
├── frontend/
├── backend/
│   ├── api.py
│   ├── file_handler.py
│   └── config.py
├── core/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── representation/
│   ├── matching/
│   ├── skills/
│   ├── recommendation/
│   └── explainability/
├── evaluation/
├── tests/
├── scripts/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 5. Team Roles & Work Division

Each member owns **core logic**, not just surface-level tasks.

### Affaan — Core Architecture & Matching
- Text preprocessing
- Similarity & ranking logic
- Explainability engine
- Overall architecture & integration

### Sayali — Representation & Evaluation
- Feature representation (TF-IDF / vector models)
- Matching strategy comparison
- Evaluation metrics & analysis

### Vivan — Skills, Recommendation & UI
- Skill extraction & gap analysis
- Recommendation logic
- Frontend & backend integration

All changes go through **Pull Requests**.

---

## 6. Technologies Used

### Core Engine
- Python
- scikit-learn
- NLTK / spaCy

### Backend
- FastAPI / Flask
- Python

### Frontend
- Streamlit / React / HTML-CSS-JS

### DevOps & Quality
- Git & GitHub
- GitHub Actions
- pytest
- Shell scripting

---

## 7. Git Setup & Collaboration Guide

### 7.1 Install Git (Windows)

1. Download **Git for Windows**
2. During installation:
   - Default editor: **Visual Studio Code**
   - PATH option: **Git from the command line and 3rd-party software**
3. Complete installation

Verify installation:
```bash
git --version
```

---

### 7.2 Configure Git Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global --list
```

---

### 7.3 Clone Repository

```bash
git clone https://github.com/melonpan1007/resume-job-matching-engine.git
cd resume-job-matching-engine
```

---

### 7.4 Branching (Always Use Your Own Branch)

```bash
git checkout -b your-name-feature
```

Example:
```bash
git checkout -b sayali-preprocessing
```

---

### 7.5 Assigned Work Areas

- **Affaan**
  - `core/preprocessing/`
  - `core/matching/`
  - `core/explainability/`

- **Sayali**
  - `core/representation/`
  - `evaluation/`

- **Vivan**
  - `core/skills/`
  - `core/recommendation/`
  - `frontend/`
  - `backend/`

Do not modify files outside your assigned folders.

---

### 7.6 Commit & Push Changes

```bash
git add .
git commit -m "Clear and meaningful commit message"
git push -u origin your-branch-name
```

---

### 7.7 Pull Requests

1. Open Pull Request on GitHub
2. Add short description
3. Request review
4. Merge into `main` only after approval

---

### 7.8 Sync with Main Branch

```bash
git checkout main
git pull origin main
git checkout your-branch-name
```

---

## 8. Development Rules (Strict)

- No direct push to `main`
- Work only in assigned folders
- All logic must be inside `core/`
- UI and backend must call core interfaces
- Small, meaningful commits only

---

## 9. Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Git
- VS Code

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Project (Example)
```bash
python backend/api.py
```

---

## 10. Future Extensions (Out of Scope)

- Advanced semantic embeddings
- LLM-based parsing
- Full cloud deployment
- Authentication & role management
```

