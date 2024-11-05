# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
def somaPares(lista):
    soma = 0
    for par in lista:
        if par % 2 == 0:
            soma += par
    print(f"A soma dos Valores Pares: {soma}")
    

def sorteia(qtda):
    lista_de_numeros = []
    for i in range (qtda):
        numero = random.randint(1, 100)
        if numero not in lista_de_numeros:
            lista_de_numeros.append(numero)
    print(f"A lista de Valores: {lista_de_numeros}")
    somaPares(lista_de_numeros)
    

while True:
    print("*====* MENU *====*")
    resposta = int(input("\033[32m(1 - Começar)\n(0 - Finalizar)\n(RESPOSTA: ) \033[m"))

    if resposta == 1: 
        qtd = int(input("Informa a Quantidade de números: "))
        sorteia(qtd)
    elif resposta == 0:
        print("\033[91m Saindo... \033[m")
        break
    else: 
        print("\033[91m ERRO... \033[m")