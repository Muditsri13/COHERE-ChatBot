from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services import ask_cohere

router = APIRouter()

@router.post("/ask")
async def ask(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    response = ask_cohere(prompt)
    return JSONResponse(content={"response": response})
