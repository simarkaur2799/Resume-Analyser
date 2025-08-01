from fastapi import FastAPI, APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
import io
import asyncio
from concurrent.futures import ThreadPoolExecutor
from app.services.resume_parser import extract_text_from_file
from app.services.ai_feedback import get_resume_feedback
from app.services.keyword_matcher import match_keywords


app = FastAPI()
router = APIRouter()
executor = ThreadPoolExecutor(max_workers=3)

class ResumeFeedbackResponse(BaseModel):
    feedback: str
    keyword_match: dict | None = None

@router.post("/resume-feedback/", response_model=ResumeFeedbackResponse)
async def resume_feedback(
    file: UploadFile = File(...),
    job_description: str = Form(None)
):
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword",
        "application/octet-stream"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {file.content_type}")

    file_bytes = await file.read()
    resume_text = extract_text_from_file(file.filename, io.BytesIO(file_bytes))

    loop = asyncio.get_event_loop()
    feedback = await loop.run_in_executor(executor, get_resume_feedback, resume_text)

    result = {"feedback": feedback}

    if job_description:
        keyword_matcher = match_keywords(resume_text, job_description)
        result["keyword_match"] = keyword_matcher

    return result

app.include_router(router)
