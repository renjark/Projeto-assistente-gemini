import os ## Operator System
import google.generativeai as genai ## Alias para a biblioteca do Gemini
from dotenv import load_dotenv ## Biblioteca para carregar variaveis de ambiente

load_dotenv()

CHAVE_API_KEY = os.getenv("GEMINI_API_KEY") ## Variável de ambiente
genai.configure(api_key=CHAVE_API_KEY) ## Configuração da API
MODELO_ESCOLHIDO = "gemini-1.5-flash" ## Modelo escolhido

promt_sistema = "Liste apenas os nomes dos produtos, e ofereça uma breve descrição de cada um"
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=promt_sistema
)

pergunta = "Listre três produtos de moda sustentável para ir ao shopping"
resposta = llm.generate_content(pergunta)

print(f"Resposta gerada: {resposta.text}")