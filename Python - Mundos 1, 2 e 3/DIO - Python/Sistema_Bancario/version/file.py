from pathlib import Path
import json


# Arquivo que manipula os dados pessoais.
class PersonalDataFile:
  
  def __init__(self, json_file = 'personal_data.json'):
        self.file_path = Path(__file__).parent / json_file
        self.file_path.touch(exist_ok=True)  # Cria o arquivo, se não existir
    
  def write(self, data):
        try: 
            if self.file_path.exists() and self.file_path.stat().st_size > 0:
               with open(self.file_path, 'r', encoding='utf-8') as file:
                 content = json.load(file) 
            else:
               content = []

            if isinstance(data, dict):
               content.append(data)

            elif isinstance(data, list):
               content.extend(data)

            else:
               print("\033[91mErro: O dado precisa ser um dicionário ou uma lista.\033[m")
               return

       
            with open(self.file_path, 'w', encoding='utf-8') as file:
               json.dump(content, file, ensure_ascii=False, indent=4)

            print("\033[92mDados armazenados.\033[m")

        except Exception as erros:
            print(f"\033[91mErro ao salvar os dados: {erros}\033[m")


  def read_or_print(self, mode="ler", name=None):
    try:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)

        # Exibindo o conteúdo para o mode "imprimir"
        if content and mode == 'imprimir':
            if name:  
                person_found = None 

                for people in content:
                    if people.get('nome') == name:
                        person_found = people
                        break

                if person_found:
                    print("-" * 42)
                    print(f"Dados do usuário {name}:")
                    for key, value in person_found.items():
                        print(f"{key}: {value}")
                    print("-" * 42)
                else:
                    print(f"\033[91mErro: Nenhuma pessoa encontrada com o nome {name}.\033[m")
            else:
                # Caso não tenha nome, imprime todos os dados
                print("-" * 42)
                print("Dados dos Cadastrados do usuário:")
                for item in content:
                    for key, value in item.items():
                        print(f"{key}: {value}")
                print("-" * 42)

        # Se o conteúdo estiver vazio
        elif not content:
            if mode == "ler":
                print("\033[93mO arquivo está vazio.\033[m")
            elif mode == "imprimir":
                print("\033[93mNão há dados para imprimir.\033[m")

        return content

    except FileNotFoundError:
        print("\033[91mArquivo não encontrado.\033[m")
    except Exception as error:
        print(f"\033[91mErro ao ler o arquivo: {error}\033[m")


  def get_by_name(self, name):
    data = self.read_or_print()

    if not data:
        return None
    
    for people in data:
        if people.get('nome') == name:  # Usa .get() para evitar KeyError
            self.read_or_print("imprimir", name)
            return people 
    
    print(f"\033[91mNenhuma pessoa encontrada com o nome {name}.\033[m")
    return None

  def get_name(self, name):
    data = self.read_or_print()

    if not data:
        return None

    for people in data:
        if people.get('nome', '').lower() == name.lower():  # Usa .get() e ignora maiúsculas/minúsculas
            return people['nome']

    print(f"\033[91mNenhuma pessoa encontrada com o nome {name}.\033[m")
    return None

    
# Arquivo que manipula os dados das contas. / acesso pela agencia. 

    

            
