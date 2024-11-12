## Importando a biblioteca math

Para usar a biblioteca `math`, temos o comando:

```python
import math
```

## Funções e constantes na biblioteca math

### math.pi e math.e

`math.pi` e `math.e` são constantes que representam o valor de pi e o número de Euler, respectivamente.

Exemplo:

```python
import math

print(math.pi)  # Imprime o valor de pi
print(math.e)   # Imprime o valor de e
```

### math.ceil(x) e math.floor(x)

`math.ceil(x)` retorna o menor inteiro maior ou igual a `x`, enquanto `math.floor(x)` retorna o maior inteiro menor ou igual a `x`.

Exemplo:

```python
import math

print(math.ceil(2.3))  # Imprime 3
print(math.floor(2.3))  # Imprime 2
```

### math.trunc(x)

`math.trunc(x)` retorna a parte inteira de `x`.

Exemplo:

```python
import math

print(math.trunc(2.3))  # Imprime 2
```

### math.pow(x, y)

A função `math.pow(x, y)` retorna `x` elevado à potência `y`.

Exemplo:

```python
import math

print(math.pow(2, 3))  # Imprime 8.0
```

### math.sqrt(x)

A função `math.sqrt(x)` retorna a raiz quadrada de `x`.

Exemplo:

```python
import math

print(math.sqrt(9))  # Imprime 3.0
```

### math.factorial(x)

A função `math.factorial(x)` retorna o fatorial de `x`.

Exemplo:

```python
import math

print(math.factorial(5))  # Imprime 120
```

### math.sin(x), math.cos(x), math.tan(x)

Essas funções retornam o seno, cosseno e tangente de `x` radianos, respectivamente.

Exemplo:

```python
import math

graus = 45
radianos = math.radians(graus)

print(math.sin(radianos))  # Imprime o seno de 45 graus
print(math.cos(radianos))  # Imprime o cosseno de 45 graus
print(math.tan(radianos))  # Imprime a tangente de 45 graus
```

### math.log(x[, base])

A função `math.log(x[, base])` retorna o logaritmo natural de `x` (para a base `e`). Se a `base` for especificada, retorna o logaritmo de `x` para a `base`.

Exemplo:

```python
import math

print(math.log(10))       # Imprime 2.302585092994046 (logaritmo natural)
print(math.log(100, 10))  # Imprime 2.0 (logaritmo na base 10)
```

