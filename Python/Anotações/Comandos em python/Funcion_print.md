### `print(*args, sep=' ', end='\n', file=None, flush=False)`
# Parte restante para adicionar

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

