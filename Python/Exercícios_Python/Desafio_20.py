# Ordem de apresentação 
import random

aluno1 = str(input("Informe o nome: "))
aluno2 = str(input("Informe o nome: "))
aluno3 = str(input("Informe o nome: "))
aluno4 = str(input("Informe o nome: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("Ordem de apresentação:")
print("O escolhido para apresentar 1: {}".format(alunos[0]))
print("O escolhido para apresentar 2: {}".format(alunos[1]))
print("O escolhido para apresentar 3: {}".format(alunos[2]))
print("O escolhido para apresentar 4: {}".format(alunos[3]))

