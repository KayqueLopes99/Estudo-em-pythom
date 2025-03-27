from pathlib import Path
import json

class Arquivo:
    def __init__(self, arquivo_json = 'fluxo_de_dados.json'):
        self.caminho_json = Path(__file__).parent / arquivo_json
        self.caminho_json.touch(exist_ok=True)  # Cria o arquivo, se não existir
    


# varificar se o nome da pessoa existe
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


    def ler_ou_imprimir(self, modo="ler"):
        try:
            with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
                conteudo = json.load(arquivo)

            # Exibindo o conteúdo para o modo "imprimir"
            if conteudo and modo == 'imprimir':
                print("-" * 42)
                print("Dados do Cadastrados do usuário:")
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
                self.ler_ou_imprimir("imprimir")
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

    def remover_dados(self):
        ...

    

            

class Arquivo_Contas:
  def __init__(self, arquivo_json = 'dados_da_conta.json'):
        self.caminho_json = Path(__file__).parent / arquivo_json
        self.caminho_json.touch(exist_ok=True)  # Cria o arquivo, se não existir
    


# varificar se o nome da pessoa existe
  def escrever_conta(self, dados):
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

  def atualizar_saldo_limite(self, nome, novo_saldo=None, novo_limite=None):
    """
    Atualiza apenas as chaves 'saldo' e 'limite' de um usuário específico no JSON.
    
    :param nome: Nome do usuário cujo saldo e limite serão atualizados.
    :param novo_saldo: Novo valor do saldo (se for None, mantém o valor atual).
    :param novo_limite: Novo valor do limite (se for None, mantém o valor atual).
    :return: True se a atualização for bem-sucedida, False caso contrário.
    """
    dados = self.ler_ou_imprimir_conta()

    if not dados:
        print("\033[91mErro: Nenhuma conta encontrada.\033[m")
        return False

    for pessoa in dados:
        if pessoa['nome'].lower() == nome.lower():  # Ignora maiúsculas e minúsculas
            if novo_saldo is not None:
                pessoa['saldo'] = novo_saldo  # Atualiza o saldo
            if novo_limite is not None:
                pessoa['limite'] = novo_limite  # Atualiza o limite
            
            self.escrever_conta(dados)  # Salva as alterações no JSON
            print(f"\033[92mSaldo e limite atualizados para {nome}.\033[m")
            return True

    print(f"\033[91mUsuário {nome} não encontrado.\033[m")
    return False

  def ler_ou_imprimir_conta(self, modo="ler"):
      try:
        if self.caminho_json.exists() and self.caminho_json.stat().st_size > 0:
            with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
                conteudo = json.load(arquivo)
        else:
            conteudo = []  # Retorna uma lista vazia se o arquivo estiver vazio

        if not isinstance(conteudo, list):  # Garante que seja uma lista
            print("\033[91mErro: O arquivo JSON não contém uma lista válida.\033[m")
            return []

        return conteudo

      except FileNotFoundError:
        print("\033[91mArquivo não encontrado.\033[m")
      except json.JSONDecodeError:
        print("\033[91mErro ao decodificar JSON. O arquivo pode estar corrompido.\033[m")
      except Exception as error:
        print(f"\033[91mErro ao ler o arquivo: {error}\033[m")

      return []  # Garante retorno de lista vazia em caso de erro



    


  def acessar_dados_pelo_nome_conta(self, nome):
        dados = self.ler_ou_imprimir()
        
        for pessoa in dados:

            if pessoa['nome'] == nome:
                self.ler_ou_imprimir("imprimir")
                return pessoa 
        
        print(f"Nenhuma pessoa encontrada com o nome {nome}.")
        return None


            

