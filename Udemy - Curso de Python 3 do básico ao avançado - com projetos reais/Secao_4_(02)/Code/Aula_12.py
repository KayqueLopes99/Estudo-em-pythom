# Manipulando chaves e valores em dicionários

pessoa = {}
## Editar
chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

## Acessar
print(pessoa[chave])

## Criar
pessoa[chave] = 'Maria'

# Remover
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

## Verificar
# Se a chave existe !? 
# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')