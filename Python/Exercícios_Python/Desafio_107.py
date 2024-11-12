from Desafios_arquivos import moeda

preço = float(input("\033[92mDigite o Preço: R$ \033[m"))
porcento = float(input("\033[95mDigite a porcentagem:  \033[m"))
print(f'\033[91mA Metade de {preço}:\033[m R$ {moeda.metade(preço)}')
print(f'\033[93mO Dobro de {preço}:m\033[m R$ {moeda.dobra(preço)}')
print(f'\033[94mO Aumentando {porcento}% de {preço}:\033[m R$ {moeda.aumentar(preço, porcento)}')
print(f'\033[96mO Diminuindo {porcento}% de {preço}:\033[m R$ {moeda.diminuir(preço, porcento)}')


