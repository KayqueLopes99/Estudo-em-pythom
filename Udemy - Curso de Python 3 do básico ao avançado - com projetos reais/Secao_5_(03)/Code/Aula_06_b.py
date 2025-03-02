# Nesta parte A o arquivo cria instâncias com os dados do json.
import json
from Aula_06_a import CAMINHO, Poket_monsters

with open(CAMINHO, "r") as arquivo:
    dados = json.load(arquivo)
print("Dados retornados do arquivo.json!")


## Criando instâncias a partir do json
for pokemon in dados:
    name_from_dados = pokemon['name']
    num_from_dados = pokemon['num']
    d = Poket_monsters(name_from_dados, num_from_dados)
    print(d.print())
   