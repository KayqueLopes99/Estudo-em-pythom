from datetime import datetime
import re
import os
from random import randint
from time import sleep
from valida import valid_number, valid_option, Validar

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[m")
    sleep(0.3)
    print("\033[38;5;136m===== Menu de Opções =====\033[m")
    sleep(0.3)
    print("\033[38;5;21m[1] - Cadastramento.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[2] - Mostrar Informações da Conta.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[3] - Sacar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[4] - Depositar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[5] - Extrato.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[6] - Sair do Sistema Bancário.\033[m")
    sleep(0.3)
    print("-"*42)

          
class Person: 
    def __init__(self, name="", data_de_nascimento="", cpf="", endereco="", email=""):
        self.name = name
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.email = email

    def data(self):
      validador = Validar()
      while True:
        print("Informações para data de nascimento (dd/mm/aaaa):")
        dia = valida_numero(input("Informe o Dia: "))
        mes = valida_numero(input("Informe o Mês: "))
        ano = valida_numero(input("Informe o Ano: "))

        if dia is None or mes is None or ano is None:
            print("\033[91mData inválida. Tente novamente.\033[m")
            continue
        
        if validador.valida_data_de_nascimento(dia, mes, ano):
            data = f"{dia:02}/{mes:02}/{ano}"
            print("\033[92mData cadastrada com sucesso!\033[m")
            return data
        else:
            print("\033[91mData inválida. Tente novamente.\033[m")

    def cadastramento(self):
        validador = Validar()
        arquivo = Arquivo()
        armazenador_temporario_de_dados = []
        
    
        while True:
            self.nome = validador.valida_nome(input("Por favor, informe o seu nome completo: "))
            if self.nome:  
                break

        while True:
            self.data_de_nascimento = self.data()
            if self.data_de_nascimento: 
                break
            else:
                print("\033[91mData inválida. Tente novamente.\033[m")
        
        while True:
            self.cpf = validador.validacao_cpf(input("Por favor, informe o seu CPF (somente números): "))
            if self.cpf: 
                break
            else:
                print("\033[91mCpf inválido. Tente novamente.\033[m")

        while True:
            self.email = validador.valida_email(input("Por favor, informe o seu endereço de e-mail: "))
            if self.email: 
                break
            else:
                print("\033[91mEmail inválido. Tente novamente.\033[m")

        
        self.endereco = input("Por favor, informe o seu endereço completo: ").title()
        if self.endereco == '':
            self.endereco = "Não Informado"

        horario_cadastro = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        armazenador_temporario_de_dados.append({
           "nome": self.nome,
           "data_de_nascimento": self.data_de_nascimento,
           "cpf": self.cpf,
           "email": self.email,
           "endereco": self.endereco,
           "data do cadastramento": horario_cadastro,

        })


        
        arquivo.escrever(armazenador_temporario_de_dados)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.data_de_nascimento!r}, {self.cpf!r}, {self.endereco!r} ,{self.email!r})'
        return f'{class_name}{attrs}'








































