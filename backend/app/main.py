from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, chat_http, chat_ws
from app.core.config import settings

app = FastAPI(title="Immobilier Chatbot API", version="0.1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(chat_http.router, prefix="/api/chat", tags=["chat-http"])
app.include_router(chat_ws.router, prefix="/ws", tags=["chat-ws"])