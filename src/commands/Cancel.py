from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
import logging
from logging import Logger

class Cancel:

    async def cancel(update: Update, context: ContextTypes) -> int:
        logger: Logger = logging.getLogger(__name__)
        user = update.message.from_user
        logger.info("User %s finalizou o chat.", user.first_name)
        await update.message.reply_text(
            "Tchau! Nós vemos em breve!", reply_markup = ReplyKeyboardRemove()
        )
        return ConversationHandler.END