from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = dado.leiaDinheiro("\033[92mDigite o Preço: R$ \033[m")
porcento = float(input("\033[95mDigite a porcentagem: \033[m"))
moeda.resumo(valor, porcento, True)

