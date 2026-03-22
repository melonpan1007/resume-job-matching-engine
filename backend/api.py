from core.skills.skill_engine import extract_skills, compare_skills
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TalentMatch API running successfully"}

@app.post("/extract-skills")
def extract_skills_api(text: str):
    skills = extract_skills(text)
    return {"skills": skills}


@app.post("/compare-skills")
def compare_skills_api(resume_skills: list[str], job_skills: list[str]):
    result = compare_skills(resume_skills, job_skills)
    return result