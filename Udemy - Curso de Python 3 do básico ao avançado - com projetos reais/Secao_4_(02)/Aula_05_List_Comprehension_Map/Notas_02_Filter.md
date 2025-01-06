## Filtro de dados em list comprehension (filter)
### *Esquerda do for é mapeamento e a direita do for é filtro*.
- Filtrar dados significa **selecionar apenas os elementos que atendem a uma condição específica** dentro de uma lista ou outro iterável.
- Uso de condições.
1. **Usando `filter()`**  
2. **Usando List Comprehension**  
 
- Sintaxe de `filter()`
```python
filter(funcao, iterável)
```

- Exemplo 1: Filtrar números pares  
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]
```

