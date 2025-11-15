from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class Altura:

    async def altura(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Altura do usuario: %s", update.message.text)
        context.user_data["altura"] = update.message.text   
        state = States.getState("dias_treino")
        await update.message.reply_text(
            "Quantos dias por semana você já treina?"
        
        )
        return state