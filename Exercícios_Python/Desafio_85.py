# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

lista_oficio = list()
lista_par = []
lista_impar = []
# Ou 
# lista_oficio = [[], []]
for c in range(1,8):
    numero = int(input(f'Informe o {c}o. Número: '))
    if numero % 2 == 0:
        lista_par.append(numero)
        # Ou
        # lista_oficio[0].append(numero) na primeria sublista.
    else:
        lista_impar.append(numero)
        # Ou
        # lista_oficio[1].append(numero) na segunda sublista.
lista_impar.sort()
# Ou
# lista_oficio[1].sort
lista_par.sort()
# Ou
# lista_oficio[0].sort
lista_oficio.append(lista_par)
lista_oficio.append(lista_impar)
print("-="*30)
print(f" Está é a lista Organizada:\n{lista_oficio}")
print("-="*30)
print(f"Valores Pares {lista_oficio[0]}")
print(f"Valores Ímpares {lista_oficio[1]}")
print("-="*30)