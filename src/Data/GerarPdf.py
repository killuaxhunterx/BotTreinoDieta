from telegram import Update, Bot
from telegram.ext import ContextTypes
from Data import Data, Gemini, Pdf
from Data.Data import Data
from Data.Gemini import Gemini
from Data.Pdf import Pdf
from dotenv import load_dotenv
import os

class GerarPdf:

    async def gerarPdf(update: Update, context: ContextTypes) -> None:
        load_dotenv()
        data = Data()
        gemini = Gemini()
        pdf = Pdf()
        bot = Bot(os.getenv('TELEGRAM_API'))
        userDataDict = data.getDictData(update, context)
        iaContent = gemini.generateContent(userDataDict)
        pdf.gerarPdf(iaContent)
        await bot.send_message(
            chat_id=update.effective_chat.id,
            text = "Parabens! 🥳🥳🥳 Aqui esta o seu pdf com treino e dietas!"
        )