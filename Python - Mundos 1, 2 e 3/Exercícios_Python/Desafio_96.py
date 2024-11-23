# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(Largura, Comprimento):
    Terreno = (Largura * Comprimento)
    print(f"O Terreno Ratangular {Largura}x{Comprimento} Tem Uma Área de: {Terreno} Metros Quadrados.")



print("===== Controle De Terrenos =====")
Largura = float(input("Informe a  Largura (m): "))
Comprimento = float(input("Informe o Comprimento (m): "))
area(Largura, Comprimento)