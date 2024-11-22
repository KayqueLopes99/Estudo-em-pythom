## A função print 
- A função `print`é usada para exibir ou imprimir informações, recebendo argumento(s).
- Aqui não temos o printf.
- - Sintaxe:
``` python
print(*args, sep=' ', end='\n', file=None, flush=False)
```
 + Coloca espaços `_`e quebra de linha por padrão `\n`.

- ***args**: Representa os valores que queremos imprimir.

  ```python
  print("Hello", "world", 123)  # Saída: Hello world 123
  ```

### sep 
- Este parâmetro **sep (separador)** controla o que será colocado **entre os valores** de `args` ao imprimir.
 + Colocado dentro do print ``sep=""` ou `sep=''`(Separador Desejado.)
 + Usado para separar impressões de argumentos de forma personalizada.
 
  ```python
  print("Hello", "world", 123, sep='-')  # Saída: Hello-world-123
  ```

### end
- Este parâmetro **end (final da linha)** define o que será impresso **no final da linha**. 
 + `end='\n'`(O final do print)
 + Imagine que temos dois print, o `end=' '` no primeiro print vai juntar essas duas linhas na mesma liha de código. Assim, escolhemos como estas linhas serão separadas por espaços por exemplo na linha de código.

  ```python
  print("Hello", end=' ')
  print("world")  # Saída: Hello world

- End pode ser útil quando você quer que os resultados sejam impressos lado a lado ou separados por um caractere específico.


```python
# Exemplo especificando o parâmetro 'end' como um espaço em branco
print("Primeira parte,", end=' ')
print("segunda parte na mesma linha.")

# Saída:
# Primeira parte, segunda parte na mesma linha.
```

- Caractere que faz a quebra de linha automatica nos print (\r\n) -> CRLF ou (\n) -> LF
- Exemplo:
``` python
# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="-", end=' = ')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
```


``` python 
# Pode ser
print("Estou aprendendo pythom!\n")
# Ou
print('Estou aprendendo pythom!\n')

# Não é necessário o \n, mas você pode usar assim. No entendo se você coloca.
print("Olá\n","mundo!")
# Ou
# O print abaixo com o restante da mensagem ele já pula a linha para você!!!
print("Ola")
print("mundo!")
. Imprimir o valor de uma variável:
## Temos isso tanto para caractere, quanto para número.
mensagem = "Olá, mundo!"
print(mensagem)
# Ou
numero = 10
print(numero)
```

# Print para textos longos:
- Para imprimir textos longos em Python, você pode usar aspas triplas para criar uma string de várias linhas. 
```python
texto = """
Este é um texto longo.
Você pode adicionar quantas linhas quiser.
Basta manter tudo entre as aspas triplas.
"""

print(texto)
```

