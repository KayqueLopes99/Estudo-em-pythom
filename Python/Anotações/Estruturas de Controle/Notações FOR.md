# Estrutura de repetição for
- Laço de Repetição.
- Variavel de controle.
- Repetir Eternamente até atingir ou conquistar a posição.
- Exemplo:
- Vc está np bloco 1, logo Vá do bloco 1 até o bloco 10, o qual se encontra o Crush kkkkkk.
- Laço C no interval0(1,10)
    passo
pega

- Sintaxe:
```python
for valor in sequencia: # (inicio,fim.salto)
    # bloco de código
```

- `valor` é a variável que assume o valor do item atual na sequência a cada iteração.
- `sequencia` é a sequência ou objeto iterável que o loop irá percorrer.
- O `bloco de código` é o conjunto de instruções que será executado para cada item na sequência.

##  Range => Intervalo.
- Exemplo:
```python
for i in range(5):
    print(i)
```

- Ele imprimirá os números de 0 a 4, um em cada linha.

# Loop com dois comandos:
- Digamos que temos o caminho de 0 à 3, e depois andar e pegar a fruta.

```python
for c in range(0,3):
    passo
    pula
passo 
pega
```
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
- O terceiro número será as casas puladas.
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