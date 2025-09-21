# -*- coding: utf-8 -*-
"""
Imersão Agentes de IA - Aula 01
Projeto: Triador de Service Desk para políticas internas da empresa Carraro Desenvolvimento

Bibliotecas utilizadas:
- langchain
- langchain-google-genai
- google-generativeai
- pydantic
- python-dotenv (para carregar a chave da API a partir de um arquivo .env)

Para instalar todas as dependências, execute no terminal:

pip install langchain langchain-google-genai google-generativeai pydantic python-dotenv
"""

# =============================================
# 1. Importações e configuração da API Key
# =============================================

# Biblioteca para acessar o modelo da :contentReference[oaicite:0]{index=0} com :contentReference[oaicite:1]{index=1}
from langchain_google_genai import ChatGoogleGenerativeAI

# Bibliotecas para carregar variáveis do arquivo .env
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env (onde está a GEMINI_API_KEY)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")  # Lê a variável de ambiente

# =============================================
# 2. Teste simples da conexão com o modelo
# =============================================

# Cria uma instância do modelo generativo do :contentReference[oaicite:2]{index=2}
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Modelo usado
    temperature=0.0,           # Respostas determinísticas
    api_key=GOOGLE_API_KEY
)

# Faz um teste para verificar se a conexão funciona
resp_test = llm.invoke("Quem é você? Seja criativo.")
# .invoke() envia uma mensagem para o modelo e retorna a resposta
print(resp_test.content)  # Exibe a resposta do modelo no terminal


# =============================================
# 3. Prompt do sistema para triagem
# =============================================

# Este prompt instrui o modelo a agir como um triador de Service Desk
TRIAGEM_PROMPT = """
Você é um triador de Service Desk para políticas internas da empresa Carraro Desenvolvimento.
Dada a mensagem do usuário, retorne SOMENTE um JSON com:
{
  "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_CHAMADO",
  "urgencia": "BAIXA" | "MEDIA" | "ALTA",
  "campos_faltantes": ["..."]
}

Regras:
- **AUTO_RESOLVER**: Perguntas claras sobre regras ou procedimentos descritos nas políticas
  (Ex: "Posso reembolsar a internet do meu home office?", "Como funciona a política de alimentação em viagens?").

- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto
  (Ex: "Preciso de ajuda com uma política", "Tenho uma dúvida geral").

- **ABRIR_CHAMADO**: Pedidos de exceção, liberação, aprovação ou acesso especial, ou quando o usuário explicitamente pede para abrir um chamado
  (Ex: "Quero exceção para trabalhar 5 dias remoto.", "Solicito liberação para anexos externos.", "Por favor, abra um chamado para o RH.").

Analise a mensagem e decida a ação mais apropriada.
"""

# =============================================
# 4. Definição do modelo de saída com Pydantic
# =============================================

from pydantic import BaseModel, Field
from typing import Literal, List, Dict

# Define o formato estruturado que o modelo deve retornar
class TriagemOut(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"]
    campos_faltantes: List[str] = Field(default_factory=list)

# =============================================
# 5. Criação do modelo LLM para triagem
# =============================================

from langchain_core.messages import SystemMessage, HumanMessage

# Instância específica do modelo para triagem
llm_triagem = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.0,
    api_key=GOOGLE_API_KEY
)

# Configura o modelo para gerar saída estruturada com base no TriagemOut
triagem_chain = llm_triagem.with_structured_output(TriagemOut)
# .with_structured_output() força o modelo a responder respeitando o formato da classe TriagemOut

# =============================================
# 6. Função principal de triagem
# =============================================

def executarTriagem(mensagem: str) -> Dict:
    """
    Executa a triagem de uma mensagem de usuário.

    Parâmetros:
        mensagem (str): texto da mensagem do usuário.

    Retorna:
        dict: dicionário com as chaves 'decisao', 'urgencia' e 'campos_faltantes'.
    """
    saida: TriagemOut = triagem_chain.invoke([
        SystemMessage(content=TRIAGEM_PROMPT),
        HumanMessage(content=mensagem)
    ])
    # .invoke() aqui envia duas mensagens para o modelo:
    # - SystemMessage: define o "papel" e as regras do modelo (como se fosse o manual de instruções)
    # - HumanMessage: contém a mensagem real do usuário que queremos classificar
    # A resposta já vem validada no formato da classe TriagemOut

    return saida.model_dump()
    # .model_dump() converte o objeto TriagemOut para um dicionário Python (dict)





# =============================================
# 7. Testes da função de triagem
# =============================================

# Lista de mensagens de teste
testes = [
    "Posso reembolsar a internet?",
    "Quero mais 5 dias de trabalho remoto. Como faço?",
    "Posso reembolsar cursos ou treinamentos da Alura?",
    "Quantas capivaras tem no Rio Pinheiros?"
]

# Executa os testes e exibe os resultados
for msg_teste in testes:
    print(f"Pergunta: {msg_teste}\n -> Resposta: {executarTriagem(msg_teste)}\n")

## Objetivo:
# Usar a IA do Gemini para triagem automática de mensagens de usuários no Service Desk.
# Ela lê a mensagem, segue as instruções do prompt e classifica em AUTO_RESOLVER, PEDIR_INFO ou ABRIR_CHAMADO, indicando também a urgência e se faltam informações.

# O código automatiza.