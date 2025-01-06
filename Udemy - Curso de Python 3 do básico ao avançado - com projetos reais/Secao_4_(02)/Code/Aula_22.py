a, b = 1, 2
a, b = b, a

# Empacotarmento
"""
var_a, var_b = pessoa.keys()
print(var_a, var_b)
var_a, var_b = pessoa.values()
print(var_a, var_b)
var_a, var_b = pessoa.items()
print(var_a, var_b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
# Ou
for chave, valor in pessoa.items():
    print(chave, valor)
"""


pessoa = {
    'nome': 'Kayque',
    'sobrenome': 'Lopes',
}


dados_pessoa = {
    'idade': 20,
    'altura': 1.70,
}


# Desempacotamento do dicionario.
# Juntar-los, criamos um terceiro e extraímos os valores de cada colocando neste. 
# Podemos adicionar informações
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)


# Empacotando
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print("Nomeados:", chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# Desempacotando - Para não colocar todas as variaveis escritas.
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)
