# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                               
# A) A soma de todos os valores pares digitados.                                                      
# B) A soma dos valores da terceira coluna.                                 
# C) O maior valor da segunda linha.
lista1 = list()
lista2 = list()
lista3 = list()
lista_Oficial = []
soma = soma1 = soma2 = soma3 = soma_terceira_coluna = 0
maior = menor = 0
for i in range(3):
    numero1 = int(input(f"Informe um número para posição [{0},{i}]: "))
    lista1.append(numero1)
    
    
for i in range(3):
    numero2 = int(input(f"Informe um número para posição [{1},{i}]: "))
    lista2.append(numero2)
    

for i in range(3):
    numero3 = int(input(f"Informe um número para posição [{2},{i}]: "))
    lista3.append(numero3)
   

lista_Oficial.append(lista1)
lista_Oficial.append(lista2)
lista_Oficial.append(lista3)

for linha in range(0,3):
    soma_terceira_coluna += lista_Oficial[linha][2]



for i in lista2:
    if i == 0:
        menor = maior = numero2
    else:
        if numero2 > maior:
            maior = numero2
        elif numero2 < menor:
            menor = numero2
# Ou 
# for c in range(0,3):
#    if c == 0 or lista_oficial[1][c] > maior:
#       maior = lista_oficial[1][c] 





soma = soma1 + soma2 + soma3
print("-="*30)
for linha in range(0,3):
    for coluna in range(0,3):
      print(f"[{lista_Oficial[linha][coluna]:^5}]", end='')
      if lista_Oficial[linha][coluna] % 2 == 0:
          soma += lista_Oficial[linha][coluna]
    print()

print("-="*30)
print(f"A Soma de Todos os Números Pares da Matriz: {soma}")
print(f"A Soma de Todos os Números da Terceira Coluna: {soma_terceira_coluna}")
print(f"O maior valor da Segunda Linha: {maior}")
print("-="*30)