from telegram import Update
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States

class Idade:

    async def idade(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        state = States.getState("sexo")
        idade = update.message.text
        context.user_data["idate"] = idade
        logger.info("Idade do usuário: %s", idade)
        await update.message.reply_text(
            "Agora preciso saber se você é homem ou mulher! Digita aqui para eu saber!"
        )
        return state

