from pathlib import Path
import json


class ArquivoConta:
    def __init__(self, arquivoTxt = 'dadosContas.txt'):
        self.caminhoTxt = Path(__file__).parent / arquivoTxt
        self.caminhoTxt.touch(exist_ok=True)  # Cria o arquivo, se não existir
    
    
# varificar se o nome da pessoa existe pelo CPFFFFF
    def escrever(self, cpf, titular, agencia, saldo, tipoConta):
        try:
            nova_linha = f"{cpf};{titular};{agencia};{saldo};{tipoConta}\n" # < -------

            # Lê todas as linhas do arquivo
            with open(self.caminhoTxt, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()

            # Verifica se a pessoa já existe e atualiza se necessário
            atualizou = False
            for i, linha in enumerate(linhas):
                if linha.startswith(f"{cpf};"):
                    linhas[i] = nova_linha
                    atualizou = True
                    break

            if not atualizou:
                linhas.append(nova_linha)
                

            # Reescreve o conteúdo atualizado no arquivo
            with open(self.caminhoTxt, 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(linhas)

        except Exception as erro:
            print(f"\033[91mErro ao salvar os dados: {erro}\033[m")


    def imprimir(self):
        try:
            # Lê todas as linhas do arquivo
            with open(self.caminhoTxt, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.readlines()

            print("-" * 42)
            print("Dados Cadastrados dos Usuários:")
            indice = 1  
            for item in conteudo:
                dados = item.strip().split(';')
                print(f"[{indice}] - Cpf: {dados[0]} | Titular: {dados[1]} | Agência: {dados[2]} | Saldo: {dados[3]} | Tipo de Conta: {dados[4]}")
                indice += 1
            print("-" * 42)
# 123456789;João;1234;1300.0;Conta Poupança

            # Se o conteúdo estiver vazio
            if not conteudo:
                    print("\033[93mNão há dados para imprimir.\033[m")

        except FileNotFoundError:
            print("\033[91mArquivo não encontrado.\033[m")
        except Exception as error:
            print(f"\033[91mErro ao ler o arquivo: {error}\033[m")

    
    def ler(self, cpf):
        try:
            # Lê todas as linhas do arquivo
            with open(self.caminhoTxt, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.readlines()

            for i, linha in enumerate(conteudo):
              if linha.startswith(f"{cpf};"):
                dados = linha.strip().split(';')
                return dados
    

        except FileNotFoundError:
            print("\033[91mArquivo não encontrado.\033[m")
        except Exception as error:
            print(f"\033[91mErro ao ler o arquivo: {error}\033[m")
         


# Implementar. 
class ArquivoPessoa:
    ...