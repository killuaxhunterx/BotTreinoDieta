from telegram import Update
from telegram.ext import ContextTypes
from logging import Logger
import logging
from states.States import States


class Objetivo:

    async def objetivo(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger.info("Objetivo do usuario: %s", update.message.text)
        context.user_data["objetivo"] = update.message.text
        state = States.getState("saude_condicao")
        await update.message.reply_text(
            "Alguma condição médica pré-existente (diabetes, hipertensão, etc.) ou lesões atuais/antigas que possam limitar certos exercícios? "
            "(Lembre-se: Sou uma IA, e isso não substitui a avaliação de um médico ou nutricionista/educador físico profissional.)"        )
        return state