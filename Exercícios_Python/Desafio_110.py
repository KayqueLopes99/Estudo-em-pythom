# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from Desafios_arquivos import moeda109

Preço = float(input("\033[92mDigite o Preço: R$ \033[m"))
porcento = float(input("\033[95mDigite a porcentagem: \033[m"))
moeda109.resumo(Preço, porcento, True)