dicionario_01 = {
    'nome': 'Kayque',
    'sobrenome': 'Lopes',
}

print(dicionario_01['nome'])
print(dicionario_01.get('idade', 'Não existe'))


# nome = dicionario_01.pop('nome') # excluir.
# print (nome) 
# print(dicionario_01)

# ultima_chave = dicionario_01.popitem() # Excluir a ultima
# print(ultima_chave)
# print(dicionario_01)


# Maneiras de fazer Isto: 

dicionario_01.update({
    'nome': 'Novo Valor',
    'idade': 20,
})

dicionario_01.update(nome='Novo Valor', idade=20)

tupla = (('nome', 'Novo Valor'), ('idade', 20))

lista = [['nome', 'novo valor'], ['idade', 20]]
dicionario_01.update(lista)
print(dicionario_01)