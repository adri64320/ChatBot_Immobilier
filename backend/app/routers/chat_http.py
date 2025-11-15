from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse, Message
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post("/", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    reply_text = chat_service.generate_reply(req.history, req.new_message)

    all_messages = req.history + [
        Message(role="user", content=req.new_message),
        Message(role="assistant", content=reply_text),
    ]

    return ChatResponse( 
        conversation_id=req.conversation_id,
        messages=all_messages,
    )