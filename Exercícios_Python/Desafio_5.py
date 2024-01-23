# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informação possiveís sobre ele

tipo_primitivo = input("Informe os dados para o senhor(a) saber seus subdados: ")
print(type(tipo_primitivo))
print("Tem numeros ?", tipo_primitivo.isnumeric())
print("Tem letras ?", tipo_primitivo.isalpha())
print("Tem decimais ?", tipo_primitivo.isdecimal())
print("Tem alfanumericos ?", tipo_primitivo.isalnum())
print("O identificador e valido em Python ?", tipo_primitivo.isidentifier())
print("Tem digitos ?", tipo_primitivo.isdigit())
print("Caracteres imprimiveis ?", tipo_primitivo.isprintable())
# true = v false = F
