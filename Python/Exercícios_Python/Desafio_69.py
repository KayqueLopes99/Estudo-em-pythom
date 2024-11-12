# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
qtd_homem = qtd_mulher = qtd = 0

while True:
    IDADE = int(input('Informe a Idade da Pessoa:'))
    sexo = str(input('Informe o seu Sexo [M/F]')).upper().strip()[0]
    escolha = int(input('Deseja Sair:\n1 - Sim\n2 - Não\nResposta: '))
    
    if IDADE > 18:
        qtd += 1
    if sexo == 'M':
        qtd_homem += 1
    if sexo == 'F' and IDADE < 20:
        qtd_mulher += 1
 
    if escolha == 1:
        print("Saiu.")
        break
print("-"*50)
print(f'{qtd} Pessoas têm mais de 18 anos.')
print("-"*50)
print(f'{qtd_homem} Homens cadastrados.')
print("-"*50)
print(f'{qtd_mulher} Mulheres com menos de 20 anos.')
print("-"*50)