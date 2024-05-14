# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# [0] -> pegar a primeira letra.
genero = str(input("Informe seu Gênero:\nM = Masculino \nF = Feminino\n")).strip().upper()[0]

while genero not in 'MmFf':
    genero = str(input("Informe um caractere válido:\nM = Masculino \nF = Feminino\n")).strip().upper()[0]
print("Gênero: {}".format(genero))

