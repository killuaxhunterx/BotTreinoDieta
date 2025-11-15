from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class OndeVaiTreinar:

    async def ondeVaiTreinar(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Local onde o usuario vai treinar: %s", update.message.text)
        context.user_data["onde_vai_treinar"] = update.message.text
        state = States.getState("horario")
        await update.message.reply_text(
            "Quais são os 5 dias da semana que você gostaria de treinar e em que horário (manhã, tarde, noite)?"
        )
        return state