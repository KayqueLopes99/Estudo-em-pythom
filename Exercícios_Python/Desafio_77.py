# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
Tupla_pokemon = ('Bubasaur', 'Squitle', 'Chamander', 'Pikachu', 'Zubat', 'Ditto', 'Mew', 'Pidgey', 'Muk', 'Dragonite', 'Moltres', 'Articuno', 'Zaptos')
vogais = 'aeiou' ## Para melhor
for palavra in Tupla_pokemon:
    print(f'\nNa Palavra {palavra} Temos: ', end='')
    # Rastrear Vogais. 
    for letra in palavra:
        # Lower para minuscula.
        if letra.lower() in vogais:
            print(letra, end='  ')

