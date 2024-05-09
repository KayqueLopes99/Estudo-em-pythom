# Crie um programa que faça o computador jogar Jokempô com você
import random
print("\033[33m ++++++++ \033[m")
print("1- Papel.")
print("2 -Tesoura.")
print("3 - Pedra.")
escolha = int(input('Escolha para o Jokempô: '))


computador = random.choice(['papel', 'tesoura', 'pedra'])

print("Computador escolhe: {}".format(computador))


if escolha == 1 and computador == 'papel':
    print("\033[34mEmpate. \033[m")
elif escolha == 1 and computador == 'tesoura':
    print("\033[34mVocê Perdeu para o Computador.\033[m")
elif escolha == 1 and computador == 'pedra':
    print("\033[34mComputador Perdeu para você. \033[m")

elif escolha == 2 and computador == 'tesoura':
    print("\033[34mEmpate. \033[m")

elif escolha == 2 and computador == 'papel':
    print("\033[34mComputador Perdeu para você. \033[m")

elif escolha == 2 and computador == 'pedra':
    print("\033[34mVocê Perdeu para o Computador.\033[m")

elif escolha == 3 and computador == 'pedra':
    print("\033[34mEmpate. \033[m")

elif escolha == 3 and computador == 'tesoura':
    print("\033[34mVocê Perdeu para o Computador.\033[m")
elif escolha == 3 and computador == 'papel':
    print("\033[34mComputador Perdeu para você. \033[m")
else: 
    print("Invalido.")