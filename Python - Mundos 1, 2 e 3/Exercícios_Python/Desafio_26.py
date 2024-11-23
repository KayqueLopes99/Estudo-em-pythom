# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = str(input('Escreva: ')).title()
print(frase)
print("Quantidade de vezes: ")
print(frase.count("A"))

print('Primeira ocorrencia: ')
print(frase.find("A"))  

print('Ultima ocorrencia: ')
print(frase.rfind("A"))  
# r para direita.
