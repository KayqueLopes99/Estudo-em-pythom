from pathlib import Path

class FileAccount:

    def __init__(self, fileText: str = 'dateAccount.txt'):
        # Define a pasta storage
        storageFolder = Path(__file__).parent / 'storage'
        storageFolder.mkdir(exist_ok=True)  # cria a pasta se não existir

        # Define o caminho completo do arquivo
        self.pathText = storageFolder / fileText
        self.pathText.touch(exist_ok=True)  # cria o arquivo se não existir
 
             
             
    def white(self, cpf, accountNumber, accountHolder, branch, balance, accountType):
        try:
            newDatasAccount: str  = f"{cpf};{accountNumber};{accountHolder};{branch};{balance};{accountType}\n" 

            with open(self.pathText, 'r', encoding='utf-8') as file:
                content = file.readlines()

            found: bool = False
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

    def updateBalance(self, cpf: str, newBalance: float):
       try:
        with open(self.pathText, 'r', encoding='utf-8') as file:
            content = file.readlines()

        updated = False 
        for i, line in enumerate(content):
            if line.startswith(f"{cpf};"):
                parts = line.strip().split(';')
                parts[4] = str(newBalance) 
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
            if line.strip().startswith(f"{cpf};"):  # CPF somente números
                return line.strip().split(';')

        return None

      except FileNotFoundError:
        print("\033[91mFile not found.\033[m")
        return None
      except Exception as error:
        print(f"\033[91mError reading file: {error}\033[m")
        return None



    