## Jupyter Notebook
- Caderno de anotações que executa códigos.


## Threads - Executando processamentos em paralelo
- Threads são **fluxos de execução dentro de um mesmo processo**.
- Usar threads permite que diferentes tarefas rodem **aparentemente ao mesmo tempo**, compartilhando o mesmo espaço de memória.

> módulo **`threading`**.

-**Sintaxe**

```python
import threading

# Função que a thread vai executar
def minha_tarefa():
    print("Executando tarefa em thread")

# Criar uma thread
t = threading.Thread(target=minha_tarefa)

# Iniciar a thread
t.start()

# Esperar a thread terminar (opcional)
t.join()
```

---

### **Exemplo prático – Executar duas funções em paralelo**

```python
import threading
import time

def tarefa_1():
    for i in range(5):
        print(f"Tarefa 1 - passo {i}")
        time.sleep(1)

def tarefa_2():
    for i in range(5):
        print(f"Tarefa 2 - passo {i}")
        time.sleep(1)

# Criar as threads
thread1 = threading.Thread(target=tarefa_1)
thread2 = threading.Thread(target=tarefa_2)

# Iniciar as threads
thread1.start()
thread2.start()

# Aguardar todas terminarem
thread1.join()
thread2.join()

print("Todas as tarefas concluídas!")
```

**Saída esperada (as linhas se intercalam, mostrando execução paralela):**

```
Tarefa 1 - passo 0
Tarefa 2 - passo 0
Tarefa 1 - passo 1
Tarefa 2 - passo 1
...
Todas as tarefas concluídas!
```

---

### **Resumo**

* **`threading.Thread(target=func)`** → cria a thread para executar `func`.
* **`start()`** → inicia a execução.
* **`join()`** → espera a thread acabar.
* Ideal para tarefas de **I/O**, pois o GIL limita ganho em tarefas puramente de CPU.

---
