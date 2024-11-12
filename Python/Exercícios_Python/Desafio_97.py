# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.     
def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print("-"*tamanho)
    print(f"  {mensagem}")
    print("-"*tamanho)


print(" === Sistema De Tamanho de Mensagens === ")

escreva("Olá, Mundo!")
escreva("Pokémon é legalllll")