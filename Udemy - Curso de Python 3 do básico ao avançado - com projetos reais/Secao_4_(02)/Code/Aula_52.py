def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    # Caso base
    if inicio >= fim:
        return fim
    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)
print(recursiva())


def fatctorial(number):
    if number == 0:
        return 1
        

    return number * fatctorial(number - 1)

print(fatctorial(10))