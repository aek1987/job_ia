from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import ChatRequest, CVRequest, JobRequest
from app.services.chat_service import ask_ai
from app.services.cv_service import analyze_cv
from app.services.job_service import recommend_jobs

app = FastAPI(title="Job IA Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
def chat(req: ChatRequest):
    return {"reply": ask_ai(req.message)}

@app.post("/api/analyze-cv")
def analyze(req: CVRequest):
    return analyze_cv(req.text)

@app.post("/api/recommend-jobs")
def recommend(req: JobRequest):
    return recommend_jobs(req.skills)
