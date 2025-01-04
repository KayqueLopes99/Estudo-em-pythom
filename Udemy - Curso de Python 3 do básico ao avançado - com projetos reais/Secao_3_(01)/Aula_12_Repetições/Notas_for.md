## Introdução ao for / in - estrutura de repetição para coisas finita
- Quanto há noção do fim de uma repetição utiliza-se `for`.
- O `While` é ultilizado quando não há noção das repetições.
- O comando `for` é um laço de Repetição. Variavel de controle.
- O objetivo: repetir Eternamente até atingir ou conquistar a posição.
- Ele recebe um iteravel "(variavel qualquer)" para atuar em uma sequência ou cojunto.

- Sintaxe:
```python
for variável in sequencia: # (inicio,fim,salto)
    # bloco de código
```
- `variável` é a variável que assume o valor do item atual na sequência a cada iteração.
- `sequencia` é a sequência ou objeto iterável que o loop irá percorrer.
- O `bloco de código` é o conjunto de instruções que será executado para cada item na sequência.


- O `for` -> `Para cada elemento dentro da sequência ou cojunto, faça ...
``` python
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + "*")
```

## range + for para usar intervalos de números
- O comando range em Python é usado para gerar uma sequência de números, que pode começar de um valor inicial (padrão é 0) e vai até, mas não incluindo, um valor final, com um incremento opcional (padrão é 1).
- range ->(start, stop, step)
- `range(variavel) -> Está variavel uma sequência de números de 0 até n-1.`
- (start) -> começo.
- (end) -> fim: ultimo digito não incluido.
- (step) -> salto: observe o inicio e o fim. 
- Exemplo:
```python
for i in range(0,1,1):
    print(i)
```
- Ele imprimirá os números de 0 a 4, um em cada linha.

# Pode ter condicionais dentro do for
- Teremos que aninhar.
- Podemos aninhar como queiser.
- Outro exemplo:
```python
for c in range(0,3):
    if moeda:
       pega
    passo
    pula
passo 
pega
```

```python
# Pular de 2 em duas casas.
for c in range(0,11,2):
    if moeda:
       pega
    passo
    pula
passo 
pega
```

##  Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)
- Iterável -> str, range, ... 
- Iterador -> quem sabe entregar um valor por vez.
- iter: `iter(string)` -> o objeto que sabe iterar a string
- next -> me entregue o próximo valor disponível. `next(string)` - Erro acontece quado acaba os valores.
- iter -> me entregue seu iterador.

``` python
texto = 'Kayque' # iterável.
iteratador = iter(texto) # iterador

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# Principal.
# for letra in texto:
#    print(letra)
```
- O for em Python funciona com iteráveis. Ele usa o método interno iter para obter um iterador (um objeto que sabe como percorrer os elementos da sequência). O for chama automaticamente next no iterador para obter o próximo valor. Quando todos os valores são processados, ocorre uma exceção StopIteration, que sinaliza para o for parar a execução sem erros visíveis.

## O que aprendemos com while também funciona no for (continue, break, else, etc)
``` python
for i in range(10): #0  a 9
    # Coodições
    if i == 2:
      print("i é 2, pulando...")
      continue
    # Break - parar.
    if i == 8:
       print('i é 8, seu else ão executará')
       break

    # Aninhado
    for j in range(1, 3):
       print(i ,j)

else:
   print("For completo com sucesso.")
    
```
- No exemplo, o else do for será executado somente se o loop externo (o for i in range(10):) for concluído completamente, ou seja, sem que um break interrompa a execução.

- Exercício em `Aula_48.py`

