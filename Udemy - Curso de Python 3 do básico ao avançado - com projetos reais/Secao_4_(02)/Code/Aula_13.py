pessoa = {
    'nome': 'José Kayque',
    'sobrenome': 'Lopes',
    'idade': 20,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)