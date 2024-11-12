# Comando Sum:
- Permite somar os elementos de uma sequência, como uma lista, tupla ou conjunto. Ela retorna a soma total dos valores presentes na sequência.
- A sintaxe :

```python
soma = sum(iterable, start)
```

- `iterable`: Pode ser qualquer lista, tupla ou conjunto contendo números.
- `start` (opcional): Permite definir um valor inicial para a soma (caso não seja especificado, o valor padrão é 0).

- **Valores iniciais diferentes de zero**: O parâmetro `start` permite definir um valor inicial para a soma. Exemplo:
   ```python
   numeros = [1, 2, 3, 4, 5]
   soma = sum(numeros, 10)  # Saída: 25
   ```
