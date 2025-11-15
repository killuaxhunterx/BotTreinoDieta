from telegram import Update
from telegram.ext import ContextTypes
from logging import Logger
import logging
from states.States import States


class IntensidadeTreino:

    async def intensidadeTreino(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Itensidade de treino do usuario: %s", update.message.text)
        context.user_data["intensidade_treino"] = update.message.text
        state = States.getState("OBJETIVO")
        await update.message.reply_text(
            "O que você deseja alcançar? (Ex: Perder gordura, ganhar massa muscular, melhorar a resistência, manter o peso)."
        )
        return state