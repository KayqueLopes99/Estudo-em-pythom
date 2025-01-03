# Exercício - sistema de perguntas e respostas com Python
import os
from time import sleep
dados_do_usuario = {}

perguntas = [
    {
        'Pergunta': 'Quais são os iniciais da Região de Kanto?',
        'Opções': [
            '(1) - Bulbasaur, Charmander e Squirtle',
            '(2) - Chikorita, Cyndaquil e Totodile',
            '(3) - Treecko, Torchic e Mudkip',
            '(4) - Turtwig, Chimchar e Piplup',
            '(5) - Snivy, Tepig e Oshawott'
        ],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual Pokémon é conhecido como o "Clone do Mew"?',
        'Opções': [
            '(1) - Celebi',
            '(2) - Jirachi',
            '(3) - Mewtwo',
            '(4) - Deoxys',
            '(5) - Ditto'
        ],
        'Resposta': 3
    },
    {
        'Pergunta': 'Qual é o tipo do Pikachu?',
        'Opções': [
            '(1) - Fogo',
            '(2) - Elétrico',
            '(3) - Água',
            '(4) - Psíquico',
            '(5) - Grama'
        ],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a evolução final de Charmander?',
        'Opções': [
            '(1) - Charmeleon',
            '(2) - Charizard',
            '(3) - Magmar',
            '(4) - Blaziken',
            '(5) - Infernape'
        ],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual Pokémon é famoso por sua habilidade de cantar e fazer os outros dormirem?',
        'Opções': [
            '(1) - Clefairy',
            '(2) - Jigglypuff',
            '(3) - Wigglytuff',
            '(4) - Meloetta',
            '(5) - Slaking'
        ],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é o nome do Pokémon lendário do tipo Fogo da 1ª geração?',
        'Opções': [
            '(1) - Entei',
            '(2) - Ho-oh',
            '(3) - Moltres',
            '(4) - Reshiram',
            '(5) - Victini'
        ],
        'Resposta': 3
    },
    {
        'Pergunta': 'Quantos ginásios existem na Liga de Kanto?',
        'Opções': [
            '(1) - 6',
            '(2) - 7',
            '(3) - 8',
            '(4) - 9',
            '(5) - 10'
        ],
        'Resposta': 3
    },
    {
        'Pergunta': 'Qual é o Pokémon nº 1 na Pokédex?',
        'Opções': [
            '(1) - Pikachu',
            '(2) - Mew',
            '(3) - Bulbasaur',
            '(4) - Charmander',
            '(5) - Eevee'
        ],
        'Resposta': 3
    },
    {
        'Pergunta': 'Quem é o rival de Ash na série original de Pokémon?',
        'Opções': [
            '(1) - Brock',
            '(2) - Misty',
            '(3) - Gary',
            '(4) - Jessie',
            '(5) - James'
        ],
        'Resposta': 3
    },
    {
        'Pergunta': 'Qual é a fraqueza do tipo Psíquico na primeira geração?',
        'Opções': [
            '(1) - Pedra e Terra',
            '(2) - Fantasma e Inseto',
            '(3) - Água e Gelo',
            '(4) - Dragão e Aço',
            '(5) - Voador e Sombrio'
        ],
        'Resposta': 2
    }
]

def funcao_de_perguntas_e_respostas():
   acertos = 0
   erros = 0
   for indice, pergunta in enumerate(perguntas):
      print(f"->Pergunta {indice + 1}:")
      print(f"\033[95m{pergunta['Pergunta']}\033[m")

      for i, opcao in enumerate(pergunta['Opções']):
         print(f"\033[93m{opcao}\033[m")
      resposta_do_usuario = input("Informe a Resposta para pergunta: ")


      if resposta_do_usuario.isdigit() and int(resposta_do_usuario) == pergunta['Resposta']:
         print("\033[92mResposta Correta!\033[m")
         acertos += 1
         
      else:
         print("\033[91mResposta Incorreta!\033[m")
         erros += 1
         
   retorno = funcao_de_centralizacao(f'O Jogador {dados_do_usuario["nome"]} Acertou {acertos} e Errou {erros} Perguntas.')
   


   
def funcao_tratamento_do_nome():
   while True:
      nome = str(input('Informe o Nome do usuário: ')).strip().capitalize()
      if not nome.replace(" ", '').isalpha():
        print("\033[91mErro! O nome deve conter apenas letras.\033[m")
      else:
        print("\033[92mNome de Usuário Cadastrado!\033[m")
        return nome
   
def cadastrar_usuario():
    nome = funcao_tratamento_do_nome()
    dados_do_usuario['nome'] = nome 
    return dados_do_usuario

def editar_nome_do_usuario():
   novo_nome = funcao_tratamento_do_nome()
   dados_do_usuario.update(nome=novo_nome)
   return dados_do_usuario

def funcao_validar_inteiro():
    while True:
      opcao_menu = input('Informe uma Opção do Menu: ')
      if not opcao_menu.isdigit():
        print("\033[91mErro! A opção deve conter apenas Números.\033[m")
      else:
        print(f"\033[92m\aOpção {opcao_menu} Selecionada.\033[m")
        return opcao_menu
      
def funcao_de_centralizacao(mensagem):
    print("-"*len(mensagem))
    print(f"\033[92m{mensagem.center(len(mensagem))}\033[m")
    print("-"*len(mensagem))

while True:
   funcao_de_centralizacao("= Sistema de Perguntas e Respostas Sobre Pokémon =")
   print("\033[94m1 - Cadastrar Nome do Usuário.\033[m")
   print("\033[95m2 - Editar Nome do Usuário.\033[m")
   print("\033[96m3 - Começar o Jogo.\033[m")
   print("\033[96m0 - Sair do Jogo.\033[m")
   print("-"*51)
   opcao = funcao_validar_inteiro()

   if opcao == "1":
      cadastrar_usuario()
   elif opcao == "2":
      if dados_do_usuario and 'nome' in dados_do_usuario:  
        editar_nome_do_usuario()
      else:  
        print("\033[91mJogador precisa de um Nome!\033[m")
   elif opcao == "3":
      if dados_do_usuario and 'nome' in dados_do_usuario:  
        funcao_de_perguntas_e_respostas()
      else:  
        print("\033[91mJogador precisa de um Nome!\033[m")
   elif opcao == "0":
      funcao_de_centralizacao("Saindo do Sistema...")
      os.system('cls')
      break
   else:
      print("\033[91mOpção fora do intervalo (0 - 3)\033[m")