# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 

# - Se ele ainda vai se alistar ao  serviço militar.

# - Se é a hora de se alistar 

# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.

ano = int(input('Informe o Ano do seu nascimento: '))

idade = 2024 - ano

print("Você tem {} Anos.".format(idade))

registro = str(input("\033[32mVocê deseja vê se pode se alistar no Serviço militar?\n Digite 'S' \033[m"))
if registro == 'S':
    print("Vamos ver!!!")
    if idade == 18:
        print("É a hora de se alistar ")
    elif idade < 18:
        falta = 18 - idade 
        print("Você ainda vai se alistar ao serviço militar. Faltam {} Anos". format(falta))
    else: 
        passou = idade - 18
        print("Já passou do tempo do alistamento. Passaram-se {} Anos". format(passou))
else:
    print("Invalido")
