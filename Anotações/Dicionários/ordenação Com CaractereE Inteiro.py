import random
from time import sleep
from operator import itemgetter

Ranking = dict()
Dicionario_ordenado = list()
for i in range(0,4):
    nome = str(input(f"Informe o Nome do {i+1}º Jogador: "))
    nomero = random.randint(1,100)

    Jogadores = {
        'Nome': nome,
        'Número': nomero
    }
    Ranking[nome] = Jogadores


print("="*45)
print("================= Jogadores =================")
for nome, Jogadores in Ranking.items():
        print(f" O Jogador {Jogadores['Nome']} jogou o dado e obteve o resultado: {Jogadores['Número']}")
        sleep(1)
        ''' Explicação: 
        key=lambda x: x[1]['Número']: Aqui, estamos especificando uma função lambda (anônima) que extrai o valor associado à chave 'Número' de cada tupla. Isso significa que a ordenação será feita com base nos números gerados pelos jogadores.
        '''
print("-=" * 40)

Dicionario_ordenado = sorted(Ranking.items(), key=lambda x: x[1]['Número'], reverse=True)

print("============= RANKING DOS JOGADORES ==============")
for indice, valor in enumerate(Dicionario_ordenado):
    print(f"{indice + 1}º lugar: {valor[0]} com {valor[1]['Número']}")
    sleep(1)
print("-=" * 40)
## Ordenação com Sorted, necessita criar um dicionario, colocando os items()
## Biblioteca Itemgetter().
# O comando Itemgetter(0) - Ordem de Chaves.
# O comando Itemgetter(1) - Ordem de Valor.
# Usamos reverse=True para colocar em ordem decrecente.
