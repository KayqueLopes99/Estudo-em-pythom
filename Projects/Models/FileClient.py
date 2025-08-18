from pathlib import Path

class FileClient:
  
  def __init__(self, fileText: str = 'clients.txt'):
        # Define a pasta storage
        storageFolder = Path(__file__).parent / 'storage'
        storageFolder.mkdir(exist_ok=True)  # cria a pasta se não existir

        # Define o caminho completo do arquivo
        self.pathText = storageFolder / fileText
        self.pathText.touch(exist_ok=True)  # cria o arquivo se não existir


  def write(self, clientDataList: list) -> None:
    try:
        with open(self.pathText, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for clientData in clientDataList: 
            formattedData = f"{clientData['cpf']}; {clientData['name']}; {clientData['dateOfBirth']}; {clientData['email']}; {clientData['address']}; {clientData['registrationTime']}\n"

            existingPerson = False
            for i, line in enumerate(lines):
                if line.startswith(f"{clientData['cpf']};"):
                    lines[i] = formattedData
                    existingPerson = True
                    break

            if not existingPerson:
                lines.append(formattedData)

        with open(self.pathText, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    except Exception as error:
        print(f"\033[91mError saving data: {error}\033[m")

  def listClients(self) -> None:
    try:
        # Read all lines from the file
        with open(self.pathText, 'r', encoding='utf-8') as file:
            content = file.readlines()
            
        print("-" * 80)
        # Azul escuro negrito
        print("\033[1;38;5;19mRegistered Client Data:\033[m")


        print("-" * 80)
        
        if not content:
            print("\033[93mNo client data available to display.\033[m")
        else:
            for index, item in enumerate(content, start=1):
                dates = item.strip().split(';')
                print(f"[{index}] CPF: {dates[0]} | Name: {dates[1]} | Date of Birth: {dates[2]} | Email: {dates[3]} | Address: {dates[4]} | Registration Time: {dates[5]}")
                
        print("-" * 80)

    except FileNotFoundError:
        print("\033[91mFile not found.\033[m")
    except Exception as error:
        print(f"\033[91mError reading the file: {error}\033[m")


  def read(self, cpf: str) -> list[str] | None:
    cpfClean = cpf.replace('.', '').replace('-', '')

    try:
        with open(self.pathText, 'r', encoding='utf-8') as file:
            content = file.readlines()

        for line in content:
            if line.strip().startswith(f"{cpfClean.strip()};"):
                dados = [campo.strip() for campo in line.strip().split(';')]
                return dados
        return None 

    except FileNotFoundError:
        print("\033[91mFile not found.\033[m")
    except Exception as error:
        print(f"\033[91mError reading the file: {error}\033[m")

