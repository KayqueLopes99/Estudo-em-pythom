## Funções lambda complexas (para entendimento)
- Sintaxe
```python
lambda argumentos: expressão_retornada, valores_atribuidos
```
- **`lambda`** cria uma função anônima.
- **`argumentos`** são os parâmetros da função.
- **`expressão`** é a operação retornada.

- Exemplo:

```py
def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(lambda x, y: x + y, 2, 3),
    # ou
    executa(soma, 2, 3),
    # ou
    soma(2, 3)
)

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(3))

```

- Cuidado com código complexos. Eles devem ser "Práticos".
- Uso para coisas mais simples. 
- Se não de certo siga na precisão com funções.8