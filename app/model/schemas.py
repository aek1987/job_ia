from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str

class CVRequest(BaseModel):
    text: str

class JobRequest(BaseModel):
    skills: List[str]
