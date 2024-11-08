from Desafios_arquivos import moeda109
from time import sleep
import os

Preço = float(input("\033[92mDigite o Preço: R$ \033[m"))
porcento = float(input("\033[95mDigite a porcentagem: \033[m"))
moeda109.resumo(Preço, porcento, True)