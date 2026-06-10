from fastapi import APIRouter
from pydantic import BaseModel

from ai_agent.citizen_assistant import process_query

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):

    response = process_query(
        request.query
    )

    return {
        "response": response
    }