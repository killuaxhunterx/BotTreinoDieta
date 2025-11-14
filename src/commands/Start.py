from telegram import Update
from telegram.ext import ContextTypes

class Start:

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        GENDER = range(1)

        await update.message.reply_text(
            "Olá, estou aqui para ajudar você a alcançar seus objetivos relacionado ao seu corpo, " \
            "montando seu treino e sua dieta! Vamos começar? Se sim, primeiramente digite o seu nome. " \
            "Caso contrário, digite /cancelar para finalizar a conversa."
        )

        return GENDER