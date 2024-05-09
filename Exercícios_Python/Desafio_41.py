# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:


ano = int(input('Informe o Ano do seu nascimento: '))

idade = 2024 - ano

print("Você tem {} Anos.".format(idade))

if idade <= 9:
    print("\033[33m Categoria Mirim.\033[m")
elif idade > 9 and idade <= 14:
    print("\033[33m Categoria Infantil.\033[m")
elif idade > 14 and idade <= 19:
    print("\033[33m Categoria Junior.\033[m")
elif idade == 20:
    print("\033[33m Categoria Sénior.\033[m")
else:
    print("\033[33m Categoria Master.\033[m")