# Se um afrase é polindromo.
polindromo = str(input("Digite uma frase para verificar se ela é Palindromo: ")).lower() # MINUSCULA
polindromo = polindromo.replace(' ', '') # TRANSFORMAR

if polindromo == polindromo[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
