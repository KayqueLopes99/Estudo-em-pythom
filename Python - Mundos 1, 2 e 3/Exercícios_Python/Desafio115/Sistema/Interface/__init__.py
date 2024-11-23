from time import sleep
from Sistema.Arquivo import *
import os
def Menu(arq):
    
    while True:
      print("-"*50)
      msg = 'Menu de opções'
      print(f"\033[94m{msg.center(50)}\033[m")
      print("-"*50)
      print("\033[95m1 - Cadastrar Usuário.\033[m")
      print("\033[95m2 - Listar Usuários Cadastrados.\033[m")
      print("\033[95m3 - Sair do Sistema.\033[m")
      print("-"*50)
      op = LeiaOpcao('Informe Uma Opção do Menu: ')
      if op == 1:
          cabeçalho_Center('Novo Cadastro de Usuário')
          nome = LeiaOpcao_Letra("Informe o Nome de Usuário: ").capitalize()
          idade = LeiaOpcao('Informe a Idade do Usuário: ')
          cadastrar_pessoas(arq, nome, idade)
      elif op == 2:
          cabeçalho_Center('Impressão dos Dados dos Usuários.')
          lerArquivo(arq)
      elif op == 3:
          cabeçalho_Center('Saindo do Sistema.')
          break
      else:
          cabeçalho_Center('Opção Invalida Senhor(a), tente novamente')
          sleep(1)
          os.system("cls")
      sleep(1)

    
    
def LeiaOpcao(mensagem):
    """ Função para ler o inteiro.

    Args:
        mensagem (_str_): A mensagem da pergunta.

    Returns:
        _int_: Numero inteiro.
    """
    while True:
        try:
            
            numero = input(mensagem)
            
            return int(numero)
        
        except ValueError:
            cabeçalho('\033[91mErro! Por favor, digite um número Inteiro válido.\033[m')
          
        except KeyboardInterrupt:
            print("\n")
            cabeçalho('\033[91mDados não informados pelo Usuário.\033[m')
            print("\n")

def LeiaOpcao_Letra(mensagem):
    while True:
        palavra_nome = input(mensagem)
        
        if palavra_nome.isalpha():  # Verifica se a entrada contém apenas letras
            return palavra_nome
        else:
            print('\033[91mErro! Por favor, digite um nome contendo apenas letras.\033[m')


def Linhas(tam=50):
    return '-' * tam

def cabeçalho(txt):
    print(Linhas())
    print(txt)
    print(Linhas())


def cabeçalho_Center(txt, tam=50):
    print(Linhas(tam))
    print(f"\033[93m{txt.center(tam)}\033[m")
    print(Linhas(tam))




    