## Declaração de varíaveis em Python
- Toda varíavel é um objeto.
- Formatação minuscula. 
. Sintaxe:
. O operador '=' é usado para atribuir
valores às varíaveis.
. '=' RECEBE
- nome_da_variavel = valor
- 
``` python
nome = 'Kayque'
idade = 19
peso = 62.3
anime = 'One piece'
print(nome, idade, peso, anime);
```
## Interagir com o usuário
. Input
- A função input() em Python lê a entrada que o usuário digitou e armazena o valor em uma variável. 

. Sintaxe:
- variavel = input(mensagem_opcional)
. Exemplo: 
- nome = input('Digite seu nome: ')
print('Olá, ' + nome)

- Exemplo:
. \n pular linha, ele vai servir na entrada de dados para organizar.
``` python
nome = input ('Qual e seu nome?\n')
idade = input ('Quantos anos voce tem?\n')
peso = input ('Quanto voce pesa?\n')
anime = input ('Qual e seu nome de seu anime?\n')
print(nome, idade, peso, anime)
```