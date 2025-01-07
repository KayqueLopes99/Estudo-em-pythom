## Introdução às Generator functions em Python
- Generator: Funções que sabem pausar em determinado ponto. 
- É uma forma compacta de criar **geradores**, parecida com as **List Comprehensions**, mas sem criar toda a lista na memória. 
```python
generator = (expressão for item in iterável if condição)
```
- `yield valor`: Parece o return, o diferencial que ele vai pausar a execução da função e guarda o valor no next, retornando o valor. 
- Usado em funções de generator.
- É um iterator pelo uso do next e `__iter__`.
o `return` pós `yield` dentre da Generator function ele trabalha como `levanta uma e exception ta tela`, expodo o valor que foi retornado. `Traceback ... StopIteration: Valor_retonado`.
- Pode-se ter vários `yield valor`

```py
def generator(n=0):
    yield 1 # Pausar
    print("Continuando...")
    yield 2 # Pausar
    print("Mais uma...")
    yield 3 # Pausar
    print("Vou terminar...")
    return 'ACABOU'


gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

## Ou

for n in gen:
    print(n)
```

- Pausar while com `yield valor`.
- **A execução no Geral** vai do inicio da função para sequencia dos demais comando dentro dela, de um yield para outro, até chegar no return. 

```py
# Temos um range generator
def funcion_generator(start=0, end=100):
    while True:
        yield start
        start += 1

        if start >= end:
            
            return 'End'
        
generator_variable = funcion_generator(end=150)
for traverse in generator_variable:
    print(traverse)
```

## yield from em generator functions
- Código com ordem ele é perfeito.
- yield	Retorna um valor por vez yield x.
- yield from	Retorna todos os valores de um iterável sem precisar de um loop	yield from lista.

+ `yield from`
- Quando usamos yield from, estamos dizendo que um gerador pode chamar outro gerador ou iterável diretamente, sem precisar de um loop for.

- Isso é útil quando temos múltiplos geradores e queremos combiná-los sem complicar o código.
```py
def generator_01():
    print("Start 01")
    yield 1
    yield 2
    yield 3
    print("End 01")


def generator_03():
     print("Start 03")
     yield 7
     yield 8
     yield 9
     print("End 03")
    


def generator_02(gen=None): # Parametro padrão
    print("Start 02")
    if gen is not None:
        yield from gen

    yield 4
    yield 5
    yield 6
    print("End 02")

g1 = generator_02(generator_01())
g2 = generator_02(generator_03())
g3 = generator_02()

for sequence_number in g1:
    print(sequence_number)

for sequence_number in g2:
    print(sequence_number)

for sequence_number in g3:
    print(sequence_number)
```