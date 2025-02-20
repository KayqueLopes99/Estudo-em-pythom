# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
- *args (ilimitado de argumentos posicionais)
- **kwargs (ilimitado de argumentos nomeados)
- 🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.
- Um bloqueio que evita erros de variável.
- Antes da Barra: Posicional.
- Depois da Barra: é Normal.

```python
def soma(a, b, /, x, y):
    print(a + b + x + y)


soma(1, 2, 3, y= 3)
```

- PEP 570 – Python Positional-Only Parameters
- https://peps.python.org/pep-0570/


- 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
- Antes da Barra: Posicional.
- Depois da Barra: é Nomeado.
- Limitar a quantidade de argumento posicionais. 



- PEP 3102 – Keyword-Only Arguments
- https://peps.python.org/pep-3102/
