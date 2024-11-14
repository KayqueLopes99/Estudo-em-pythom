nome = 'Kayque Lopes'
altura = 1.65
peso = 59
imc = peso / (altura * altura) 

linha_1 = f"Nome: {nome} Altura: {altura} Peso: {peso} IMC: {imc:.2f}"
print(linha_1)

print(f"Nome: {nome} Altura: {altura} Peso: {peso} IMC: {imc:.2f}")



## Outra forma
"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
