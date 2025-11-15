from telegram import Update
from telegram.ext import ContextTypes
from logging import Logger
import logging
from states.States import States


class PesoAtual:

    async def pesoAtual(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        logger = logging.info("Peso do usuario: %s", update.message.text)
        context.user_data['peso_atual'] = update.message.text
        state = States.getState("DIAS_TREINO")
        await update.message.reply_text(
            "Quantos dias por semana você já treina?"
        )
        return state

