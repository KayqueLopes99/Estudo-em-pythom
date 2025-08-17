
from time import sleep
import sys
import os
from random import randint
from FileClient import FileClient
# Adiciona a pasta raiz do projeto no sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Tratatives import Tratatives
from Client import Client
from Accounts import BankAccount, CheckingAccount
def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")
    
    
def menu():
    print("-"*42)
    print("\033[38;5;136m===== Bem-vindo ao Banco FinTechOne! =====\033[38;5;136m")
    print("\033[38;5;136m===== Menu de Opções =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Register.\033[m")
    print("\033[38;5;21m[2] - View data registers.\033[m")
    print("\033[38;5;21m[3] - List clients.\033[m") # recurso do adminitrador!    


    
    print("\033[38;5;21m[3] - Consultar Saldo.\033[m")
    print("\033[38;5;21m[4] - Sacar.\033[m")
    print("\033[38;5;21m[5] - Depositar.\033[m")
    print("\033[38;5;21m[6] - Sair do Sistema Bancário.\033[m")
    print("-"*42)

     
def executeMenu():
    validator = Tratatives()
    client: Client = None
    
    while True:
        
        menu()
        escolha = validator.validate_integer_option(input("Informe a escolha do menu acima: "))

        if escolha is None:
            continue

        match escolha:
            case 1:
                tempDataStorage = []

# Criando um objeto Client diretamente
                client = Client(
     name="Maria Souza",
    dateOfBirth="15/03/1995",
    cpf="10931769469",
    email="maria.souza@example.com",
    address="Rua das Flores, 123 - São Paulo/SP"
)
                tempDataStorage.append({
    "name": "Maria Souza",
    "dateOfBirth": "15/03/1995",
    "cpf": "10931769469",
    "email": "maria.souza@example.com",
    "address": "Rua das Flores, 123 - São Paulo/SP",
    "registration_time": "2025-08-17 13:00:00"
})
                
                

# Agora sim, adiciona o objeto client ao armazenamento
                ##tempDataStorage.append(client)

                fileRegister = FileClient()
                fileRegister.write(tempDataStorage)
 
                
                
                
                # print("\033[38;5;136m===== Enter data client  =====\033[m")                
                # client = Client()
                # fileRegister.write(tempDataStorage)
                # ## client.registerClient()
                
                while True:
                    print("\033[38;5;136m===== Escolha o tipo de conta: =====\033[m")
                    print("\033[38;5;21m[1] - Conta Poupança.\033[m")
                    print("\033[38;5;21m[2] - Conta Corrente.\033[m")
                    print("\033[38;5;21m[0] - Voltar.\033[m")
                    
                    
                    

                    option2 : int = validator.validate_integer(input("Informe o tipo de conta desejado: "))


                    if option2 not in [0, 1, 2]:
                        print("\033[91mErro: Opção inválida! Escolha novamente.\033[m")
                        continue
                    
                    
                    match option2:
                        case 1:
                            branch = randint(10000, 50000)
                        case 2: 
                            branch: int = randint(10000, 50000)
                            checkingAccount: BankAccount = CheckingAccount(client.cpf, client.name, branch)
                            client.account = checkingAccount
                            checkingAccount.createAccount()
                        case 0:
                            print("\033[92m Voltando para o meno anterior!\033[m")
                            sleep(5)
                            os.system('cls')
                            break
                           
                                               
                        
                        
                                                

                    # Lógica do banco
                    # cliente.conta = conta  
                    # banco.clientes.append(cliente)
                    # banco.adicionar_conta(conta)

                    
                    # if agencia not in banco.agencias:
                    #    banco.agencias.append(agencia)
                    
                    # break  
                
            
            
                
            case 2:
                while True:
                   cpf = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
                   if cpf:
                      cpfClean = cpf.replace('.', '').replace('-', '')
                      Client.printDataClient(cpfClean)
                      break
                   else:
                      error_message("-"*30)
                              
            case 3:
                senha = input("Digite a senha de administrador para listar todos os clientes: ")
                if senha == "admin7":
                    Client.listDatesOfClients()  
                else:
                    error_message("Senha incorreta! Acesso negado.")
            case 4:
                pass
            case 5:
                account: BankAccount = BankAccount()
                while True:
                    
                   cpf: str = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
                   if cpf:
                      cpfClean = cpf.replace('.', '').replace('-', '')
                      account.deposit(cpfClean, 100)
                      break
                   else:
                      error_message("-"*30)
                
                
                
                
            case 6:
                print("\033[92mSaindo do Sistema Bancário. Volte Sempre!\033[m")
                sleep(5)
                os.system('cls')
                break
            


