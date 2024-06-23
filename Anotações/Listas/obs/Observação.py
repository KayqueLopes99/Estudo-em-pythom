# Se você igualar as listas, se mudar uma a outra muda.
a = [1,2,3,4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Podemos Criar uma Copia 
print("Copia no Ftaiamento")
d = [1,2,3,4]
c = d[:]# Recebe todos os itens da lista D.
c[2] = 8
print(f'Lista D: {d}')
print(f'Lista C: {c}')