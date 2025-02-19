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
import time
caminho_arquivo = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_4_(02)\\Code\\Aula_56.txt"


def creation(caminho):
    if not os.path.exists(caminho): ## Ver se o Arquivo existe 
       with open(caminho, "w", encoding="utf-8") as arquivo:
         print("-"*35)
         print("\033[92mLista de Tarefas Criada!\033[m")
         print("-"*35)
        


def open_file_list(nome_arquivo):
    if not os.path.exists(nome_arquivo): 
        print("\033[91m[ERRO] -> O arquivo não existe.\033[m")
        return
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



def to_write(nome_arquivo):
    creation(nome_arquivo)
    tarefa = input("\033[95mAdicione Novas Tarefas: \033[m").strip()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo: 

        tarefas_existentes = [linha.strip() for linha in arquivo.readlines()]

    if tarefa not in tarefas_existentes:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
           arquivo.write(tarefa + '\n')
        print("\033[92mTarefa adicionada com sucesso!\033[m")
    else: 
        print("\033[93mEssa tarefa já foi adicionada antes!\033[m")

def unmake(nome_arquivo, tarefas_anteriores):
    try:
      with open(nome_arquivo, "r", encoding="utf-8") as arquivo: 
         tarefas = arquivo.readlines()
         if tarefas:
            tarefa_removida = tarefas.pop().strip()
            tarefas_anteriores.append(tarefa_removida)
                                      
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo: 
               arquivo.writelines(tarefas)
            print(f"\033[92mTarefa desfeita: {tarefa_removida}\033[m")

         else:
            print("\033[91mNenhuma tarefa para desfazer.\033[m")

    except FileNotFoundError:
       print("\033[91m[ERRO] -> O arquivo não foi encontrado para desfazer a tarefa.\033[m")


def remake(nome_arquivo, tarefas_anteriores):
   if not tarefas_anteriores:
        print("\033[91mNenhuma tarefa para refazer.\033[m")
        return
   
   tarefa_restaurada = tarefas_anteriores.pop()

   with open(nome_arquivo, "a", encoding="utf-8") as arquivo: 
      arquivo.write(tarefa_restaurada + "\n")
      print(f"\033[92mTarefa refeita: {tarefa_restaurada}\033[m")



creation(caminho_arquivo)
tarefas_anteriores = []

while True:
    print("-"*35)
    print("\033[94m==== Sistema de Tarefas ====\033[m")
    time.sleep(0.5)
    print("\033[94m[1] - Listar Tarefas.\033[m")
    time.sleep(0.5)
    print("\033[94m[2] - Adicionar Tarefa.\033[m")
    time.sleep(0.5)
    print("\033[94m[3] - Desfazer Tarefa especifica.\033[m")
    time.sleep(0.5)
    print("\033[94m[4] - Refazer Tarefa espacifica.\033[m")
    time.sleep(0.5)
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
        open_file_list(caminho_arquivo)      
    elif op_int == 2:
        to_write(caminho_arquivo)
    elif op_int == 3:
        unmake(caminho_arquivo, tarefas_anteriores)
    elif op_int == 4:
        remake(caminho_arquivo, tarefas_anteriores)
    else:
        print("\033[91mInforme uma Opção Correspondente ao Menu.\033[m")
        time.sleep(0.50)