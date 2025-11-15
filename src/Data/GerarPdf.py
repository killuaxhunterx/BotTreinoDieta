from telegram import Update, Bot
from telegram.ext import ContextTypes
from Data import Data, Gemini, Pdf
from states.States import States
from dotenv import load_dotenv
import os

class GerarPdf:

    async def gerarPdf(update: Update, context: ContextTypes) -> None:
        load_dotenv()
        data = Data.Data
        gemini = Gemini.Gemini
        pdf = Pdf.Pdf
        bot = Bot(os.getenv('TELEGRAM_API'))
        userDataDict = data.getDictData(update, context)
        iaContent = gemini.generateContent(userDataDict)
        pdf.gerarPdf(iaContent)
        await bot.send_message(
            chat_id=update.effective_chat.id,
            text = "Parabens! 🥳🥳🥳 Aqui esta o seu pdf com treino e dietas!"

        )