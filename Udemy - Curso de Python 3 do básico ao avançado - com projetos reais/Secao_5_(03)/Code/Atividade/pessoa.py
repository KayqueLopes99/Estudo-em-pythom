from tratativas import valida_cpf, mensagem_erro, mensagem_sucesso, valida_numero, valida_opcao_inteiro
from datetime import datetime
import re
from file import Arquivo
import os
from random import randint
from conta import Conta, ContaCorrente, ContaPoupanca


def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[38;5;136m")
    print("\033[38;5;136m===== Menu de Opções =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Cadastramento.\033[m")
    print("\033[38;5;21m[2] - Mostrar Informações da Conta.\033[m")
    print("\033[38;5;21m[3] - Sacar.\033[m")
    print("\033[38;5;21m[4] - Depositar.\033[m")
    print("\033[38;5;21m[5] - Sair do Sistema Bancário.\033[m")
    print("-"*42)

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

           

# deve ajustar na opção de imprimir dados da pessoa especificada-----------------------------------       
def acessar_conta():
     validador = Validar()
     arquivo = Arquivo()

     while True:
            nome_usuario = validador.valida_nome(input("Por favor, informe o seu nome completo cadastrado: ")).title()

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



    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.data_de_nascimento!r}, {self.cpf!r}, {self.endereco!r} ,{self.email!r})'
        return f'{class_name}{attrs}'

  
# ajuste. 
class Cliente(Pessoa):
    arquivo = Arquivo()
    def __init__(self, nome, data_de_nascimento, cpf, endereco, email):
        super().__init__(nome, data_de_nascimento, cpf, endereco, email)  # Reutilizando atributos da classe pai

        # dados_cadastrados saia talvez!!!!
        # self.dados_cadastrados = dados_cadastrados \ dados_cadastrados=None->init
        self.conta: Conta | None = None


    #@property
    # def dados(self):
        """Getter: Retorna os dados da conta do cliente."""
    #   return self.dados_cadastrados



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

    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and  self._checa_cliente(cliente) and self._checa_conta(conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}{attrs}'


# Função para pegar os dados da conta das pessoas e colocar numa lista do tipo [{}].

# Função para pegar os dados das agencias e colocar numa lista do tipo [].

# função de pegar os dados docliente já está feita.

# em sacar e depositar 
# a pessoa informa o nome, a agencia e os dados da conta já são colocados atomaticamente
# imprime os dados da conta relacionada.

# adicionar uma verificação so pode sacar e depoisitar se o nome do cliente estiver na lista [{}],  e a agencia [] -> a conta [{}].
# 


# dados da conta, das agencia e do cliente[ok]














def executar():
    cliente = None 

    while True:
        menu()
        escolha = valida_opcao_inteiro(input("Informe a escolha do menu acima: "))

        if escolha is None:
            continue

        match escolha:
            case 1:
                print("\n🔹 Cadastro de Cliente 🔹")
                pessoa = Pessoa()
                pessoa.cadastramento()

                # Criando o cliente
                cliente = Cliente(pessoa.nome, pessoa.data_de_nascimento, pessoa.cpf, pessoa.endereco, pessoa.email)

                while True:
                    print("\nEscolha o tipo de conta:")
                    print("1 - Conta Poupança")
                    print("2 - Conta Corrente")

                    tipo_conta = valida_opcao_inteiro(input("Informe o tipo de conta desejado: "))

                    if tipo_conta not in [1, 2]:
                        print("\033[91mErro: Opção inválida! Escolha novamente.\033[m")
                        continue

                    # Criando a conta associada ao cliente
                    if tipo_conta == 1:
                        cliente.conta = ContaPoupanca(randint(10000, 50000), randint(1000, 9999), saldo=0)
                    else:
                        limite = valida_opcao_inteiro(input("Informe o limite da conta corrente: "))
                        cliente.conta = ContaCorrente(randint(10000, 50000), randint(1000, 9999), saldo=0, limite=limite)

                    break  # Sai do loop após escolher uma conta válida
                
                print("\n\033[92mCliente cadastrado com sucesso!\033[m")
                print(cliente)
                print(cliente.conta)

            case 2:
                arquivo = Arquivo()
                if cliente is None:
                    print("\033[91mErro: Nenhum cliente cadastrado!\033[m")
                elif cliente.conta is None:
                    print("\033[91mErro: Cliente não possui uma conta cadastrada!\033[m")
                else:
                    arquivo.ler_ou_imprimir("imprimir")
                    print(cliente.conta.obter_saldo_e_limite())

            case 3:
                print("Você escolheu: Sacar.")
                if cliente is None:
                    print("\033[91mErro: Nenhum cliente cadastrado!\033[m")
                elif cliente.conta is None:
                    print("\033[91mErro: Cliente não possui uma conta cadastrada!\033[m")
                else:
                    valor = valida_numero(input("Informe o valor a ser Sacado: "))
                    cliente.conta.sacar(valor)

            case 4:
                print("Você escolheu: Depositar.")
                if cliente is None:
                    print("\033[91mErro: Nenhum cliente cadastrado!\033[m")
                elif cliente.conta is None:
                    print("\033[91mErro: Cliente não possui uma conta cadastrada!\033[m")
                else:
                    valor = valida_numero(input("Informe o valor a ser Depositado: "))
                    cliente.conta.depositar(valor)

            case 5:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                os.system('cls')
                break


# --------------------------------- Parte de execução.
executar()

