from telegram import Update, Bot, InputFile
from telegram.ext import ContextTypes, ConversationHandler
from dotenv import load_dotenv
import os
from Data import GerarPdf

class EnviarPdf:

    async def enviarPdf(update: Update, context: ContextTypes) -> int:
        gerarPdf = GerarPdf.GerarPdf
        await gerarPdf.gerarPdf(update, context)
        load_dotenv()
        bot = Bot(os.getenv('TELEGRAM_API'))
        path = "/home/arthur/automacaoTelegram/src/treinoDieta.pdf"
        chat_id = update.effective_chat.id
        try:
            with open(path, 'rb') as pdf:
                await bot.send_document(
                    chat_id = chat_id,
                    document = InputFile(pdf, filename="suaDietaETreino.pdf"),
                )
        except Exception as e:
            print(e)
        return ConversationHandler.END