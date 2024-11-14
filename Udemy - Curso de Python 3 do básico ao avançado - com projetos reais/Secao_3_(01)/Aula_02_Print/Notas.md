## A função print 
- A função `print`é usada para exibir ou imprimir informações, recebendo argumento(s).
- - Sintaxe:
``` python
print(*args, sep=' ', end='\n', file=None, flush=False)
```
 + Coloca espaços `_`e quebra de linha por padrão `\n`.

- ***args**: Representa os valores que queremos imprimir.

  ```python
  print("Hello", "world", 123)  # Saída: Hello world 123
  ```
- Este parâmetro **sep (separador)** controla o que será colocado **entre os valores** de `args` ao imprimir.
 + Colocado dentro do print ``sep=""` ou `sep=''`(Separador Desejado.)
 + Usado para separar impressões de argumentos de forma personalizada.
 
  ```python
  print("Hello", "world", 123, sep='-')  # Saída: Hello-world-123
  ```


- Este parâmetro **end (final da linha)** define o que será impresso **no final da linha**. 
 + `end='\n'`(O final do print)
 + Imagine que temos dois print, o `end=' '` no primeiro print vai juntar essas duas linhas na mesma liha de código. Assim, escolhemos como estas linhas serão separadas por espaços por exemplo na linha de código.

  ```python
  print("Hello", end=' ')
  print("world")  # Saída: Hello world


- Caractere que faz a quebra de linha automatica nos print (\r\n) -> CRLF ou (\n) -> LF
- Exemplo:
``` python
# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="-", end=' = ')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
```
