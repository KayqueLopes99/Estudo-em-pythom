# As f-strings
- São uma maneira de formatar strings que é mais concisa e fácil de ler do que os métodos anteriores.

- Sintaxe:

```python
nome = "Mundo"
mensagem = f"Olá, {nome}!"
print(mensagem)  # Saída: Olá, Mundo!
```

```python
x = 10
y = 5
resultado = f"A soma de {x} e {y} é {x + y}"
print(resultado)  # Saída: A soma de 10 e 5 é 15
```

```python
import datetime
data_atual = datetime.datetime.now()
print(f"A data e hora atuais são: {data_atual:%Y-%m-%d %H:%M:%S}")
# Saída: A data e hora atuais são: 2024-05-15 21:59:26 (dependendo do momento da execução)
```

- As f-strings são uma ferramenta poderosa e flexível que torna a formatação de strings em Python muito mais intuitiva e legível.

# Obs:
- Nova forma de print:
- print(f'A soma vale {variavel}')
``` python
- # Loop infinito:
n = s = 0
while True:
    n = int(input('Digite em número: '))
    if n == 999:
       break
    s += n
s -= 999
# print('A Soma vale {}'.format(s))
print(f'A soma vale {s}')
```

### Nova Maneira.
### dinheiro = 1333.66
### print(f'{dinheiro:.2f}')