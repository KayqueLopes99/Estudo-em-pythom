# Replace: 
- O comando `replace()` em Python é um método usado para substituir partes de uma *string* por outra *string*.
-  Ele retorna uma nova *string* com as substituições realizadas, sem alterar a original.

### Sintaxe
```python
string.replace(parte_antiga, nova_parte, [count])
```

- **`parte_antiga`**: a sequência de caracteres que você deseja substituir.
- **`nova_parte`**: a sequência de caracteres que substituirá a `parte_antiga`.
- **`count`** (opcional): o número de vezes que a substituição deve ser feita. Se omitido, todas as ocorrências serão substituídas.

### Exemplos

1. **Substituir todas as ocorrências:**
   ```python
   texto = "Olá mundo! O mundo é incrível."
   novo_texto = texto.replace("mundo", "planeta")
   print(novo_texto)
   # Saída: "Olá planeta! O planeta é incrível."
   ```
