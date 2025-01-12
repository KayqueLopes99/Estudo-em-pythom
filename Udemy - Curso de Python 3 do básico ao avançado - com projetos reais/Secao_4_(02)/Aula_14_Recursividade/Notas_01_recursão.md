## Funções Recursivas, Recursividade e Stack Overflow no Python
## 0.1 O Que é uma Função Recursiva:
- É uma função que **chama a si mesma** dentro de seu próprio código.
- Ela é usada para resolver problemas que podem ser divididos em **subproblemas menores**.
- Dividir para conquistar.
+ Toda recursividade deve ter:
- 01. Um problema que possa em partes menores
- 02. Um caso recursivo que resolve um pequeno problema.
- 03. Um caso base
- 04. Uniformidade

- Exemplo:
```python
def contagem_regressiva(n):
    if n <= 0:  # Caso base
        print("Fim!")
    else:
        print(n)
        contagem_regressiva(n - 1)  # Chamada recursiva

contagem_regressiva(5)
```
- **Caso base**: A condição que **para** a recursão.  
- **Passo recursivo**: A chamada da função com um valor menor para aproximar do caso base.

--- 

- Cada chamada recursiva cria um **novo quadro de pilha (stack frame)** na memória.
- O Python mantém essas chamadas em uma **pilha de execução (Call Stack)**.

## **Exemplo: Fatorial de um Número**  
```python
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)  # Chamada recursiva

print(fatorial(5))  # 5 * 4 * 3 * 2 * 1 = 120
```
- **Fluxo de Execução**:  
```
fatorial(5)
 → 5 * fatorial(4)
   → 4 * fatorial(3)
     → 3 * fatorial(2)
       → 2 * fatorial(1) → Retorna 1
```
- **Quando a pilha atinge `n == 1`**, os valores são desempilhados e calculados **de trás para frente**.

---

## 0.3. Stack Overflow: O Perigo da Recursão Infinita  
- Se a função **não tiver um caso base** ou **a pilha for excedida**, ocorre um **Stack Overflow**, que faz o programa travar.
```python
def infinito(n):
    print(n)
    infinito(n + 1)  # Nunca para!

infinito(1)
```
```
RecursionError: maximum recursion depth exceeded
```

## Limite de recursão e cuidados com funções recursivas
- O limite é até 996.
- Alterar o limite. 
```py
import sys
sys.setrecursionlimit(1004)
```
