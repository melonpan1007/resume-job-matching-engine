from core.recommendation.recommender import recommend_jobs
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.skills.skill_engine import extract_skills, compare_skills
from fastapi import UploadFile, File
from backend.file_handler import extract_text_from_pdf
from core.recommendation.recommender import recommend_jobs

app = FastAPI()


@app.get("/")
def home():
    return {"message": "TalentMatch API running successfully"}


# ✅ Pydantic Models
class TextInput(BaseModel):
    text: str


class SkillCompareInput(BaseModel):
    resume_skills: list[str]
    job_skills: list[str]


# ✅ Extract Skills API

class RecommendationInput(BaseModel):
    resume_text: str
    job_texts: list[str]
    top_k: int = 5

@app.post("/extract-skills")
def extract_skills_api(data: TextInput):

    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    skills = extract_skills(data.text)
    return {"skills": skills}


# ✅ Compare Skills API
@app.post("/compare-skills")
def compare_skills_api(data: SkillCompareInput):

    if not data.resume_skills or not data.job_skills:
        raise HTTPException(status_code=400, detail="Skills list cannot be empty")

    result = compare_skills(data.resume_skills, data.job_skills)
    return result

@app.post("/recommend")
def recommend_api(data: RecommendationInput):

    if not data.resume_text or not data.job_texts:
        raise HTTPException(status_code=400, detail="Invalid input")

    result = recommend_jobs(data.resume_text, data.job_texts, data.top_k)

    return {"recommendations": result} 

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # extract text from PDF
    resume_text = extract_text_from_pdf(file)

    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Empty resume")

    # sample job descriptions (for now)
    job_texts = [
        "Looking for Python and Machine Learning engineer",
        "Backend developer with Python, SQL and FastAPI",
        "Frontend developer React JS"
    ]

    recommendations = recommend_jobs(resume_text, job_texts)

    return {
        "resume_text": resume_text[:300],  # preview
        "recommendations": recommendations
    }