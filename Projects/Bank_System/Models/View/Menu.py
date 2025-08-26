from time import sleep
import sys
import os
from random import randint
from FileClient import FileClient
from FileAccount import FileAccount


from Tratatives import Tratatives
from Client import Client
from Accounts import BankAccount, CheckingAccount, SavingsAccount

def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")
    
def menu():
    print("-"*42)
    print("\033[38;5;136m===== Welcome to FinTechOne Bank! =====\033[38;5;136m")
    print("\033[38;5;136m===== Menu Options =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Register.\033[m")
    print("\033[38;5;21m[2] - View data registers.\033[m")
    print("\033[38;5;21m[3] - List clients.\033[m")

    print("\033[38;5;21m[4] - Check data Account.\033[m")
    print("\033[38;5;21m[5] - Withdraw.\033[m")
    print("\033[38;5;21m[6] - Deposit.\033[m")
    print("\033[38;5;21m[7] - Exit banking system.\033[m")
    print("-"*42)

def executeMenu():
    validator = Tratatives()
    client: Client = None
    
    while True:
        menu()
        choice = validator.validate_integer_option(input("Enter your choice from the menu above: "))

        if choice is None:
            continue

        match choice:
            case 1:
                client = Client()
                client.registerClient()
                
                
                while True:
                    print("\033[38;5;136m===== Choose account type: =====\033[m")
                    print("\033[38;5;21m[1] - Savings Account.\033[m")
                    print("\033[38;5;21m[2] - Checking Account.\033[m")

                    option2: int = validator.validate_integer(input("Enter the desired account type: "))

                    if option2 not in [1, 2]:
                        print("\033[91mError: Invalid option! Please choose again.\033[m")
                        continue
                    
                    match option2:
                        case 1:
                            branch: int = randint(10000, 50000)
                            savingsAccount: BankAccount = SavingsAccount(client.cpf, client.name, branch)
                            client.account = savingsAccount
                            savingsAccount.createAccount()
                            print("\033[92mReturning to the previous menu!\033[m")
                            sleep(5)
                            os.system('cls')
                            break
                            
                        case 2: 
                            branch: int = randint(10000, 50000)
                            checkingAccount: BankAccount = CheckingAccount(client.cpf, client.name, branch)
                            client.account = checkingAccount
                            checkingAccount.createAccount()
    
                        
                            print("\033[92mReturning to the previous menu!\033[m")
                            sleep(5)
                            os.system('cls')
                            break

                    
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
                password = input("Enter administrator password to list all clients: ")
                if password == "admin7":
                    Client.listDatesOfClients()  
                else:
                    error_message("Incorrect password! Access denied.")
            
            case 4:
                 while True:
                    cpf = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
                    if cpf:
                        cpfClean = cpf.replace('.', '').replace('-', '')
                        BankAccount.printDataAccount(cpfClean)
                        break
                    else:
                        error_message("-"*30)
                
            case 5:
                
             file: FileAccount = FileAccount()

             while True:
                 cpf: str = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
                 if cpf:
                     cpfClean = cpf.replace('.', '').replace('-', '')
                     accountData: list[str] | None = file.read(cpfClean)
            
                     if accountData is not None:
                         cpf_value = accountData[0].strip()
                         accountNumber = int(accountData[1].strip())
                         accountHolder = accountData[2].strip()
                         branch = accountData[3].strip()
                         balance = float(accountData[4].strip())
                         accountType = accountData[5].strip()
                         while True:
                            value_input = input("Enter the amount to withdraw: ")
                            value = validator.validate_integer(value_input)
                            if value is not None:
                                break
                         if accountType == "Savings Account":
                               
                             account = SavingsAccount(cpf_value, accountHolder, branch, balance, accountType)
                             account.withdraw(cpf_value, value)
                             break
                         elif accountType == "Checking Account":
                             account = CheckingAccount(cpf_value, accountHolder, branch, balance, accountType)
                             account.withdraw(cpf_value, value)
                             break
                     else:
                         print(f"\033[91mAccount with CPF {cpf} not found!\033[m")
                         break
                 else:
                     error_message("-"*30)

            
            case 6:
                account: BankAccount = BankAccount()
                while True:
                    cpf: str = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
                    if cpf:
                        cpfClean = cpf.replace('.', '').replace('-', '')
                        while True:
                            value_input = input("Enter the amount to deposit: ")
                            value = validator.validate_integer(value_input)
                            if value is not None:
                                account.deposit(cpfClean, value)
                                break
                        
                        break
                    else:
                        error_message("-"*30)
            case 7:
                print("\033[92mExiting banking system. Come back soon!\033[m")
                sleep(5)
                os.system('cls')
                break


