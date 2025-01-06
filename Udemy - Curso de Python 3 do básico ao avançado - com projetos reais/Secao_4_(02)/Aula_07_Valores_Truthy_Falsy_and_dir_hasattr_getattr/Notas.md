## Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
+ **valores "Truthy"**: São valores que, mesmo não sendo `True`, o Python interpreta como verdadeiros. 

- Qualquer número diferente de zero (1, -5, 3.14, etc.)
- Strings não vazias ('Hello', "Python", etc.)
- Listas não vazias ([1, 2, 3])
- Dicionários não vazios ({'a': 10})
- Tuplas não vazias ((10, 20))
- Conjuntos não vazios ({1, 2, 3})

+ **valores "Falsy"**: São valores que, mesmo não sendo `False`, o Python interpreta como falsos.  

-None (valor nulo)
- False (o próprio booleano falso)
- 0 ou 0.0 (zero de qualquer tipo: int, float, complex)
- '' (string vazia)
- [] (lista vazia)
- {} (dicionário vazio)
- set() (conjunto vazio)
- () (tupla vazia)
- range(0) (intervalo vazio)


+ Nem tudo precisa ser exatamente `True` ou `False` para ser usado como verdadeiro ou falso. Alguns valores são tratados (Truthy) ou (Falsy) quando usados em condições (`if`, `while`, etc.).  

```python
nome = input("Digite seu nome: ") or "Usuário Anônimo"
print(nome)
```
```py
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
```