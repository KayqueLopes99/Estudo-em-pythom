# Exercício - Lista de tarefas com opções de desfazer e refazer

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
caminho_arquivo = "C:\\Users\\kaiqu\\OneDrive\\Imagens\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_4_(02)\\Code\\"

caminho_arquivo += 'Aula_56.txt'

def create_arq(caminho):
    if not os.path.exists(caminho): ## Ver se o Arquivo existe 
       with open(caminho, "w", encoding="utf-8") as arquivo:
         print("-"*35)
         print("\033[92mLista de Tarefas Criada!\033[m")
         print("-"*35)
    return 1


def open_arquivo_listar(nome_arquivo):
    try: 
      with open(nome_arquivo, "r", encoding="utf-8") as arquivo: 
        conteudo = arquivo.read()
        if not conteudo:
            print("\033[93m[A Lista de Tarefas está Vazia]\033[m")
            return

        print("-"*35)
        print("\033[92mLista de Tarefas Anotadas:\033[m")
        print(conteudo) 
        print("-"*35)

    except FileNotFoundError: 
        print("\033[91m[ERRO] -> O arquivo não existe.\033[m")

    return 1


def escrever(nome_arquivo):
    tarefa = input("\033[95mAdicione Novas Tarefas: \033[m").capitalize()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo: 

        tarefas_existentes = arquivo.readlines()


    for  in tarefas_existentes:
        tarefas_existentes = [t.strip()] # Retirar espaços. 

    if tarefa not in tarefas_existentes:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
           arquivo.write(tarefa + '\n')
           print("\033[92mTarefa adicionada com sucesso!\033[m")
    else: 
        print("\033[93mEssa tarefa já foi adicionada antes!\033[m")
    return 1


create_arq(caminho_arquivo)




while True:
    print("-"*35)
    print("\033[94m==== Sistema de Tarefas ====\033[m")
    print("\033[94m[1] - Listar Tarefas.\033[m")
    print("\033[94m[2] - Adicionar Tarefa.\033[m")
    print("\033[94m[3] - Desfazer Tarefa especifica.\033[m")
    print("\033[94m[4] - Refazer Tarefa espacifica.\033[m")
    print("\033[94m[0] - Sair do Sistema.\033[m")
    print("-"*35)
    op = input("\033[92mInforme uma opção do menu: \033[m")
    if not op.isdigit():
        print("\033[91m[ERRO] -> Informe um opção com valor numerico. \033[m")
        continue
    op_int = int(op)
    if op_int == 0:
        print("\033[92mSaindo do Sistema de Tarefas.\033[m")
        os.system("cls")
        break
    elif op_int == 1:
        if create_arq(caminho_arquivo) == 1:
            open_arquivo_listar(caminho_arquivo)      
        else: 
            print("\033[91mArquivo [NÃO] foi criado.\033[m")
    elif op_int == 2:
        escrever(caminho_arquivo)
    elif op_int == 3:
        print("Desfazer")

    elif op_int == 4:
        print("Refazer")
    
    else:
        print("\033[91mInforme uma Opção Correspondente ao Menu.\033[m")



