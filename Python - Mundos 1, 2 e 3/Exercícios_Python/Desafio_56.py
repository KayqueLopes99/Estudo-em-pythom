media = 0
homem_velho = 0
qtd = 0
nome_homem_velho = ''

for i in range(1,3):
    Nome = str(input('Informe o seu Nome: '))
    Idade = int(input('Informe o sua Idade: '))
    Genero = int(input('Informe o seu Gênero:\n1 - Homem\n2 - Mulher\n'))
    media += Idade

    if Genero == 1 and Idade > homem_velho:
        homem_velho = Idade
        nome_homem_velho = Nome
    if Genero == 2 and Idade < 20:
        qtd += 1

media /= 4        
print("A média de idade é {}.".format(media))
print("O homem mais velho é {} com {} anos.".format(nome_homem_velho, homem_velho))
print('{} mulheres têm menos de 20 anos'.format(qtd))
