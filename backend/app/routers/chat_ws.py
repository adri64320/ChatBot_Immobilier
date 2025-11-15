from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

from app.services.chat_service import ChatService
from app.schemas.chat import Message
from app.utils.logging_utils import get_logger

router = APIRouter()
chat_service = ChatService()
logger = get_logger(__name__)


@router.websocket("/chat/{conversation_id}")
async def chat_ws(websocket: WebSocket, conversation_id: str):
    await websocket.accept()
    logger.info(f"Client connecté au WS - conversation {conversation_id}")

    history: List[Message] = []

    try:
        while True:
            # 1) On attend le message utilisateur
            user_message = await websocket.receive_text()
            logger.info(f"[WS] message user: {user_message!r}")

            # 2) On génère la réponse
            reply_text = chat_service.generate_reply(history, user_message)
            logger.info(f"[WS] reply générée: {reply_text!r}")

            # 3) On met à jour l'historique
            history.append(Message(role="user", content=user_message))
            history.append(Message(role="assistant", content=reply_text))

            # 4) On ENVOIE la réponse au client
            await websocket.send_text(reply_text)
            logger.info("[WS] reply envoyée au client")

    except WebSocketDisconnect:
        logger.info(f"Client déconnecté du WS - conversation {conversation_id}")
    except Exception as e:
        logger.exception(f"Erreur dans chat_ws: {e}")