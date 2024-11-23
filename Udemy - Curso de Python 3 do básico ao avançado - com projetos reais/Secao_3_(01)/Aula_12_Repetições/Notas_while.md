## Estrutura de repetição - while e break -
+ Conceito:
- `while (enquanto)` -> Executa uma ação enquanto uma condição for verdadeira(Atendida).
- Enquanto não satifazer a Condição o loop continua.
- Usada para repetir um bloco de código enquanto uma condição for verdadeira(Atendida).
- Sintaxe:
````python
while condicao:
    # bloco de código Dentro.
# Bloco de código fora.
````
- Cuidado com Loop infinito (Repetição que sempre é verdadeira).
- Quando termina o bloco de código ele volta para o while e checa a condição novamente.
- Debuger.

## While true:
- O loop while True é um loop infinito. Ele continuará a executar o bloco de código dentro dele até que uma instrução break seja chamada.
- Usamos break para sair se uma condição se tornar verdade.
- Exemplo:
```` python
while True:
    resposta = input("Digite 'sair' para terminar o loop: ")
    if resposta == 'sair':
        print("Saindo do loop.")
        break

````
## While False:
-  Ele nunca será executado porque False é uma constante que sempre avalia como falsa. Portanto, o código dentro do loop nunca será alcançado. 
- Exemplo:
```` python
while False:
    print("Este código nunca será executado.")
````

## Break 
- Stop na Condição, desviando para o lado de fora da condição.
- Interrompa o while mais proximo.
- Colocamos dentro do loop.

## Comando Break
- Stop na Condição, desviando para o lado de fora da condição.
- Colocamos dentro do loop.
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

- O `break` também pode ser usado em loops `for`, especialmente quando você está 
- procurando por um item em uma lista e deseja parar o loop assim que o encontrar:
- Dentro de uma condição aninhada como um `if`.
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

## OBS:
- Na condição:
- Se não for nenhum desses caracteres.
- Eles podem ser Juntos.
```python
while genero not in 'MmFf':
     # Bloco.
```

## Operadores aritméticos compostos
### De atibuição.
- x += y -> x = x + y
- x -= y -> x = x - y
- x *= y -> x = x * y
- x /= y -> x = x / y
- x //= y -> x = x // y
- x %= y -> x = x % y
- x **= y -> x = x ** y

##  while + continue - pulando alguma repetição
``` python
c = 0
while c <= 10:
    c += 1
    print(c)
print("Acabou.")

```
- Usado dentro de loops para pular a iteração atual e passar imediatamente para a próxima, ignorando o restante do código que vem depois dele dentro do loop.
- continue só pode ocorrer sintaticamente aninhado em um laço for ou while, mas não aninhado em uma função ou definição de classe dentro desse laço. Ele continua com o próximo ciclo do laço de fechamento mais próximo.
- `Ele vai pular algo`

- Sintaxe:
```python
while condição:
    if condição_para_pular:
        continue  # Ignora o restante do código abaixo e vai para a próxima iteração
    # Código que será executado se a condição_para_pular não for atendida
```

```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:  # Verifica se o número é par
        continue    # Pula para a próxima iteração
    print(i)        # Será executado apenas para números ímpares
```

``` python
contador = 0

while contador <= 100:
    contador += 1 # Atualização sempre.

    if contador == 6:
        print("Não vou mostrar o 6.")
        continue # Dentro de condições e repetição aninhada.

    if contador >= 10 and contador <= 27:
        print(f"Não vou mostrar o {contador}")
        continue

    print(contador)

    if contador == 40:
        break

print("-"*10)
```

## while + while (laços internos)
- É comum usar laços de repetição aninhados (while dentro de while) para repetir alguma coisa dentro de uma repetição existente.
- Imagine um circulo grande o while externo começa a rodar e o outro while dentro dele é o circulo interno que roda uma qtd x vezes em todo iteração do externo  
```` python
qtd_linhas = 5
qtd_colunas = 5

linha = 1 # Iniciamos com a linha 1.
print("-"*10) 
while linha <= qtd_linhas:
    # Cada linha deve estar em 5 colunas.
    coluna = 1
    # Quando executa começa com a linha 1 verificando a condição, depois a declaração de coluna vai para o loop interno while repetindo 5 vezes pois são 5 colunas para linha 1 e ...
    while coluna <= qtd_colunas:
        # print(f'{linha=} {coluna=}')
        print(f'{linha} {coluna}')
        coluna += 1
    linha += 1


print("-"*10) 
````
- Exercício `Aula39.py`
- Exercício `Aula40.py`

## while / else (recurso peculiar do Python)
- Contém `else`.
- Quando o laço while é executado completamente o bloco `else` é executado, detro ou fora do while.
- Exemplo, procurar um espaço vazio ou algum ouro elemento na string, tipo se não encontrar falava que não encontrou o eleemnto definido

``` python
""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
```

## while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)
- Algoritmo que salva um valor enquanto execulta uma tarefa.
- Exercício: `Aula42.py`.
- Aqui teremos um método de iteração, ou seja, percorrer o elemento e fazer contagens.
 
