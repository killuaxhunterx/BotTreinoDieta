from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import logging
from logging import Logger

class Name:

    async def name(update: Update, context: ContextTypes) -> None:
        logger: Logger = logging.getLogger(__name__)
        user = update.message.from_user
        logger.info("User name: %s", user.first_name)
        await update.message.reply_text(
            f"Prazer em te conhecer {user.first_name}! Agora preciso saber se você é homem ou mulher, vamos lá?",
            reply_markup=ReplyKeyboardRemove()
        )
    
