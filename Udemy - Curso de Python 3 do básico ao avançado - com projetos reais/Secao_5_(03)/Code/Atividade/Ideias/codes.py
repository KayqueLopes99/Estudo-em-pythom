"""
from abc import ABC, abstractmethod
from random import randint
from datetime import datetime
import re
from file import Arquivo_Contas, Arquivo
import os

class Conta():
  LIMITE_DO_BANCO = 2500


  def __init__(self,titular='', agencia="BancoTech", saldo_inicial=0, limite=LIMITE_DO_BANCO):
        self.numero_conta = randint(10000, 50000)
        self.titular = titular
        self.saldo = saldo_inicial
        self.agencia = agencia # deve informar !!!
        self.limite = limite
        self.limite_utilizado = False
    
    
  


  def adiciona_dados_da_conta(self, nome):
    arquivo_contas = Arquivo_Contas()
    arquivo_usuarios = Arquivo()

    # Verifica se o nome existe no arquivo de usuários
    self.titular = arquivo_usuarios.obter_nome(nome)
    if not self.titular:
        print(f"\033[91mErro: Nenhuma pessoa encontrada com o nome '{nome}'.\033[m")
        return None

    # Garante que a leitura dos dados da conta seja uma lista
    dados_contas = arquivo_contas.ler_ou_imprimir_conta() or []

    # Verifica se já existe uma conta para essa pessoa
    for conta in dados_contas:
        if conta["nome"] == self.titular:
            print(f"\033[91mErro: A conta para {self.titular} já existe com o número {conta['numero da conta']}.\033[m")
            return None

    # Cria os dados da nova conta
    dados_nova_conta = {
        "nome": self.titular,
        "numero da conta": self.numero_conta,
        "agencia": self.agencia,
        "saldo": self.saldo,
        "limite": self.limite,
    }

    # Adiciona a nova conta ao arquivo JSON
    arquivo_contas.escrever_conta([dados_nova_conta])

    print(f"\033[92mConta criada com sucesso para {self.titular}. Número da conta: {self.numero_conta}\033[m")
    return dados_nova_conta
    

    
    

 


    

# Ver o limite
class ContaCorrente(Conta):
    
    def __init__(self, agencia, saldo_inicial=0, limite=1500):
        super().__init__(agencia, saldo_inicial, limite)
    
    def sacar(self, nome, valor):
        print("Saque em Conta Corrente")
        return self.realizar_saque(nome, valor)
    
    def adicionar_limite(self, nome, valor):
       arquivo = Arquivo_Contas()
       dados = arquivo.ler_ou_imprimir_conta()

       # Verifica se o limite já foi utilizado
       if not self.limite_utilizado:
          if self.limite + valor <= self.LIMITE_DO_BANCO:
              self.limite += valor
              self.limite_utilizado = True

            # Atualiza os dados no arquivo
              for pessoa in dados:
                 if pessoa['nome'] == nome:
                    pessoa['limite'] = self.limite
                    arquivo.escrever(dados)
                    print(f"Limite adicional de {valor} adicionado à conta de {nome}. Novo limite: {self.limite}")
                    return pessoa
              print(f"Erro ao atualizar dados para o usuário {nome}.")
          else:
               print(f"Erro: O novo limite ultrapassa o limite permitido de {self.LIMITE_DO_BANCO}.")
       else:
           print(f"Limite adicional não pode ser aplicado novamente para {nome} ou conta não é Corrente.")
       return None


        

"""