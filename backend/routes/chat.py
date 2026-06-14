from fastapi import APIRouter
from pydantic import BaseModel

from ai_agent.citizen_assistant import process_query
from ai_agent.session_db import (
    create_session,
    get_sessions,
    get_chat_history
)


router = APIRouter()

class ChatRequest(BaseModel):
    query: str

    session_id: str


@router.post("/new-chat")
def new_chat():

    session_id = create_session()

    return {
        "session_id": session_id
    }

@router.post("/chat")
def chat(request: ChatRequest):

    response = process_query(
        request.query,
        request.session_id
    )

    return {
        "response": response
    }


@router.get("/sessions")
def sessions():

    data = get_sessions()

    return {
        "sessions": data
    }




@router.get("/history/{session_id}")
def history(
    session_id: str
):

    messages = get_chat_history(
        session_id
    )

    return {
        "messages": messages
    }