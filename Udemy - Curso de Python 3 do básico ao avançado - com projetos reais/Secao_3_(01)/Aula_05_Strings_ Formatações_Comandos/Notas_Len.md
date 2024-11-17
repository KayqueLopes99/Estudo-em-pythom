## Fatiamento de strings e a função len
- 1. `len()`:
-  Esta função retorna o número de caracteres em uma string(Tamanho).
    - Sintaxe: `len(string)`
    - Exemplo:
    ```python
    s = "Olá, Mundo!"
    print(len(s))  # Saída: 11
    ```
- Obs: a função len retorna a qtd 
de caracteres da str.
- A análise de strings é uma tarefa comum em programação e Python oferece várias funções integradas.
- Tamanho, terminação alfabetica e Funcionalidade.


## Fatiamento de strings
- As strings são iteraveis (Elemento por elemento por índice).
- Pegar pedaços selecionados da string.
-  012345678 (indices)
-  Olá mundo
- -987654321 (indices)
- Fatiamento(Sintaxe): `[inicio:fim:passo] [::]`
- inicio: o começo do fatiamento.
- Se omitir o inicio começa do inicio também.
- fim: se não colocar ele (omitir) ele imprime tudo.
- Se colocar o final, teremos uma observação.
- `SE VOCÊ QUISER PARAR UM ÍNDICE ESCOLHIDO FAÇA INDICE + 1.`.
- Obs: espaços contam, pois ele é um caractere.
- Passo: de quantos em quantos caracteres ele vai pular.
```` python
variavel = 'Olá mundo'
print(variavel[::-1])
````


- Escolher uma Letra por seu índice correspondente. 
``` 
FRASE = 'AguaTerraFogoAr'

- Na memória:
[A][g][u][a][ ][T][e][r][r][a][  ][ F ][ o ][ g ][ o ][  ][ A ][ r ]
 0  1  2  3  4  5  6  7  8  9  10   11   12   13   14  15   16   17

```
- Podemos:
> [0] -> pegar a primeira letra.
```python
genero = str(input("Informe seu Gênero:\nM = Masculino \nF = Feminino\n"))
```
> FRASE[9] -> a
- Podemos: 
- Sintaxe: [começo:fim]
> FRASE[11:14] -> F até g
- Aqui não irá pegar o indice 14, logo:
>  FRASE[11:15] -> F até o 
- Entedemos que deleta o último sempre.
- Podemos:
>  FRASE[11:18] -> F até o FINAL. 
- É uma maneira errada, mas funciona.
- Podemos:
- Sintaxe: [começo:fim:salto]
>  FRASE[11:18:2] -> F até o final pulando de 2 em 2. 
- Impressão: F g espaço r
- Podemos:
>  FRASE[:4] -> Da primeira letra até o 11, deletando o 11.
- Impressão: Agua
- Podemos:
>  FRASE[0:] -> Do caractere com o indice até o final.
- Podemos:
> FRASE[0::3] -> Vai até o final pulando de 3 em 3.

### aula28.py
- Exercício.
```python 
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Informe seu Nome: ') 
idade = input('Informe sua Idade: ')


# Quando você escreve if idade:, está verificando se a variável idade é considerada "verdadeira" em um contexto lógico.
if nome and idade:
    print(f"Seu Nome: {nome}")
    print(f"Seu Nome invertido: {nome[::-1]}")
    if ' ' in nome:
        print("Seu Nome contém espaços.")
    else:
        print("Seu Nome não contém espaços.")
    print(f"O Nome {nome} tem {len(nome)} Letras.")
    print(f"A primeira Letra do seu nome: {nome[0]}")
    print(f"A Ultima Letra do seu nome: {nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")
```