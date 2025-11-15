from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class SaudeCondicao:

    async def saudeCondicao(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Condiçao da saude do usuario: %s", update.message.text)
        context.user_data["saude_condicao"] = update.message.text
        state = States.getState("experiencia_treino")
        await update.message.reply_text(
            "É iniciante, intermediário ou avançado na musculação/treinamento?"
        )
        return state