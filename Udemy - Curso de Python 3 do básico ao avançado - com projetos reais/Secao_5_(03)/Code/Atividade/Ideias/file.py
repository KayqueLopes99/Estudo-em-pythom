from pathlib import Path

class Arquivo:
  def __init__(self, arquivo_conta='fluxo_de_dados.txt'):
        self.caminho_txt = Path(__file__).parent / arquivo_conta
        self.caminho_txt.touch(exist_ok=True)  # Cria o arquivo, se não existir


  def escrever_dados(self, dados):
    try:
        # Lê todas as linhas do arquivo
        if self.caminho_txt.exists():
            with open(self.caminho_txt, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
        else:
            linhas = []

        # Converte as linhas para dicionários e remove os dados da mesma pessoa
        novas_linhas = []
        nomes_a_remover = {dados['titular']} if isinstance(dados, dict) else {item['titular'] for item in dados}

        for linha in linhas:
            if any(f"titular: {nome}" in linha for nome in nomes_a_remover):
                continue  # Pula os dados antigos da pessoa
            novas_linhas.append(linha)

        # Abre o arquivo no modo de escrita ('w') para sobrescrever os dados
        with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(novas_linhas)  # Escreve os registros filtrados

            # Adiciona os novos dados
            if isinstance(dados, dict):
                linha = "; ".join(f"{chave}: {valor}" for chave, valor in dados.items())
                arquivo.write(linha + "\n")  
            elif isinstance(dados, list):
                for item in dados:
                    linha = "; ".join(f"{chave}: {valor}" for chave, valor in item.items())
                    arquivo.write(linha + "\n")  

        print("\033[92mDados armazenados com sucesso.\033[m")

    except Exception as erro:
        print(f"\033[91mErro ao salvar os dados: {erro}\033[m")


  def ler_ou_imprimir_dados(self, modo="ler"):
        try:
            # Verifica se o arquivo não está vazio antes de tentar ler
            if self.caminho_txt.stat().st_size > 0:
                with open(self.caminho_txt, 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.readlines()  # Lê as linhas do arquivo como uma lista de strings

                # Exibindo o conteúdo para o modo "imprimir"
                if conteudo and modo == 'imprimir':
                    print("-" * 42)
                    print("Dados dos Cadastrados do usuário:")
                    for linha in conteudo:
                        print(linha.strip())  # Remove quebras de linha extras
                    print("-" * 42)

                # Se o conteúdo estiver vazio, trata a mensagem de erro
                elif not conteudo:
                    if modo == "ler":
                        print("\033[93mO arquivo está vazio.\033[m")
                    elif modo == "imprimir":
                        print("\033[93mNão há dados para imprimir.\033[m")

            else:
                print("\033[93mO arquivo está vazio.\033[m")

            return conteudo

        except FileNotFoundError:
            print("\033[91mArquivo não encontrado.\033[m")
        except Exception as error:
            print(f"\033[91mErro ao ler o arquivo: {error}\033[m")
            
  def atualizar_saldo_limite(self, nome, novo_saldo=None, novo_limite=None):
    """
    Atualiza apenas as chaves 'saldo' e 'limite' de um usuário específico no TXT.

    :param nome: Nome do usuário cujo saldo e limite serão atualizados.
    :param novo_saldo: Novo valor do saldo (se for None, mantém o valor atual).
    :param novo_limite: Novo valor do limite (se for None, mantém o valor atual).
    :return: True se a atualização for bem-sucedida, False caso contrário.
    """
    try:
        # Lê todas as linhas do arquivo
        if not self.caminho_txt.exists() or self.caminho_txt.stat().st_size == 0:
            print("\033[91mErro: Nenhuma conta encontrada.\033[m")
            return False
        
        with open(self.caminho_txt, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        atualizado = False
        novas_linhas = []

        for linha in linhas:
            dados = dict(item.split(": ") for item in linha.strip().split("; "))

            if dados.get("titular", "").lower() == nome.lower():
                if novo_saldo is not None:
                    dados["saldo"] = str(novo_saldo)  # Atualiza saldo
                if novo_limite is not None:
                    dados["limite"] = str(novo_limite)  # Atualiza limite
                atualizado = True

            novas_linhas.append("; ".join(f"{chave}: {valor}" for chave, valor in dados.items()) + "\n")

        if not atualizado:
            print(f"\033[91mUsuário {nome} não encontrado.\033[m")
            return False

        # Reescreve o arquivo com os dados atualizados
        with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(novas_linhas)

        print(f"\033[92mSaldo e limite atualizados para {nome}.\033[m")
        return True

    except Exception as erro:
        print(f"\033[91mErro ao atualizar os dados: {erro}\033[m")
        return False
