from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class QuantasRefeicoes:

    async def quantasRefeicoes(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Quantidade de refeiçoes do usario: %s", update.message.text)
        context.user_data["quantas_refeicoes"] = update.message.text
        state = States.getState("HORARIO_FIXO_COMER")
        await update.message.reply_text(
            "Você tem horários fixos para comer ou varia muito?"
        )
        return state