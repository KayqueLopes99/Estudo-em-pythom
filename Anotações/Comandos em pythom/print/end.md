# END
- O parâmetro `end` na função `print()` em Python permite que você defina o que será impresso no final da execução dessa função. 

- End pode ser útil quando você quer que os resultados sejam impressos lado a lado ou separados por um caractere específico.

- Exemplo:
```python
# Exemplo sem especificar o parâmetro 'end'
print("Primeira linha")
print("Segunda linha")

# Saída:
# Primeira linha
# Segunda linha
```

```python
# Exemplo especificando o parâmetro 'end' como um espaço em branco
print("Primeira parte,", end=' ')
print("segunda parte na mesma linha.")

# Saída:
# Primeira parte, segunda parte na mesma linha.
```

- Neste segundo exemplo, a primeira chamada de `print()` termina com um espaço em branco (`' '`) em vez de uma nova linha. Portanto, quando a segunda chamada de `print()` é executada, ela começa exatamente onde a primeira terminou, resultando em ambas as strings sendo impressas na mesma linha.

