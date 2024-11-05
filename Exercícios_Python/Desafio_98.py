# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                    a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2                                                          c) uma contagem personalizada


from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
       passo *= -1 # o passo deve ser sempre positivo. 
    if passo == 0:
       passo = 1
    print("=== Começando ===")
    print(f"Contagem de {inicio} até {fim} em {passo} em {passo}:") 
    if inicio < fim:
       contador = inicio
       while contador <= fim:
          print(f"{contador} ", end='', flush=True)
          sleep(0.5)
          contador += passo

    else: 
       contador = inicio
       while contador >= fim:

         #flush para contar com segundos melhor.
        print(f"{contador} ", end='', flush=True)
        sleep(0.5)
        contador -= passo

    print("Fim!")
    print("-=-" * 15)

    
print("= Sistema de Contador =")
contador(1, 10, 1)
contador(10, 0, 2)

print(" === Personalizar === ")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
