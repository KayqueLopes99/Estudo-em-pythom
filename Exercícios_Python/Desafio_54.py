# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
qtdMaiores = 0
qtdMonores = 0
for i in range(1,8):
    pessoa = int(input('Informe o Ano de nascimento da {} pessoa: '.format(i))) 
    ano = 2024 - pessoa
    if ano >= 18:
        qtdMaiores += 1
        print("Pessoa com ano {} é maior de idade.".format(pessoa))
    else:
        qtdMonores += 1
        print("Pessoa com ano {} é menor de idade.".format(pessoa))
print("Quandidade de maiores de idade: {}".format(qtdMaiores))
print("Quandidade de Menores de idade: {}".format(qtdMonores))