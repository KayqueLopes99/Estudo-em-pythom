nome = str(input('Informe o seu nome de Treinador Pokémon: '))

print('Bem vindo Jovem Treinador {}!'.format(nome))

print("Pokémons: ")
print("1 - Pidgey")
print("2 - Starly")
print("3 - Fletchling")

poket = int(input('Escolha um Pokémon: '))

if poket == 1:
    print("Escolheu Pidgey!")
    print("informações:")
    print("Pidgey é um pokémon de Kanto, ele é eum pokémon ave pequeno e rechonchudo ")
    escolha = str(input("Deseja Evoluir digite S: "))
    if escolha == "S":
        print("Evoluiu para Pidgeotto")
        print("informações:")
        print("Pidgeotto é um pokémon de Kanto e é a evolução de Pidgey, Ele é coberto com penas marrons, tem um rosto, parte inferior e penas de vôo de cor creme.")
        escolha = str(input("Deseja Evoluir digite S: "))
        if escolha == "S":
            print("Evoluiu para Pidgeot")
            print("informações:")
            print("Pidgeot é um Pokémon dos tipos Normal e Voador, categorizado como Pokémon Pássaro e introduzido na Primeira Geração. É a forma evoluída de Pidgeotto e forma final de Pidgey.")
        else: 
            print("Desligado!")    
    else: 
        print("Desligado!")
elif poket == 2:
    print("Escolheu Starly!")
    print("informações:")
    print("Starly é um Pokémon dos tipos Normal e Voador, categorizado como Pokémon Pássaro Estrela e introduzido na Quarta Geração.")
    escolha = str(input("Deseja Evoluir digite S: "))
    if escolha == "S":
        print("Evoluiu para Staravia")
        print("informações:")
        print("Staravia é um Pokémon dos tipos Normal e Voador, categorizado como Pokémon Pássaro Estrela e introduzido na Quarta Geração. É a forma evoluída de Starly.")
        escolha = str(input("Deseja Evoluir digite S: "))
        if escolha == "S":
            print("Evoluiu para Staraptor")
            print("informações:")
            print("Staraptor é um Pokémon dos tipos Normal e Voador, categorizado como Pokémon Pássaro Predador e introduzido na Quarta Geração. É a forma final de Starly.")
        else: 
            print("Desligado!")
    else: 
        print("Desligado!")
elif poket == 3:
    print("Escolheu Fletchling!")
    print("informações:")
    print("Fletchling é um Pokémon dos tipos Normal e Voador, categorizado como Pokémon Pássaro Pequeno e introduzido na Sexta Geração.")
    escolha = str(input("Deseja Evoluir digite S: "))
    if escolha == "S":
        print("Evoluiu para Fletchinder")
        print("informações:")
        print("Fletchinder é um Pokémon dos tipos Fogo e Voador, categorizado como Pokémon Pássaro Em Chamas e introduzido na Sexta Geração. É a forma evoluída de Fletchling.")
        escolha = str(input("Deseja Evoluir digite S: "))
        if escolha == "S":
            print("Evoluiu para Talonflame")
            print("informações:")
            print("Talonflame é um Pokémon dos tipos Fogo e Voador, categorizado como Pokémon Pássaro Cimitarra e introduzido na Sexta Geração. É a forma final de Fletchling.")
        else: 
            print("Desligado!")
    else: 
        print("Desligado!")
