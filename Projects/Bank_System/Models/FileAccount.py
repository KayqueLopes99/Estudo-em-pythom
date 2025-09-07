from pathlib import Path
import re
from datetime import datetime
class FileAccount:

    def __init__(self, fileText: str = 'dateAccount.txt'):
        # Define a pasta storage
        storageFolder = Path(__file__).parent / 'storage'
        storageFolder.mkdir(exist_ok=True)  # cria a pasta se não existir

        # Define o caminho completo do arquivo
        self.pathText = storageFolder / fileText
        self.pathText.touch(exist_ok=True)  # cria o arquivo se não existir
 
             
             
    def write(self, typeAccount, cpf, accountNumber, accountHolder, branch, balance, accountType, limit=0):
        try:
            # Se for conta corrente, adiciona o limite
            if typeAccount.lower() == "checking account":
                newDatasAccount = f"{cpf};{accountNumber};{accountHolder};{branch};{balance};{accountType};{limit}\n"
            else:
                newDatasAccount = f"{cpf};{accountNumber};{accountHolder};{branch};{balance};{accountType}\n"

            with open(self.pathText, 'r', encoding='utf-8') as file:
                content = file.readlines()

            found = False
            for i, line in enumerate(content):
                if line.startswith(f"{cpf};"):
                    found = True
                    break

            if found:
                print(f"Account with CPF {cpf} already exists!")
            else:
                content.append(newDatasAccount)
                print(f"\033[92mAccount for CPF {cpf} created successfully!\033[m")

            with open(self.pathText, 'w', encoding='utf-8') as file:
                file.writelines(content)

        except Exception as error:
            print(f"\033[91mError saving data: {error}\033[m")

    def updateBalance(self, cpf: str, newBalance: float, newLimit: float = None) -> None:
        try:
            with open(self.pathText, 'r', encoding='utf-8') as file:
                content = file.readlines()

            updated = False
            for i, line in enumerate(content):
                if line.startswith(f"{cpf};"):
                    parts = line.strip().split(';')
                    # Atualiza saldo
                    parts[4] = str(newBalance)
                    # Atualiza limite se for conta corrente e o parâmetro foi passado
                    if len(parts) > 6 and parts[5].lower() == "checking account" and newLimit is not None:
                        parts[6] = str(newLimit)
                    content[i] = ';'.join(parts) + '\n'
                    updated = True
                    break

            if updated:
                with open(self.pathText, 'w', encoding='utf-8') as file:
                    file.writelines(content)
                print(f"\033[92mBalance for CPF {cpf} updated successfully!\033[m")
            else:
                print(f"\033[91mAccount with CPF {cpf} not found!\033[m")

        except Exception as error:
            print(f"\033[91mError updating balance: {error}\033[m")


    def read(self, cpf: str) -> list[str] | None:
        try:
            with open(self.pathText, 'r', encoding='utf-8') as file:
                content = file.readlines()

            for line in content:
                parts = line.strip().split(';')
                if parts[0] == cpf:      
                    return parts

            return None

        except FileNotFoundError:
            print("\033[91mFile not found.\033[m")
            return None
        except Exception as error:
            print(f"\033[91mError reading file: {error}\033[m")
            return None





class FileStatement:
    def __init__(self, fileText: str = 'statement.txt'):
        storageFolder = Path(__file__).parent / 'storage'
        storageFolder.mkdir(exist_ok=True)
        self.pathText = storageFolder / fileText
        self.pathText.touch(exist_ok=True)


    def write(self, cpf: str, entry: str, transactionTime: datetime) -> None:
        try:
            timestamp_str = transactionTime.strftime('%d-%m-%Y %H:%M:%S')
            
            newEntry = f"{cpf};{timestamp_str};{entry}\n"
            
            with open(self.pathText, 'a', encoding='utf-8') as file:
                file.write(newEntry)
            
            print(f"\033[92mStatement entry for CPF {cpf} added successfully!\033[m")

        except Exception as error:
            print(f"\033[91mError saving statement entry: {error}\033[m")

    def read(self, cpf: str) -> list[str]:
        try:
            with open(self.pathText, 'r', encoding='utf-8') as file:
                content = file.readlines()

            entries = []
            for line in content:
                parts = line.strip().split(';', 2) 
                # parts[0] = cpf, parts[1] = timestamp, parts[2] = entry
                
                if parts[0] == cpf and len(parts) == 3:
                    formatted_entry = f"{parts[2]} | Date: {parts[1]}"
                    entries.append(formatted_entry)
            
            return entries

        except FileNotFoundError:
            print("\033[91mFile not found.\033[m")
            return []
        except Exception as error:
            print(f"\033[91mError reading statement file: {error}\033[m")
            return []