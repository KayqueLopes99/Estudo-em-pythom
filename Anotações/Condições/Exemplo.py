print("Bem vindo ao Sistema pokémon:")

print('1 - Bubasaur\n2 - Chamander\n3 - Squirtle\n')
Pokemon = int(input('Qual pokémon você vai escolher? '))

if Pokemon == 1:
    print("Bubasaur escolhido")
elif Pokemon == 2:
    print("Chamander escolhido")
elif Pokemon == 3:
    print("Squirtle escolhido")
else:
    print("Pokémon errado!")

ataques = Pokemon
dano = 0
nome = 0
if ataques == 1:
    print("Bubasaur")
    print("Chicote de Cipó - 20 de dano.")
    dano = 20
    nome = "Chicote de Cipó"
elif ataques == 2:
    print("Chamander")
    print("Brasa - 15 de dano.")
    dano = 15
    nome = "Brasa"
elif ataques == 3:
    print("Squirtle")
    print("Bolha - 15 de dano.")
    dano = 10
    nome = "Bolha"
else: 
    print("Pokémon errado!")

ratata = 20
print("Hora da Batalha!")
print("Ratata apareceu!")
print("Vá {}!".format(Pokemon))
print("Use {}".format(nome))
print("Ratata sofrer {} de dano!".format(dano))
if dano == 20:
    print("Ratata perdeu!")
    print("Vitória")
elif dano <= 20:
    print("Ratata usou Hiper mordida!")
    print("Derrota!")
