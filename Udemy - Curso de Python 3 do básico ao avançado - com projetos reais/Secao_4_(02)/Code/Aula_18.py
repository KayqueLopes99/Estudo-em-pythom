# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite uma Letra: ')
    if not letra.isalpha():
        print("Isso não é uma letra")
        continue
    else:
        letras.add(letra.lower())
    
    if 'l' in letras:
        print("Parabéns venceu!")
        break
    print(letras)