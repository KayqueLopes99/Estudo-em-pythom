pessoa = {
    'Nome': 'José Kayque',
    'Sobrenome': 'Lopes',
    'Idade': 20,
    'altura': 1.7,

# - Lista - 
    'Endereços': [
        {'Rua': 'Zona Rural', 'Número': 230},
        {'Graduação': 'Tecnologia da Informação', 'Matricula': 2023011415}
    ],

}

# print(pessoa, type(pessoa))
# pessoa = dict(nome='KAYQUE')
print(pessoa["Nome"])
print(pessoa["Sobrenome"])
print()

for chave in pessoa:
    print(chave, pessoa[chave])