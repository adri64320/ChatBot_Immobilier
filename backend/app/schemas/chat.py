from pydantic import BaseModel
from typing import List, Literal

Role = Literal["user", "assistant"]


class Message(BaseModel):
    role: Role
    content: str


class ChatRequest(BaseModel):
    conversation_id: str
    new_message: str
    history: List[Message] = []


class ChatResponse(BaseModel):
    conversation_id: str
    messages: List[Message]