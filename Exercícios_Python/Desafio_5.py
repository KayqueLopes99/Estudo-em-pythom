# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informação possiveís sobre ele

tipo_primitivo = input("Informe os dados para o senhor(a) saber seus subdados: ")
print(type(tipo_primitivo))
print(tipo_primitivo.isnumeric())
print(tipo_primitivo.isalpha())
print(tipo_primitivo.isdecimal())
print(tipo_primitivo.isalnum())
print(tipo_primitivo.isidentifier())
print(tipo_primitivo.isdigit())
print(tipo_primitivo.isprintable())
# true = v false = F