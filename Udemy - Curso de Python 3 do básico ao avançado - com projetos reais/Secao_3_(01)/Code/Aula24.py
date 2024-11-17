nome = 'Kayque'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[-3])
print(nome[-2])
print(nome[-1])

print("-" * 10)

print('que' in nome) # True
print('Ky' in nome) # False
print("-" * 10) 
print('que' not in nome) # False
print('Ky' not in nome) # True

nome = input("Digite seu nome: ")
encontrar = input("Digite o ue deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está no seu Nome {nome}.")
else:
    print(f"{encontrar} não está em {nome}")

