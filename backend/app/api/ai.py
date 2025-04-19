from fastapi import APIRouter
from app.utils.openai_chat import get_ai_response

router = APIRouter()

@router.get("/{query}")
async def chat(query: str):
    response = await get_ai_response(query)
    return {"response": response}
