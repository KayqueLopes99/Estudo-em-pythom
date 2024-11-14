## Usando a função input para coletar dados do usuário
- Interagir com o usuário solicitando dados.
- A função input() em Python lê a entrada que o usuário digitou e armazena o valor em uma variável. 
- Ele é já uma string.
- Saí do input() e vai para varíavel.
- Podemos converter já para o Tipo. 

- Sintaxe:
- `variavel = tipo(input('mensagem_opcional'))`

- Exemplo: 
``` python
nome = str(input('Digite seu nome: '))
print('Olá, ' + nome)
idade = str(input(f'Digite sua idade {nome}: '))
print(nome, idade)
```

- Exemplo:
. \n pular linha, ele vai servir na entrada de dados para organizar.
``` python
nome = input ('Qual e seu nome?\n')
idade = input ('Quantos anos voce tem?\n')
peso = input ('Quanto voce pesa?\n')
anime = input ('Qual e seu nome de seu anime?\n')
print(nome, idade, peso, anime)
```

- Imprimir o nome da varíavel e o seu valor atribuido.
``` python
nome = input("Nome: ")
print(f"{nome=}")
```

