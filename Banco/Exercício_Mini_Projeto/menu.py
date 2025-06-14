from tratativas import valida_cpf
from datetime import datetime
import re
from file import Arquivo
import os
from random import randint
from contas import Conta


def valida_opcao_inteiro(variavel):
    if isinstance(variavel, int) or (isinstance(variavel, str) and variavel.isdigit()):
        var_int = int(variavel)
        if 1 <= var_int <= 5:
            return var_int
        else:
            print("\033[91mOpção selecionada não está no intervalo [1-12].\033[m")
    else:
        print("\033[91mA opção escolhida deve ser um número inteiro.\033[m")



def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[38;5;136m")
    print("\033[38;5;136m===== Menu de Opções =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Cadastramento.\033[m")
    print("\033[38;5;21m[2] - Consultar Saldo.\033[m")
    print("\033[38;5;21m[3] - Sacar.\033[m")
    print("\033[38;5;21m[4] - Depositar.\033[m")
    print("\033[38;5;21m[5] - Sair do Sistema Bancário.\033[m")
    print("-"*42)


def mensagem_erro(texto):
    print(f"\033[91m{texto}\033[m")

def mensagem_sucesso(texto):
    print(f"\033[92m{texto}\033[m")



class Validar:
    def valida_nome(self, nome):
        if not nome.replace(" ", "").isalpha():
            print("\033[91mNome do Usuário Invalido!\nPor favor, informe um Nome Válido.\033[m")
            return None
    
        nome_formatado = nome.title()
        return nome_formatado
    
    def valida_data_de_nascimento(self, dia, mes, ano):
        try:
            data = datetime(year=ano, month=mes, day=dia)
            if not (1900 <= ano <= 2025):
                mensagem_erro("Erro: Ano Invalido!")
                return False
            return True
        except ValueError:
            print("\033[91mData Inválida! Verifique dia ou mês.\033[m")
            return False
       
    def validacao_cpf(self, cpf):
        resultado = valida_cpf(cpf)
        return resultado
    def valida_email(self, email):
        # Expressão regular para validar formato de e-mail básico
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        # Verificando se o e-mail segue o padrão
        if re.match(padrao_email, email):
            return email
        else:
            print("\033[91mErro: Email não é válido.\033[m")
            return None

           
        

def valida_numero(variavel):
    if isinstance(variavel, (int, float)):  # Verifica se já é um número
        return variavel
    
    if isinstance(variavel, str):  # Se for string, tenta converter
        if variavel.isdigit():  # Verifica se é um número inteiro
            return int(variavel)
        try:
            return float(variavel)  # Tenta converter para float
        except ValueError:
            pass  # Se falhar, cai na mensagem de erro abaixo

    print("\033[91mPor favor, insira um valor numérico válido.\033[m")
    return None

            
def acessar_conta():
     validador = Validar()
     arquivo = Arquivo()

     while True:
            nome_usuario = validador.valida_nome(input("Por favor, informe o seu nome completo cadastrado: ")).capitalize()

            dados_usuario = arquivo.acessar_dados_pelo_nome(nome_usuario)

            if dados_usuario: 
                cliente = Cliente(
            nome=dados_usuario['nome'],
            data_de_nascimento=dados_usuario['data_de_nascimento'],
            cpf=dados_usuario['cpf'],
            endereco=dados_usuario['endereco'],
            email=dados_usuario['email'],
            dados_cadastrados=dados_usuario
        )
        
                break
            else:
                print(f"Usuário {nome_usuario} não encontrado.")


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
            else:
                print("\033[91mNome inválido. Tente novamente.\033[m")

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



   
# ajuste. 
class Cliente(Pessoa):
    arquivo = Arquivo()
    def __init__(self, nome, data_de_nascimento, cpf, endereco, email,  dados_cadastrados):
        super().__init__(nome, data_de_nascimento, cpf, endereco, email)  # Reutilizando atributos da classe pai
        self.dados_cadastrados = dados_cadastrados


    @property
    def dados(self):
        """Getter: Retorna os dados da conta do cliente."""
        return self.dados_cadastrados
    
    

     
def executar():
    while True:
        menu()
        escolha = valida_opcao_inteiro(input("Informe a escolha do menu acima: "))

        if escolha is None:
            continue

        match escolha:
            case 1:
                pessoa = Pessoa()
                pessoa.cadastramento()
                conta = Conta()
                valida = Validar()
                nome = valida.valida_nome(input("Informe o Nome do cadastramento: ")).title()
                conta.adiciona_dados_da_conta(nome)
            
            case 2:
                conta = Conta()
                valida = Validar()
                nome = valida.valida_nome(input("Informe o Nome do cadastramento: "))
                conta.mostrar_saldo(nome)
            case 3:
                print("Você escolheu: Sacar.")
                conta = Conta()  # Cria uma instância da classe Conta
                valida = Validar()  # Cria uma instância da classe Validar
                nome = valida.valida_nome(input("Informe o Nome do cadastramento: ")) # Valida o nome informado
                valor = valida_numero(input("Informe o valor a ser sacado: "))  # Valida o valor do saque
                conta.realizar_saque(nome, valor)  # Chama o método realizar_saque da classe Conta

            case 4:
                
                conta = Conta()
                valida = Validar()
                nome = valida.valida_nome(input("Informe o Nome do cadastramento: ")).title()
                valor = valida_numero(input("Informe o valor a ser depositado na conta: "))
                conta.depositar(nome, valor)
            case 5:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                os.system('cls')
                break
            


executar()