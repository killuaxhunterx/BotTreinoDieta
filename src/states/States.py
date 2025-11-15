
class States:

    _STATE_MAP = {
            "NAME": 1,
            "IDADE": 2,
            "SEXO": 3,
            "PESO_ATUAL": 4,
            "ALTURA": 5,
            "DIAS_TREINO": 6,
            "INTENSIDADE_TREINO": 7,
            "OBJETIVO": 8,
            "SAUDE_CONDICAO": 9,
            "EXPERIENCIA_TREINO": 10,
            "ONDE_VAI_TREINAR": 11,
            "HORARIO": 12,
            "TIPO_ALIMENTO": 13,
            "ALIMENTOS_RESTRICAO": 14,
            "QUANTAS_REFEICOES": 15,
            "HORARIO_FIXO_COMER": 16,
            "PREPARO_COMIDA": 17,
            "FACIL_ACESSO_ALIMENTOS": 18,
            "ENVIAR_PDF": 19
        }
    
    
    @classmethod
    def getState(cls, state: str) -> int:
        stateFormatted = state.upper().replace(" ", "_")
        return cls._STATE_MAP.get(stateFormatted, -1)
        


       
    