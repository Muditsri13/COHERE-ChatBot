from fastapi import APIRouter
from pydantic import BaseModel
from app.services import ask_openai

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/ask")
def ask_ai(request: PromptRequest):
    response = ask_openai(request.prompt)
    return {"response": response}
