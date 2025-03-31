## Usando a função input para coletar dados do usuário
- É utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). 
- **A função lê a entrada, converte para string e retorna o valor**.
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

## **Este é a melhor forma de solicitar**:
- Primeiro obtermos os dados em forma de string e posteriomente convertemos para algum tipo de dados como inteiro, boleano ou float. Não é necessário converter para string, pois ela já é uma.
- Lógico antes de converter faça o tratamento. 
``` python
nome = input ('Qual e seu nome?\n')
idade = input ('Quantos anos voce tem?\n')
idade_int = int(idade)
peso = input ('Quanto voce pesa?\n')
peso_int = int(peso)
anime = input ('Qual e seu nome de seu anime?\n')
print(nome, idade, peso, anime)
```

- Imprimir o nome da varíavel e o seu valor atribuido.
``` python
nome = input("Nome: ")
print(f"{nome=}")
```

## Declaração de varíaveis em Python
- Toda varíavel é um objeto.
- O operador '=' é usado para atribuir
valores às varíaveis.

``` python
nome = 'Kayque'
idade = 19
peso = 62.3
anime = 'One piece'
print(nome, idade, peso, anime);
```

## Regras: 
- variaveis são Minuscula. 
- Deve obrigatoriamente começar com uma letra.
- Não deve possuir espaços em branco.
- Não pode conter símbolos especiais, exceto o sublinhado (_).