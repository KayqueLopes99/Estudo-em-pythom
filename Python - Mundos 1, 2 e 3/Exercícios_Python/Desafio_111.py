# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from utilidadesCeV import moeda

Preço = float(input("\033[92mDigite o Preço: R$ \033[m"))
porcento = float(input("\033[95mDigite a porcentagem: \033[m"))
moeda.resumo(Preço, porcento, True)