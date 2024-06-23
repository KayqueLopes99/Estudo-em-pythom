temp = []
princ = []

while True:
    # APPEND COM INSERÇÃO.
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    princ.append(temp[:])# Colocamos pois colocamos uma copia da lista temp na oficial e depois com clear descartamos ela na lista temp.
    temp.clear()
    resp = str(input("Quer continuar? [s/n]"))
    # Se está na resposta.
    if resp in 'Nn':
        break
print(f"Os Dados foram {princ}")