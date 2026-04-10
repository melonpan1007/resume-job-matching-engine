from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.skills.skill_engine import extract_skills, compare_skills
from core.recommendation.recommender import recommend_jobs
from backend.file_handler import extract_text_from_pdf

app = FastAPI()


# ------------------------------
# 🔥 CORS
# ------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------
# ROOT
# ------------------------------
@app.get("/")
def home():
    return {"message": "TalentMatch API running successfully"}


# ------------------------------
# MODELS
# ------------------------------
class TextInput(BaseModel):
    text: str


class SkillCompareInput(BaseModel):
    resume_skills: list[str]
    job_skills: list[str]


class RecommendationInput(BaseModel):
    resume_text: str


# ------------------------------
# SKILL EXTRACTION
# ------------------------------
@app.post("/extract-skills")
def extract_skills_api(data: TextInput):

    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Empty text")

    return {"skills": extract_skills(data.text)}


# ------------------------------
# SKILL COMPARISON
# ------------------------------
@app.post("/compare-skills")
def compare_skills_api(data: SkillCompareInput):

    if not data.resume_skills or not data.job_skills:
        raise HTTPException(status_code=400, detail="Invalid input")

    return compare_skills(data.resume_skills, data.job_skills)


# ------------------------------
# TEXT RECOMMENDATION
# ------------------------------
@app.post("/recommend")
def recommend_api(data: RecommendationInput):

    if not data.resume_text:
        raise HTTPException(status_code=400, detail="Invalid input")

    result = recommend_jobs(data.resume_text)

    return {
        "overall_score": result["overall_score"],
        "recommendations": result["recommendations"]
    }


# ------------------------------
# PDF UPLOAD
# ------------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:
        resume_text = extract_text_from_pdf(file)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Empty resume")

        result = recommend_jobs(resume_text)

        return {
            "resume_preview": resume_text[:300],
            "overall_score": result["overall_score"],
            "recommendations": result["recommendations"]
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))