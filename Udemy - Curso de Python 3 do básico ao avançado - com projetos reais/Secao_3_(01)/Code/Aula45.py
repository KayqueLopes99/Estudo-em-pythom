texto = 'Kayque' # iterável.
iteratador = iter(texto) # iterador

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# Principal.
# for letra in texto:
#    print(letra)