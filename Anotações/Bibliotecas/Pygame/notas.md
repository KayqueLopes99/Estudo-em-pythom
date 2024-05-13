# Biblioteca Pygame.
- Inicializar sempre com:
````python
pygame.init()
````

## 1. pygame.time.get_ticks():
- Este comando retorna o número de milissegundos desde que `pygame.init()` foi chamado. Isso é útil para rastrear a quantidade de tempo que passou. A sintaxe é:
    ```python
    tempo_passado = pygame.time.get_ticks()
    ```
    Aqui, `tempo_passado` será o tempo em milissegundos desde a inicialização do Pygame.

## 2. pygame.time.wait(milliseconds):
- Este comando pausa o programa por uma quantidade de tempo especificada em milissegundos. A sintaxe é:
    ```python
    pygame.time.wait(500)  # pausa o programa por 500 milissegundos
    ```
    Neste exemplo, o programa será pausado por 500 milissegundos.

## 3. pygame.time.delay(milliseconds):
- Este comando também pausa o programa por uma quantidade de tempo especificada em milissegundos. No entanto, ao contrário do `pygame.time.wait()`, este comando usa o processador (em vez de dormir) para tornar o atraso mais preciso. A sintaxe é:
    ```python
    pygame.time.delay(500)  # pausa o programa por 500 milissegundos
    ```
    Neste exemplo, o programa será pausado por 500 milissegundos.

## 4. pygame.time.set_timer(event, millis): 
- Este comando cria um evento para aparecer na fila de eventos a cada número dado de milissegundos. A sintaxe é:
    ```python
    MEU_EVENTO = pygame.USEREVENT + 1
    pygame.time.set_timer(MEU_EVENTO, 2000)  # dispara o evento MEU_EVENTO a cada 2000 milissegundos
    ```
    Neste exemplo, o evento `MEU_EVENTO` será disparado a cada 2000 milissegundos.

