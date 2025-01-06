# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis 
# Mutáveis [] {} set()
# Imutáveis {} "" 0 0.0 None False range(0, 10)
list = []
dictionary = {}
conjunto_set = set()
tuple = ()
string = ''
inteiro_whole = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def funcion_falsy(valor):
    return 'Falsy' if not valor else 'Truthy'

print(f"Teste", funcion_falsy('Teste'))
print(f'{list=}', funcion_falsy(list))
print(f'{dictionary=}', funcion_falsy(dictionary))
print(f'{conjunto_set=}', funcion_falsy(conjunto_set))
print(f'{tuple=}', funcion_falsy(tuple))
print(f'{inteiro_whole=}', funcion_falsy(inteiro_whole))
print(f'{flutuante=}', funcion_falsy(flutuante))
print(f'{falso=}', funcion_falsy(falso))
print(f'{intervalo=}', funcion_falsy(intervalo))