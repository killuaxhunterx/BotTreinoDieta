from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States

class FacilAcessoAlimentos:

    async def facilAcessoAlimentos(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        state = States.getState("enviar_pdf")
        context.user_data["facil_acesso_alimentos"] = update.message.text
        logger.info("Horarios que o usuaria faz refeição: %s", update.message.text)
        await update.message.reply_text(
            "Digite ou clique em /gerarpdf para gerar o seu pdf com as suas dietas e treinos! Falta pouco!😁😁"
        )
        return state

