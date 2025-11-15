from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class PreparoComida:

    async def preparoComida(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Preparo das refeiçoes do usario: %s", update.message.text)
        context.user_data["preparo_comida"] = update.message.text
        state = States.getState("FACIL_ACESSO_ALIMENTOS")
        await update.message.reply_text(
            "Você tem acesso fácil a todos os tipos de alimentos?"
        )
        return state