# O limite , Limite disponível: {limite_atual:.2f}
def depositar(historico, saldo, valor):
        LIMITE_DE_DEPOSITO = 10000
        horario = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if valor <= 0:
            print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
            return saldo
        

        saldo_atual = saldo
        limite_atual = LIMITE_DE_DEPOSITO
     
        if saldo_atual + valor > limite_atual:
            print(f"\033[91mErro: O saldo total não pode ultrapassar o limite do banco ({limite_atual}).\033[m")
            return saldo   
        
        saldo_atual += valor   
        saldo = saldo_atual
        historico.append(f"Depósito de R$ {valor:.2f} - Realizado em {horario}")

        print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {saldo:.2f}\033[m")
        return saldo

7

def sacar(historico, saldo, valor, saques_diarios, limite):
        LIMITE_DO_SAQUE = 1000
        horario = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if valor > LIMITE_DO_SAQUE:
            print(f"Você não pode sacar mais que R${LIMITE_DO_SAQUE} por saque.")
            return saldo, saques_diarios, limite

        if valor <= 0:
            print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
            return saldo, saques_diarios, limite
        
        if saques_diarios == 0:
            print(f"\033[91mVocê atingiu o limite de saques diários.\033[m")
            return saldo, saques_diarios, limite

        saldo_disponivel = saldo + limite  

        print(f"O saldo atual: R$ {saldo:.2f} | Limite disponível: R$ {limite:.2f}")

        if valor > saldo_disponivel:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            return saldo, saques_diarios, limite
        
        valor_sacado = valor

        if valor <= saldo:
            saldo -= valor

        else:
            diferenca = valor - saldo  
            saldo = 0  
            limite -= diferenca  

        # Armazena o valor correto antes da modificação
        historico.append(f"Saque de R$ {valor_sacado:.2f} - Realizado em {horario}")
        saques_diarios -= 1

        print(f"\033[92mSaque de R$ {valor_sacado:.2f} realizado! Novo saldo: R$ {saldo:.2f} | Novo limite: R$ {limite:.2f}\033[m")

        return saldo, saques_diarios, limite


def imprimir(historico):
    indice = 1
    print("-"*42)
    print("\033[38;5;136m============ Extrato da Conta ============\033[m")
    for extrato in historico:  
        print(f"\033[38;5;136m{indice}*: {extrato}\033[m") 
        indice += 1
    print("-"*42)
    






def execute():
    historico = [] # ADD futuramente na classe conta. 
    saldo = 0
    saques_diarios = 3  # Quantidade máxima de saques por dia
    
    limite_do_saque = 1000
    
    while True:
        menu()
        option = valid_option(input("Informe a option do menu acima: "))
        

        if option is None:
            print("\033[91mErro: Opção inválida. Tente novamente.\033[m")
            continue

        match option:
            case 1:
                print("\033[38;5;136m===== Cadastro de Cliente =====\033[m")
                print("\033[38;5;136m===== Escolha o tipo de conta: =====\033[m")
                print("\033[38;5;21m[1] - Conta Poupança.\033[m")
                print("\033[38;5;21m[2] - Conta Corrente.\033[m")
                    

            case 2:
                print("\033[38;5;21m[2] - Mostrar Informações da Conta.\033[m")
                # Dados pessoais Json. <- nome.
                # Dados da conta .txt <- agencia.
                   

            case 3:


                while True:
                  valor = valid_number(input("Informe o valor a ser sacado: "))
    
                  if valor is not None:  
                      saldo, saques_diarios, limite_do_saque = sacar(historico, saldo, valor, saques_diarios, limite_do_saque)
                      break  
                  else:
                      print("\033[91mTente novamente.\033[m")   

                saldo, saques_diarios, limite_do_saque = sacar(historico, saldo, valor, saques_diarios, limite_do_saque)
                

            case 4:
                while True:
                  valor = valid_number(input("Informe o valor a ser sacado: "))
    
                  if valor is not None:  
                      saldo, saques_diarios, limite_do_saque = sacar(historico, saldo, valor, saques_diarios, limite_do_saque)
                      break  
                  else:
                      print("\033[91mTente novamente.\033[m")  
                      
                saldo = depositar(historico, saldo, valor)
                
                
                
            case 5:
                print("\033[38;5;21m[5] - Extrato.\033[m")
                imprimir(historico)

            case 6:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                sleep(5)
                clear_screen()
                break



execute()






"""
class Pessoa: 
    def __init__(self, nome="", data_de_nascimento="", cpf="", endereco="", email=""):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.email = email

    def data(self):
      validador = Validar()
      while True:
        print("Informações para data de nascimento (dd/mm/aaaa):")
        dia = valida_numero(input("Informe o Dia: "))
        mes = valida_numero(input("Informe o Mês: "))
        ano = valida_numero(input("Informe o Ano: "))

        if dia is None or mes is None or ano is None:
            print("\033[91mData inválida. Tente novamente.\033[m")
            continue
        
        if validador.valida_data_de_nascimento(dia, mes, ano):
            data = f"{dia:02}/{mes:02}/{ano}"
            print("\033[92mData cadastrada com sucesso!\033[m")
            return data
        else:
            print("\033[91mData inválida. Tente novamente.\033[m")

    def cadastramento(self):
        validador = Validar()
        arquivo = Arquivo()
        armazenador_temporario_de_dados = []
        
    
        while True:
            self.nome = validador.valida_nome(input("Por favor, informe o seu nome completo: "))
            if self.nome:  
                break

        while True:
            self.data_de_nascimento = self.data()
            if self.data_de_nascimento: 
                break
            else:
                print("\033[91mData inválida. Tente novamente.\033[m")
        
        while True:
            self.cpf = validador.validacao_cpf(input("Por favor, informe o seu CPF (somente números): "))
            if self.cpf: 
                break
            else:
                print("\033[91mCpf inválido. Tente novamente.\033[m")

        while True:
            self.email = validador.valida_email(input("Por favor, informe o seu endereço de e-mail: "))
            if self.email: 
                break
            else:
                print("\033[91mEmail inválido. Tente novamente.\033[m")

        
        self.endereco = input("Por favor, informe o seu endereço completo: ").title()
        if self.endereco == '':
            self.endereco = "Não Informado"

        horario_cadastro = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        armazenador_temporario_de_dados.append({
           "nome": self.nome,
           "data_de_nascimento": self.data_de_nascimento,
           "cpf": self.cpf,
           "email": self.email,
           "endereco": self.endereco,
           "data do cadastramento": horario_cadastro,

        })


        
        arquivo.escrever(armazenador_temporario_de_dados)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.data_de_nascimento!r}, {self.cpf!r}, {self.endereco!r} ,{self.email!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    arquivo = Arquivo()
    def __init__(self, nome, data_de_nascimento, cpf, endereco, email):
        super().__init__(nome, data_de_nascimento, cpf, endereco, email)  # Reutilizando atributos da classe pai

        self.conta: Conta | None = None

class Banco:
    def __init__(
                 self,
                 agencias: list[int] | None =  None,
                 clientes:  list[Pessoa] | None =  None, 
                 contas:  list[Conta] | None =  None,
                 ):
        
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False 
        
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False 
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False 
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False 



    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and  self._checa_cliente(cliente) and self._checa_conta(conta) and \
        self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def adicionar_conta(self, conta: Conta):
        Adiciona uma conta (Corrente ou Poupança) à lista de contas do banco.
        if conta not in self.contas:
            self.contas.append(conta)
            print(f"\033[92mConta {conta.conta} adicionada com sucesso ao banco!\033[m")
        else:
            print(f"\033[93mConta {conta.conta} já está cadastrada.\033[m")


    def listar_contas(self):
        Lista todas as contas cadastradas no banco
        print("\n🔹 Contas Cadastradas no Banco:")
        for conta in self.contas:
            print(f"- {conta}")

    def obter_agencias(self):
       Retorna uma lista com todas as agências cadastradas nas contas do banco.
       return list({conta.agencia for conta in self.contas})


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}{attrs}'
    





"""