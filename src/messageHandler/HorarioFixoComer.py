from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States

class HorarioFixoComer:

    async def horarioFixoComer(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        state = States.getState("PREPARO_COMIDA")
        context.user_data["horario_fixo_comer"] = update.message.text
        logger.info("Horarios que o usuaria faz refeição: %s", update.message.text)
        await update.message.reply_text(
            "Você prefere refeições rápidas ou tem tempo para cozinhar?"
        )
        return state

