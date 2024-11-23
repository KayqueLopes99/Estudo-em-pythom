salas = [
   #   0        1
   ['Maria', 'Helena', ], # 0
   #   0
   ['Elaine', ], # 1
   #  0        1        2
   ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3])
print(salas[2][3][2])


for sala in salas: # percorrer a lista
    print(f'Sala: {sala}')
    for aluno in sala: # percorrer as sublisttas
        print(aluno)