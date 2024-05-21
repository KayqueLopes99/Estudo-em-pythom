# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
número_tupla = ((int(input('Digite um número: '))), 
                (int(input('Digite um número: '))), 
                (int(input('Digite um número: '))),
                (int(input('Digite um número: '))),)
print(número_tupla)

contagem = número_tupla.count(9)
print(f'O valor 9 na Tupla {número_tupla} aparece {contagem} Vezes.')

indice = número_tupla.index(3)
if 3 in número_tupla:
    indice = número_tupla.index(3)
    print(f'O número 3 está na posição ou índice: {indice}')
else:
    print("O número 3 não foi encontrado na tupla.")

for c in número_tupla:
    if c % 2 == 0:
        print(f'Número Par: {c}')