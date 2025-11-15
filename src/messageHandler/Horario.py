from telegram import Update
from telegram.ext import ContextTypes
from logging import Logger
import logging
from states.States import States

class Horario:

    async def horario(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Horario em que o usuario pode treinar: %s", update.message.text)
        context.user_data["horario"] = update.message.text
        state = States.getState("tipo_alimento")
        await update.message.reply_text(
            "Você é vegetariano, vegano, onívoro, etc.?"
        )
        return state