from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.skills.skill_engine import extract_skills, compare_skills
from core.recommendation.recommender import recommend_jobs
from backend.file_handler import extract_text_from_pdf
from core.ingestion.job_loader import load_jobs

app = FastAPI()


# ------------------------------
# 🔥 CORS (VERY IMPORTANT)
# ------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------
# Root API
# ------------------------------
@app.get("/")
def home():
    return {"message": "TalentMatch API running successfully"}


# ------------------------------
# Request Models
# ------------------------------
class TextInput(BaseModel):
    text: str


class SkillCompareInput(BaseModel):
    resume_skills: list[str]
    job_skills: list[str]


class RecommendationInput(BaseModel):
    resume_text: str
    job_texts: list[str]
    top_k: int = 5


# ------------------------------
# Extract Skills
# ------------------------------
@app.post("/extract-skills")
def extract_skills_api(data: TextInput):

    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    skills = extract_skills(data.text)
    return {"skills": skills}


# ------------------------------
# Compare Skills
# ------------------------------
@app.post("/compare-skills")
def compare_skills_api(data: SkillCompareInput):

    if not data.resume_skills or not data.job_skills:
        raise HTTPException(status_code=400, detail="Skills list cannot be empty")

    result = compare_skills(data.resume_skills, data.job_skills)
    return result


# ------------------------------
# Recommendation API (TEXT)
# ------------------------------
@app.post("/recommend")
def recommend_api(data: RecommendationInput):

    if not data.resume_text or not data.job_texts:
        raise HTTPException(status_code=400, detail="Invalid input")

    result = recommend_jobs(
        data.resume_text,
        data.job_texts,
        data.top_k
    )

    return {"recommendations": result}


# ------------------------------
# Resume Upload API (PDF)
# ------------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:
        resume_text = extract_text_from_pdf(file)

        if not resume_text or not resume_text.strip():
            raise HTTPException(status_code=400, detail="Empty or unreadable resume")

        # 🔥 FIXED CALL
        recommendations = recommend_jobs(resume_text)

        return {
            "resume_preview": resume_text[:300],
            "recommendations": recommendations
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))