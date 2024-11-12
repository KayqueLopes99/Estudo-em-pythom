# Reaização de testes

frase = 'Agua Fogo Terra Ar'

print(frase)

numero = int(input("Informe o indice para imprimir a letra correspondente: "))

print(frase[numero])

numero1 = int(input("Informe o primero indice para imprimir a sequencia de letras correspondentes: "))

numero2 = int(input("Informe o primero indice para imprimir a sequencia de letras correspondentes: "))

print(frase[numero1:numero2])

numero3 = int(input("Informe o primero indice para imprimir a sequencia de letras correspondentes: "))

numero4 = int(input("Informe o primero indice para imprimir a sequencia de letras correspondentes: "))

numero5 = int(input("Informe o salto: "))
print(frase[numero3:numero4:numero5])

print('Contagem de letra G')
print(frase.upper().count('G'))

print('Contagem de letras:')
print(len(frase))

print('Tranformar: ')
print(frase.replace('Ar', 'Voador'))

print("Verificar a palavra está dentro da frase")
print(frase.find("Fogo"))

print("Verificar a palavra está dentro da frasee transformação: ")
print(frase.lower().find("fogo"))

print("Cria Lista:")
print(frase.split())

dividido = (frase.split())
# Na palavra vídeo teremos a terceira letra.
print(dividido[2][3])