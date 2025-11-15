from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States


class TipoAlimento:

    async def tipoAlimento(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Tipo de alimento que o usuario come: %s", update.message.text)
        context.user_data["tipo_alimento"] = update.message.text
        state = States.getState("alimentos_restricao")
        await update.message.reply_text(
            "Há alimentos que você não come por preferência ou alergia/intolerância (ex: glúten, lactose, frutos do mar)?"
        )
        return state