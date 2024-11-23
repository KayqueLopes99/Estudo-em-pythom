# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informação possiveís sobre ele

tipo_primitivo = input("Informe os dados para o senhor(a) saber seus subdados: ")
print(type(tipo_primitivo))
print("\033[36mTem numeros ?\033[m", tipo_primitivo.isnumeric())
print("\033[36mTem letras ?\033[m", tipo_primitivo.isalpha())
print("\033[36mTem decimais ?\033[m", tipo_primitivo.isdecimal())
print("\033[36mTem alfanumericos ?\033[m", tipo_primitivo.isalnum())
print("\033[36mO identificador e valido em Python ?\033[m", tipo_primitivo.isidentifier())
print("\033[36mTem digitos ?\033[m", tipo_primitivo.isdigit())
print("\033[36mCaracteres imprimiveis ?\033[m", tipo_primitivo.isprintable())
# true = v false = F
