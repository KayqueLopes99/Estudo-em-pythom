# Break 
- Stop na Condição, desviando para o lado de fora da condição.
- Interrompa.
- Colocamos dentro do loop.

# Comando Break
- Interromper um loop, seja ele um `while` ou um `for`. Quando o Python encontra um comando `break` dentro de um desses loops, ele encerra imediatamente o loop.
```python
# Este loop vai pedir ao usuário para digitar um número
# e vai parar quando o usuário digitar '0'.
while True:
    numero = int(input('Digite um número (0 para sair): '))
    if numero == 0:
        print('Você escolheu sair do loop.')
        break
    else:
        print(f'O número digitado foi {numero}.')
```

### O `break` também pode ser usado em loops `for`, especialmente quando você está procurando por um item em uma lista e deseja parar o loop assim que o encontrar:

```python
# Lista de números
numeros = [1, 3, 7, 9, 2, 5]

# Este loop vai procurar pelo número '2' e parar quando encontrá-lo.
for numero in numeros:
    if numero == 2:
        print('Número 2 encontrado!')
        break
    else:
        print(f'Número {numero} não é o que estamos procurando.')
```

