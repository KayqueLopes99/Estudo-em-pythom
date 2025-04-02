"""
Exercício: Comparador de Idades
"""

print("\033[38;5;136m------- Comparador de Idades -------\033[m")
idade1 = input("Informe a idade da primeira pessoa: ")
idade2 = input("Informe a idade da segunda pessoa: ")

if idade1.isdigit() and idade2.isdigit():
    idade1 = int(idade1)
    idade2 = int(idade2)

    if idade1 > idade2:
        print("\033[92mA primeira pessoa é mais velha que a segunda.\033[m")
    elif idade1 < idade2:
        print("\033[92mA primeira pessoa é mais nova que a segunda.\033[m")
    else:
        print("\033[92mAs pessoas têm a mesma idade.\033[m")

else:
    print("\033[91mErro: Digite apenas números inteiros para a idade.\033[m")



