from random import randint
from time import sleep
from operator import itemgetter
Ranking = list()
Jogadores = {
    'Jogador1': randint(1,100),
    'Jogador2': randint(1,100),
    'Jogador3': randint(1,100),
    'Jogador4': randint(1,100),
             
}
Ranking.append(Jogadores)
print("="*45)
print("================= Jogadores =================")
for jogador in Ranking:
    for chave, valor in jogador.items():
        print(f"O Jogador {chave} tirou {valor} no Dado.")
        sleep(1)
        
print("-=" * 40)
# Ordena o ranking com base nos valores (números aleatórios) presentes nas chaves Números em cada diconario na lista.
#  para acessar o valor associado à chave 'Número' em cada jogador.
Ranking = sorted(Jogadores.items(), key=itemgetter(1), reverse=True)

print("============= RANKING DOS JOGADORES ==============")
# Trando como uma lista, enumeramos, como ele é uma tupla dentro de uma lista.
for i, valor in enumerate(Ranking):
    print(f"{i + 1}º lugar o Jogador {valor[0]}: {valor[1]}")
    sleep(1)
print("-=" * 40)

## Ordenação com Sorted, necessita criar um dicionario, colocando os items()
## Biblioteca Itemgetter().
# O comando Itemgetter(0) - Ordem de Chaves.
# O comando Itemgetter(1) - Ordem de Valor.
# Usamos reverse=True para colocar em ordem decrecente.
