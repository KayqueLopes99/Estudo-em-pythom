x = 1 # Está varíavel é global externo.

def escopo():
    # global x
    x = 10 # Está varíavel so funciona aqui, neste local interno.

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)