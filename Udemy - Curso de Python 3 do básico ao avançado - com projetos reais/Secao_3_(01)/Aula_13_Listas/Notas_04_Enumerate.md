## **`enumerate()` em Python**
- É uma função embutida do Python que permite iterar sobre elementos de uma sequência (como listas, tuplas ou strings) ao mesmo tempo em que fornece o índice de cada elemento. 

---

- *Sintaxe*
```python
enumerate(iterável, início=0)
```
- **`iterável`** → Qualquer objeto iterável, como lista, tupla ou string.  
- **`início`** *(opcional)* → Define o número inicial do índice (padrão é `0`).

---

### **Exemplo 1: Iterando sobre uma lista com `enumerate()`**
```python
frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
```
🔹 **Saída**:
```
Índice 0: maçã
Índice 1: banana
Índice 2: uva
```

---

### **Exemplo 2: Usando `enumerate()` com um índice personalizado**
Podemos definir um índice inicial diferente de zero:

```python
frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas, start=1):
    print(f"Posição {indice}: {fruta}")
```
🔹 **Saída**:
```
Posição 1: maçã
Posição 2: banana
Posição 3: uva
```

---

### **Exemplo 3: Convertendo `enumerate()` em uma lista**
O `enumerate()` retorna um objeto enumerado, que pode ser convertido para lista ou tupla:

```python
frutas = ["maçã", "banana", "uva"]
lista_enumerada = list(enumerate(frutas))

print(lista_enumerada)
```
🔹 **Saída**:
```
[(0, 'maçã'), (1, 'banana'), (2, 'uva')]
```

---
