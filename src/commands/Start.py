from telegram import Update
from telegram.ext import ContextTypes
from states.States import States

class Start:

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        state = States.getState("NAME")

        await update.message.reply_text(
            "Olá, meu nome é Dr. Natalia, sou nutricionista e personal trainer e estou aqui para ajudar você a alcançar seus objetivos relacionado ao seu corpo, " \
            "montando seu treino e sua dieta! Vamos começar? Se sim, primeiramente digite o seu nome. " \
            "Caso contrário, digite /cancel para finalizar a conversa."
        )

        return state