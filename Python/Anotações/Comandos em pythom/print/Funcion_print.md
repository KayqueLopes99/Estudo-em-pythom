### `print(*args, sep=' ', end='\n', file=None, flush=False)`

- ***args**: Representa os valores que queremos imprimir. O `*args` significa que podemos passar vários valores separados por vírgula para o `print`, e ele os imprimirá juntos. Exemplo:
  ```python
  print("Hello", "world", 123)  # Saída: Hello world 123
  ```

- **sep (separador)**: Este parâmetro controla o que será colocado **entre os valores** de `args` ao imprimir. Por padrão, o valor é um espaço (`' '`). Podemos mudar o `sep` para outra coisa. Exemplo:
  ```python
  print("Hello", "world", 123, sep='-')  # Saída: Hello-world-123
  ```

- **end (final da linha)**: Este parâmetro define o que será impresso **no final da linha**. Por padrão, o valor é uma nova linha (`'\n'`), fazendo com que cada `print` fique em uma nova linha. Podemos mudar `end` para outro valor para que o próximo `print` apareça na mesma linha, por exemplo:
  ```python
  print("Hello", end=' ')
  print("world")  # Saída: Hello world
  ```

- **`file` (arquivo)**: Este parâmetro permite que o `print` envie a saída para um **arquivo** em vez da tela. Se não especificarmos nada, ele manda para a tela (`sys.stdout`). Para usar um arquivo, primeiro abrimos o arquivo e, em seguida, indicamos o `file`. Exemplo:
  ```python
  with open('output.txt', 'w') as f:
      print("Hello world", file=f)  # A mensagem será escrita no arquivo output.txt
  ```

- **`flush`**: Esse parâmetro controla se o Python deve **limpar o conteúdo** imediatamente ou não. Quando `flush=True`, o Python força a saída a ser impressa imediatamente, sem esperar. Isso é útil em situações em que queremos ver a saída de um programa em tempo real, como em uma barra de progresso. Exemplo:
  ```python
  import time
  for i in range(5):
      print(i, end=' ', flush=True)
      time.sleep(1)  # Cada número será mostrado na tela sem esperar o final do loop
  ```
  - flush=True, garantindo que cada número seja mostrado assim que o print é chamado, sem atrasos.

