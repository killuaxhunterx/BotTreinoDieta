from google import genai
from google.genai.types import GenerateContentResponse
from dotenv import load_dotenv
import json

class Gemini:

    def generateContent(content: dict[str]) -> str:
        load_dotenv()
        try:
            client = genai.Client()
            content_json = json.dumps(content, indent=2, ensure_ascii=False)
            
            prompt = (
                "Gere um plano de treino e dieta detalhado e formatado, exclusivamente com base nas informações a seguir. "
                "Coloque como cabeçalho o nome, idade, altura e peso"
                "APENAS gere o conteúdo do plano (treino e dieta), sem comentários ou introduções sobre o prompt, retire tambem * e **. "
                "Aqui estão todas as informações do usuário:\n\n"
                f"{content_json}"
            )
            response: GenerateContentResponse = client.models.generate_content(
                model = 'gemini-2.5-flash', 
                contents = prompt
            )
            return response.text
        except Exception as e:
            print(f"Error em gerar conteudo {e}")
       
