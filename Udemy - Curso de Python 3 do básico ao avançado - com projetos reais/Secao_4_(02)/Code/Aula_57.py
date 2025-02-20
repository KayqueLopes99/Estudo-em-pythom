import os
import json

CAMINHO = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_4_(02)\\Code\\Aula_57.json"
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


## Json: 
def ler(tarefas, caminho):
    dados = []
    try:
     with open(caminho, 'r', encoding='utf8') as arquivo:
         dados = json.load(arquivo)
    except FileExistsError:
        print("Arquivo não existe.")
        salvar(tarefas, caminho)
    return dados

def salvar(tarefas, caminho):
    dados = tarefas
    with open(caminho, 'w', encoding='utf8') as arquivo:
         dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados
    



tarefas = ler([], CAMINHO) # Json
tarefas_refazer = []

while True:
    salvar(tarefas, CAMINHO) # Json
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    elif tarefa == 'sair':
        break
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue