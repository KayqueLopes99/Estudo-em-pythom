#  Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
lista1 = list()
lista2 = list()
lista3 = list()
lista_Oficial = []
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
    for coluna in range(0,3):
      print(f"[{lista_Oficial[linha][coluna]:^5}]", end='')
    print()

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
  for c in range(0, 3):
     matriz [l] [c] = int(input(f'Digite um valor para [{1}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print('{[matriz[l][c]:^5}]', end='')
    print() 
'''