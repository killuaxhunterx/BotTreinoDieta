from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States



class DiasTreino:

    async def diasTreino(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Dias de treino do usuario: %s", update.message.text)
        context.user_data["dias_treino"] = update.message.text
        state = States.getState("intensidade_treino")
        await update.message.reply_text(
             "Qual é a intensidade desses treinos (leve, moderada, intensa)?"
        )
        return state