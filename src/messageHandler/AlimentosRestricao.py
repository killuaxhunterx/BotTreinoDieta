from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class AlimentosRestricao:

    async def alimentosRestricao(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Tipo de alimento que o usuario não come: %s", update.message.text)
        context.user_data["alimentos_restricao"] = update.message.text
        state = States.getState("QUANTAS_REFEICOES")
        await update.message.reply_text(
            "Quantas refeições você costuma fazer por dia?"
        )
        return state