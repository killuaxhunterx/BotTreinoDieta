from telegram import Update
from telegram.ext import CommandHandler, filters, MessageHandler, Application, ConversationHandler
from dotenv import load_dotenv
from commands import EnviarPdf, Start, Cancel
from messageHandler import (IntensidadeTreino, Name, Idade, Sexo, PesoAtual, DiasTreino, Altura, Objetivo, 
                            SaudeCondicao, ExperienciaTreino, OndeVaiTreinar, Horario, TipoAlimento, 
                            AlimentosRestricao, QuantasRefeicoes, HorarioFixoComer, PreparoComida, 
                            FacilAcessoAlimentos)
import os
import logging
from states.States import States

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    load_dotenv()
    application = Application.builder().token(os.getenv('TELEGRAM_API')).build()
    start = Start.Start.start
    cancel = Cancel.Cancel.cancel
    name = Name.Name.name
    idade = Idade.Idade.idade
    sexo = Sexo.Sexo.sexo
    pesoAtual = PesoAtual.PesoAtual.pesoAtual
    altura = Altura.Altura.altura
    diasTreino = DiasTreino.DiasTreino.diasTreino
    intesidadeTreino = IntensidadeTreino.IntensidadeTreino.intensidadeTreino
    objetivo = Objetivo.Objetivo.objetivo
    saudeCondicao = SaudeCondicao.SaudeCondicao.saudeCondicao
    experienciaTreino = ExperienciaTreino.ExperienciaTreino.experienciaTreino
    ondeVaiTreinar = OndeVaiTreinar.OndeVaiTreinar.ondeVaiTreinar
    horario = Horario.Horario.horario
    tipoAlimento = TipoAlimento.TipoAlimento.tipoAlimento
    alimentosRestricao = AlimentosRestricao.AlimentosRestricao.alimentosRestricao
    quantasRefeicoes = QuantasRefeicoes.QuantasRefeicoes.quantasRefeicoes
    horarioFixoComer = HorarioFixoComer.HorarioFixoComer.horarioFixoComer
    preparoComida = PreparoComida.PreparoComida.preparoComida
    facilAcessoAlimentos = FacilAcessoAlimentos.FacilAcessoAlimentos.facilAcessoAlimentos
    enviarPdf = EnviarPdf.EnviarPdf.enviarPdf
    conversationHandler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = {
            States.getState("name"): [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            States.getState("idade"): [MessageHandler(filters.TEXT & ~filters.COMMAND, idade)],
            States.getState("sexo"): [MessageHandler(filters.TEXT & ~filters.COMMAND, sexo)],
            States.getState("peso_atual"): [MessageHandler(filters.TEXT & ~filters.COMMAND, pesoAtual)],
            States.getState("altura"): [MessageHandler(filters.TEXT & ~filters.COMMAND, altura)],
            States.getState("dias_treino"): [MessageHandler(filters.TEXT & ~filters.COMMAND, diasTreino)],
            States.getState("INTENSIDADE_TREINO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, intesidadeTreino)],
            States.getState("OBJETIVO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, objetivo)],
            States.getState("SAUDE_CONDICAO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, saudeCondicao)],
            States.getState("EXPERIENCIA_TREINO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, experienciaTreino)],
            States.getState("ONDE_VAI_TREINAR"): [MessageHandler(filters.TEXT & ~filters.COMMAND, ondeVaiTreinar)],
            States.getState("HORARIO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, horario)],
            States.getState("TIPO_ALIMENTO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, tipoAlimento)],
            States.getState("ALIMENTOS_RESTRICAO"): [MessageHandler(filters.TEXT & ~filters.COMMAND, alimentosRestricao)],
            States.getState("QUANTAS_REFEICOES"): [MessageHandler(filters.TEXT & ~filters.COMMAND, quantasRefeicoes)],
            States.getState("HORARIO_FIXO_COMER"): [MessageHandler(filters.TEXT & ~filters.COMMAND, horarioFixoComer)],
            States.getState("PREPARO_COMIDA"): [MessageHandler(filters.TEXT & ~filters.COMMAND, preparoComida)],
            States.getState("FACIL_ACESSO_ALIMENTOS"): [MessageHandler(filters.TEXT & ~filters.COMMAND, facilAcessoAlimentos)],
            States.getState("enviar_pdf"): [CommandHandler('gerarpdf', enviarPdf)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conversationHandler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()