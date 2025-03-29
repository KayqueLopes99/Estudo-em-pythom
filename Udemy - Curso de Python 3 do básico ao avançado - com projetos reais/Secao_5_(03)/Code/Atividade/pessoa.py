from tratativas import valida_numero, valida_opcao_inteiro, Validar
from datetime import datetime
import re
from file import Arquivo
import os
from random import randint
from conta import Conta, ContaCorrente, ContaPoupanca
from time import sleep

def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[38;5;136m")
    sleep(0.3)
    print("\033[38;5;136m===== Menu de Opções =====\033[38;5;136m")
    sleep(0.3)
    print("\033[38;5;21m[1] - Cadastramento.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[2] - Mostrar Informações da Conta.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[3] - Sacar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[4] - Depositar.\033[m")
    sleep(0.3)
    print("\033[38;5;21m[5] - Sair do Sistema Bancário.\033[m")
    sleep(0.3)
    print("-"*42)
             
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
        """Adiciona uma conta (Corrente ou Poupança) à lista de contas do banco."""
        if conta not in self.contas:
            self.contas.append(conta)
            print(f"\033[92mConta {conta.conta} adicionada com sucesso ao banco!\033[m")
        else:
            print(f"\033[93mConta {conta.conta} já está cadastrada.\033[m")


    def listar_contas(self):
        """Lista todas as contas cadastradas no banco."""
        print("\n🔹 Contas Cadastradas no Banco:")
        for conta in self.contas:
            print(f"- {conta}")

    def obter_agencias(self):
       """Retorna uma lista com todas as agências cadastradas nas contas do banco."""
       return list({conta.agencia for conta in self.contas})


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}{attrs}'
    
def executar():
    banco = Banco()
    cliente = None  
    
    
    while True:
        menu()
        escolha = valida_opcao_inteiro(input("Informe a escolha do menu acima: "))

        if escolha is None:
            continue

        match escolha:
            case 1:
                print("\033[38;5;136m===== Cadastro de Cliente =====\033[m")
                pessoa = Pessoa()
                pessoa.cadastramento()

                cliente = Cliente(pessoa.nome, pessoa.data_de_nascimento, pessoa.cpf, pessoa.endereco, pessoa.email)

                while True:
                    print("\033[38;5;136m===== Escolha o tipo de conta: =====\033[m")
                    print("\033[38;5;21m[1] - Conta Poupança.\033[m")
                    print("\033[38;5;21m[2] - Conta Corrente.\033[m")
                    

                    tipo_conta = valida_opcao_inteiro(input("Informe o tipo de conta desejado: "))

                    if tipo_conta not in [1, 2]:
                        print("\033[91mErro: Opção inválida! Escolha novamente.\033[m")
                        continue

                   
                    agencia = randint(10000, 50000)
                    numero_conta = randint(1000, 9999)
                    
                    if tipo_conta == 1:
                        conta = ContaPoupanca(agencia, numero_conta, saldo=0)
                    else:
                        limite = valida_numero(input("Informe o limite da conta corrente: "))
                        conta = ContaCorrente(agencia, numero_conta, saldo=0, limite=limite)

                    cliente.conta = conta  
                    banco.clientes.append(cliente)
                    banco.adicionar_conta(conta)

                    
                    if agencia not in banco.agencias:
                        banco.agencias.append(agencia)
                    
                    break  
                
                print("\n\033[92mCliente cadastrado com sucesso!\033[m")
                print(cliente)
                print(cliente.conta)

            case 2:
                   
               validador = Validar()
               arquivo = Arquivo()
    
               nome = validador.valida_nome(input("Por favor, informe o seu nome completo: "))
               cliente_dados = arquivo.acessar_dados_pelo_nome(nome)  # 🔹 Busca o cliente no arquivo
    
               if cliente_dados is None:
                  print(f"\033[91mErro: Nenhum cliente cadastrado com esse nome!\033[m")
               else:
                  print(f"\033[38;5;136m===== Dados do Cliente {cliente_dados['nome']}: =====\033[m")
        

               cliente = None
               for c in banco.clientes:
                 if c.nome == nome:
                    cliente = c
                    break  

               if cliente is None:
                   print("\033[91mErro: Nenhum cliente cadastrado no sistema bancário!\033[m")
               elif cliente.conta is None:
                   print("\033[91mErro: Cliente não possui uma conta cadastrada!\033[m")
               elif banco.autenticar(cliente, cliente.conta):
                   conta_cliente = cliente.conta.obter_dados_conta()
                   if conta_cliente:
                     for key, value in conta_cliente[0].items():
                       print(f"{key}: {value}")
                       
                   else:
                      print("Nenhum dado de conta encontrado.")

                   print(cliente.conta.obter_saldo_e_limite())   
               else:
                   print("\033[91mErro: Falha na autenticação do cliente!\033[m")

            case 3:
                if cliente and banco.autenticar(cliente, cliente.conta):
                    print("Você escolheu: Sacar.")
                    valor = valida_numero(input("Informe o valor a ser Sacado: "))
                    cliente.conta.sacar(valor)
                else:
                    print("\033[91mErro: Cliente não autenticado ou inexistente!\033[m")

            case 4:
                if cliente and banco.autenticar(cliente, cliente.conta):
                    print("Você escolheu: Depositar.")
                    valor = valida_numero(input("Informe o valor a ser Depositado: "))
                    cliente.conta.depositar(valor)
                else:
                    print("\033[91mErro: Cliente não autenticado ou inexistente!\033[m")

            case 5:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                sleep(5)
                os.system('cls')
                break




