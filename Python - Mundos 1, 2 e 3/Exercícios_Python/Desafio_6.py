# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input("Informe a primera nota\n"))
nota2 = float(input("Informe a segunda nota\n"))
nota3 = float(input("Informe a terceira nota\n"))
nota4 = float(input("Informe a quarta nota\n"))

media = (nota1 + nota2 +  nota3 + nota4)/4
print("Nota 1: {:.2f}".format(nota1))
print("Nota 2: {:.2f}".format(nota2))
print("Nota 3: {:.2f}".format(nota3))
print("Nota 4: {:.2f}".format(nota4))
print("A media: {:.2f}".format(media))