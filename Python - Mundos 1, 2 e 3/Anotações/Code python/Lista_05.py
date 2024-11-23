galera = [['joana', 24], ['allan', 19], ['leo', 22]]
print(galera)
print(galera[0])
print(galera[0][0])

gol = list()
tempo = list()

for c in range(0, 2):
    tempo.append(str(input("Nome: ")))
    tempo.append(int(input("Idade: ")))
    gol.append(tempo[:])
    tempo.clear()

print(gol)