from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class ExperienciaTreino:

    async def experienciaTreino(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Experiencia de treino do usuario: %s", update.message.text)
        context.user_data["experiencia_treino"] = update.message.text
        state = States.getState("onde_vai_treinar")
        await update.message.reply_text(
            "Você treina em academia (com acesso a máquinas, pesos livres, etc.)" 
            "ou em casa (com quais equipamentos: halteres, elásticos, peso corporal)?"
        )
        return state