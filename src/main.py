from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, filters, MessageHandler, Application, ConversationHandler
from dotenv import load_dotenv
from commands import Start, Cancel
from messageHandler import (Name, Idade, Sexo, PesoAtual, DiasTreino)
import os
import logging
from states.States import States

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

NAME, IDADE, SEXO, PESO_ATUAL, DIAS_TREINO, ITENSIDADE_TREINO, OBJETIVO, SAUDE_CONDICAO, EXPERIENCIA_TREINO, ONDE_VAI_TREINAR, HORARIO,TIPO_ALIMENTO, ALIMENTOS_RESTRICAO, QUANTAS_REFEICOES, HORARIO_FIXO_COMER, PREPARO_COMIDA, FACIL_ACESSO_ALIMENTOS = range(17)


def main() -> None:
    load_dotenv()
    application = Application.builder().token(os.getenv('TELEGRAM_API')).build()
    start = Start.Start.start
    cancel = Cancel.Cancel.cancel
    name = Name.Name.name
    idade = Idade.Idade.idade
    sexo = Sexo.Sexo.sexo
    pesoAtual = PesoAtual.PesoAtual.pesoAtual
    diasTreino = DiasTreino.DiasTreino.diasTreino
    conversationHandler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = {
            States.getState("name"): [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            States.getState("idade"): [MessageHandler(filters.TEXT & ~filters.COMMAND, idade)],
            States.getState("sexo"): [MessageHandler(filters.TEXT & ~filters.COMMAND, sexo)],
            States.getState("peso_atual"): [MessageHandler(filters.TEXT & ~filters.COMMAND, pesoAtual)],
            States.getState("dias_treino"): [MessageHandler(filters.TEXT & ~filters.COMMAND, diasTreino)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conversationHandler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()