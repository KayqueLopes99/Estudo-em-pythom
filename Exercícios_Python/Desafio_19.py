# O professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome de escolhido.
import random
aluno1 = str(input("Informe o nome: "))
aluno2 = str(input("Informe o nome: "))
aluno3 = str(input("Informe o nome: "))
aluno4 = str(input("Informe o nome: "))


print("O escolhido para limpar o quadro foi {}: ".format(random.choice([aluno1, aluno2, aluno3, aluno4])))