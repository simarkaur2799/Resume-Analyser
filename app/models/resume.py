from pydantic import BaseModel
from typing import List, Optional

class ResumeAnalysis(BaseModel):
    name: str
    email: Optional[str]
    skills: List[str]
    raw_text: str
    experience: Optional[int] = 0

class ResumeFeedback(BaseModel):
    name: Optional[str]
    years_of_experience: Optional[int]
    key_skills: List[str]
    education: Optional[str]
    professional_experience: Optional[str]
    certifications: Optional[str]
    suggestions_for_improvement: Optional[str]

class ResumeFeedbackResponse(BaseModel):
    feedback: ResumeFeedback
