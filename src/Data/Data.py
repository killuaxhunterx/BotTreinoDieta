from telegram import Update
from telegram.ext import ContextTypes

class Data:

    def getDictData(update: Update, context: ContextTypes) -> dict[str]:
        data = {
            "name": context.user_data.get("name"),
            "idade": context.user_data.get("idade"),
            "sexo": context.user_data.get("sexo"),
            "peso_atual": context.user_data.get("peso_atual"),
            "altura": context.user_data.get("altura"),
            "dias_treino": context.user_data.get("dias_treino"),
            "intensidade_treino": context.user_data.get("intensidade_treino"),
            "objetivo": context.user_data.get("objetivo"),
            "saude_condicao": context.user_data.get("saude_condicao"),
            "experiencia_treino": context.user_data.get("experiencia_treino"),
            "onde_vai_treinar": context.user_data.get("onde_vai_treinar"),
            "horario_treino": context.user_data.get("horario"),
            "tipo_alimento": context.user_data.get("tipo_alimento"),
            "alimentos_restricao": context.user_data.get("alimentos_restricao"),
            "quantas_refeicoes": context.user_data.get("quantas_refeicoes"),
            "horario_fixo_comer": context.user_data.get("horario_fixo_comer"),
            "preparo_comida": context.user_data.get("preparo_comida"),
            "facil_acesso_alimentos": context.user_data.get("facil_acesso_alimentos")
        }

        return data


    
        