from time import sleep
import os
from Utils import tratatives
from client import registerClient, listDataClient, listClients
from account import createCheckingAccount, listDataAccounts, deposit, print_statement, withdraw

def menu():
    print("-"*45)
    print("\033[38;5;136m======= Welcome to FinTechOne Bank! =======\033[38;5;136m")
    print("\033[38;5;136m       ===== Menu Options =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Register.\033[m")
    print("\033[38;5;21m[2] - View data registers.\033[m")
    print("\033[38;5;21m[3] - List clients.\033[m")

    print("\033[38;5;21m[4] - Check data(s) Account(s) and statement.\033[m") 
    print("\033[38;5;21m[5] - Withdraw.\033[m")
    print("\033[38;5;21m[6] - Deposit.\033[m")
    print("\033[38;5;21m[7] - Exit banking system.\033[m")
    print("-"*45)
      

def executeMenu():
    users: list[dict[str]] = []
    accounts: list[dict[str]] = []
    statement: list = [] 
    balance = 0.0  
    overdraft_limit = 500.0  
    daily_withdrawals = 3 
    

    while True:
        menu()

        choice = tratatives.validateIntegerOption(input("Enter your choice from the menu above: "))
        
        if choice is None:
            continue

        match choice:
            case 1:
                client: dict | None = registerClient(users)
                if client and client not in users:
                    users.append(client)
                    print("\033[92mClient successfully registered!\033[m")
                    for user in users:
                        print(user)
                else:
                    print("\033[93mClient already registered!\033[m")
                                
                while True:
                    option2 = input("Create account (yes/no): ").strip().lower()

                    if option2 not in ['yes', 'no']:
                        print("\033[91mError: Invalid option! Please choose again.\033[m")
                        continue

                    if option2 == 'yes':
                        while True:
                           cpf = tratatives.validateCpf(input("Please enter your CPF (numbers only): "))
                           if cpf:
                               cpfClean = cpf.replace('.', '').replace('-', '')
                               account: dict | None = createCheckingAccount(accounts, users, cpfClean)
                               break
                           else:
                               print("\033[91mError: Invalid CPF! Please try again.\033[m")

                        if account:
                            accounts.append(account)
                            print("\033[92mAccount successfully created!\033[m")
                        else:
                            print("\033[93mAccount creation failed!\033[m")

                        
                    elif option2 == 'no':
                        print("\033[92mReturning to the previous menu!\033[m")
                        sleep(3)
                        os.system('cls')
                        break


                    
            case 2:
                while True:
                    cpf = tratatives.validateCpf(input("Please enter your CPF (numbers only): "))
                    if cpf:
                        cpfClean = cpf.replace('.', '').replace('-', '')
                        listDataClient(cpfClean, users)
                              
                        break
                    else:
                        print("\033[91mError: Invalid CPF! Please try again.\033[m")
                        
            
                     
            case 3:
                password = input("Enter administrator password to list all clients: ")
                if password == "admin7":
                    listClients(users)
                else:
                    print("\033[91mIncorrect password! Access denied.\033[m")            
            
            
            
            case 4:
                   while True:
                      cpf = tratatives.validateCpf(input("Please enter your CPF (numbers only): "))
                      
                      
                      if cpf:
                          cpfClean = cpf.replace('.', '').replace('-', '')
                          listDataAccounts(cpfClean, accounts, balance, statement)
                          
        
                          break
                   
                
            case 5:
                
                

                while True:
                    cpf: str = tratatives.validateCpf(input("Please enter your CPF (numbers only): "))
                    if cpf:
                        cpfClean = cpf.replace('.', '').replace('-', '')
            
    
                        while True:
                           value_input = input("Enter the amount to withdraw: ")
                           value = tratatives.validateFloat(value_input)
                           if value is not None:
                               ## def withdraw(*, statement: list[str], balance: float, amount: float, daily_withdrawals: int, overdraft_limit: float) -> tuple[float, int, float]:
                               # return balance, daily_withdrawals, overdraft_limit
                                balance, daily_withdrawals, overdraft_limit = withdraw(
                                        statement=statement,
                                        balance=balance,
                                        amount=value,
                                        daily_withdrawals=daily_withdrawals,
                                        overdraft_limit=overdraft_limit
                                    )
                               
                                break
                        
                           else:
                             print(f"\033[91mAccount with CPF {cpf} not found!\033[m")
                             break
                        break
                    else:
                        print("\033[91mError: Invalid CPF! Please try again.\033[m")

            
            case 6:
                 
                while True:
                     cpf: str = tratatives.validateCpf(input("Please enter your CPF (numbers only): "))
                     if cpf:
                         cpfClean = cpf.replace('.', '').replace('-', '')
                         while True:
                             value_input = input("Enter the amount to deposit: ")
                             value = tratatives.validateFloat(value_input)
                             if value is not None:
                                balance = deposit(statement, balance, value)
                                break
                         break
                     else:
                        print("\033[91mError: Invalid CPF! Please try again.\033[m")
            
                     
            case 7:
                print("\033[92mExiting banking system. Come back soon!\033[m")
                sleep(5)
                os.system('cls')
                break