from pathlib import Path
import json
class Arquivo:
  def __init__(self, arquivo_json = 'fluxo_de_dados.json'):
        self.caminho_json = Path(__file__).parent / arquivo_json
        self.caminho_json.touch(exist_ok=True)  # Cria o arquivo, se não existir
    
  def escrever(self, dados):
        try: 
            if self.caminho_json.exists() and self.caminho_json.stat().st_size > 0:
               with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
                 conteudo = json.load(arquivo)  # Lê os dados existentes no arquivo JSON
            else:
               conteudo = []

            if isinstance(dados, dict):
               conteudo.append(dados)
            elif isinstance(dados, list):
               conteudo.extend(dados)
            else:
               print("\033[91mErro: O dado precisa ser um dicionário ou uma lista.\033[m")
               return

       
            with open(self.caminho_json, 'w', encoding='utf-8') as arquivo:
               json.dump(conteudo, arquivo, ensure_ascii=False, indent=4)

            print("\033[92mDados armazenados.\033[m")

        except Exception as erros:
            print(f"\033[91mErro ao salvar os dados: {erros}\033[m")

  def ler_ou_imprimir(self, modo="ler", nome=None):
    try:
        with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
            conteudo = json.load(arquivo)

        # Exibindo o conteúdo para o modo "imprimir"
        if conteudo and modo == 'imprimir':
            if nome:  # Se o nome foi fornecido, procura a pessoa específica
                pessoa_encontrada = None
                for pessoa in conteudo:
                    if pessoa.get('nome') == nome:
                        pessoa_encontrada = pessoa
                        break

                if pessoa_encontrada:
                    print("-" * 42)
                    print(f"Dados do usuário {nome}:")
                    for chave, valor in pessoa_encontrada.items():
                        print(f"{chave}: {valor}")
                    print("-" * 42)
                else:
                    print(f"\033[91mErro: Nenhuma pessoa encontrada com o nome {nome}.\033[m")
            else:
                # Caso não tenha nome, imprime todos os dados
                print("-" * 42)
                print("Dados dos Cadastrados do usuário:")
                for item in conteudo:
                    for chave, valor in item.items():
                        print(f"{chave}: {valor}")
                print("-" * 42)

        # Se o conteúdo estiver vazio
        elif not conteudo:
            if modo == "ler":
                print("\033[93mO arquivo está vazio.\033[m")
            elif modo == "imprimir":
                print("\033[93mNão há dados para imprimir.\033[m")

        return conteudo

    except FileNotFoundError:
        print("\033[91mArquivo não encontrado.\033[m")
    except Exception as error:
        print(f"\033[91mErro ao ler o arquivo: {error}\033[m")

        

  def acessar_dados_pelo_nome(self, nome):
        dados = self.ler_ou_imprimir()
        
        for pessoa in dados:

            if pessoa['nome'] == nome:
                self.ler_ou_imprimir("imprimir", nome)
                return pessoa 
        
        print(f"Nenhuma pessoa encontrada com o nome {nome}.")
        return None
    
  def obter_nome(self, nome):
       dados = self.ler_ou_imprimir()
    
    
       for pessoa in dados:
          if pessoa.get('nome') and pessoa['nome'].lower() == nome.lower():  # Usa `.get()` e ignora maiúsculas/minúsculas
            return pessoa['nome']
    
       print(f"\033[91mNenhuma pessoa encontrada com o nome {nome}.\033[m")
       return None

    

    

            
