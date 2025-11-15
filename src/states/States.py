
class States:

    _STATE_MAP = {
            "NAME": 0,
            "IDADE": 1,
            "SEXO": 2,
            "PESO_ATUAL": 3,
            "DIAS_TREINO": 4,
            "INTENSIDADE_TREINO": 5,
            "OBJETIVO": 6,
            "SAUDE_CONDICAO": 7,
            "EXPERIENCIA_TREINO": 8,
            "ONDE_VAI_TREINAR": 9,
            "HORARIO": 10,
            "TIPO_ALIMENTO": 11,
            "ALIMENTOS_RESTRICAO": 12,
            "QUANTAS_REFEICOES": 13,
            "HORARIO_FIXO_COMER": 14,
            "PREPARO_COMIDA": 15,
            "FACIL_ACESSO_ALIMENTOS": 16
        }
    
    
    @classmethod
    def getState(cls, state: str) -> int:
        stateFormatted = state.upper().replace(" ", "_")
        return cls._STATE_MAP.get(stateFormatted, -1)
        


       
    