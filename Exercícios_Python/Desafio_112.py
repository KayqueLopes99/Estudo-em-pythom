# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários
from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = dado.leiaDinheiro("\033[92mDigite o Preço: R$ \033[m")
porcento = float(input("\033[95mDigite a porcentagem: \033[m"))
moeda.resumo(valor, porcento, True)

