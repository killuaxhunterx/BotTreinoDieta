from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import logging
from logging import Logger
from states.States import States

class Name:

    async def name(update: Update, context: ContextTypes) -> int:
        state = States.getState('idade')
        logger: Logger = logging.getLogger(__name__)
        logger.info("User name: %s", update.message.text)
        context.user_data["nome"] = update.message.text
        await update.message.reply_text(
            f"Prazer em te conhecer {update.message.text}! Agora preciso saber sua idade, vamos lá?",
            reply_markup=ReplyKeyboardRemove()
        )
        return state
    
