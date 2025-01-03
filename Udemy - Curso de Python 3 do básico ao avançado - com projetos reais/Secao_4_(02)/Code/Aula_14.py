import copy # Biblioteca para copi profunda e rasa.

dicionario_01 = {
    'chave_1': 1,
    'chave_2': 2,
    'chave_3': 3,
    'chave_4': [0, 1, 2],

}

dicionario_02 = dicionario_01.copy()

dicionario_02['chave_1'] = 1000
dicionario_02['chave_4'][1] = 99999 # muda em ambos.

print(dicionario_01)
print()
print(dicionario_02)