from typing import List
from app.schemas.chat import Message
from app.utils.logging_utils import get_logger

logger = get_logger(__name__)


class ChatService:
    def generate_reply(self, history: List[Message], new_message: str) -> str:
        logger.info(f"Nouveau message utilisateur: {new_message!r}")

        msg = new_message.lower()

        # Exemple ultra simplifié de règles "immobilier"
        if "paris" in msg:
            return (
                "Pour Paris, les loyers sont élevés mais la demande est forte. "
                "Tu peux viser des T2 autour de 1100-1400 €/mois selon le quartier."
            )

        if "lyon" in msg:
            return (
                "Lyon est intéressante pour l'investissement locatif, "
                "surtout autour de Part-Dieu, Confluence, Villeurbanne."
            )

        if "investissement" in msg or "rentabilité" in msg:
            return (
                "Pour évaluer un investissement, on regarde rendement brut/net, "
                "vacance locative, charges et fiscalité (LMNP, régime réel, etc.)."
            )

        return (
            "Je suis un chatbot immobilier de démo. Tu peux me demander : "
            "\"Je cherche un T2 à Paris\", "
            "\"Quels quartiers pour investir à Lyon ?\", "
            "\"Comment calculer la rentabilité locative ?\""
        )