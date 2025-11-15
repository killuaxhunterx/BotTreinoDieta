from telegram import Update
from telegram.ext import ContextTypes
from logging import Logger
import logging
from states.States import States
from Data.Data import Data


class Sexo:

    async def sexo(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Sexo do usuario: %s", update.message.text)
        state = States.getState("peso_atual")
        context.user_data['sexo'] = update.message.text
        await update.message.reply_text(
            "Perfeito! Digite agora seu peso atual: "
        )
        return state