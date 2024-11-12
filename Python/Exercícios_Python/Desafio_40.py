# Crie um programa que leia duas  notas de um aluno e calcule sua média, mostarndo uma mensagem no final, de acordo com a média atingindo:

Nota1 = float(input("Informe sua Primeira Nota: "))
Nota2 = float(input("Informe sua Segunda Nota: "))
Nota3 = float(input("Informe sua Terceira Nota: "))

media = (Nota1 + Nota2 + Nota3)/3

if media < 5.0:
    print("\033[31mReprovado\033[m")
elif media >= 5.0 and media <= 6.9:
    print("\033[35m Recuparação \033[m")
else: 
    print("\033[32m Aprovado \033[m")