# Manipulando cadeia de texto
- String: Conjuntos de caracteres, com índices na memória e podemos manipular.

- Cada caracter tem seu índice correspondente. 
- Diferenciação de letras
## Fatiamento
- Escolher uma Letra por seu índice correspondente. 
``` 
FRASE = 'AguaTerraFogoAr'

- Na memória:
[A][g][u][a][ ][T][e][r][r][a][  ][ F ][ o ][ g ][ o ][  ][ A ][ r ]
 0  1  2  3  4  5  6  7  8  9  10   11   12   13   14  15   16   17

```
- Podemos:
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

## Análise 
- A análise de strings é uma tarefa comum em programação e Python oferece várias funções integradas.
- Tamanho, terminação alfabetica e Funcionalidade.

### 1. len():
-  Esta função retorna o número de caracteres em uma string.
    - Sintaxe: `len(string)`
    - Exemplo:
    ```python
    s = "Olá, Mundo!"
    print(len(s))  # Saída: 11
    ```

### 2. count():
 - Esta função retorna o número de vezes que um caractere ou uma substring aparece na string.
 - Contagem com fatiamento.
    - Sintaxe: `string.count(substring, start=..., end=...)`
    - Exemplo:
    ```python
    s = "Olá, Mundo! Mundo, você está aí?"
    print(s.count("Mundo"))  # Saída: 2
    ```

### 3. find():
 - Esta função retorna o índice da primeira ocorrência da substring na string. Se a substring não for encontrada, retorna -1.
    - Sintaxe: `string.find(substring, start=..., end=...)`
    - Exemplo:
    ```python
    s = "Olá, Mundo! Mundo, você está aí?"
    print(s.find("Mundo"))  # Saída: começa no 5
    print(s.find("Terra"))  # Saída: -1
    ```
### in
- O operador in em Python é usado para verificar se um valor existe em uma sequência.

``` Python
s = "Olá, Mundo!"
print("Mundo" in s)  # Saída: True
```

## Transformação
- Modificar a sequência de caracteres.

### 1. replace:
- replace(old, new, count)
-  Esta função retorna uma cópia da string onde todas as ocorrências da substring `old` são substituídas pela substring `new`.
-  O parâmetro `count` é opcional e, se especificado, apenas as primeiras `count` ocorrências são substituídas.

    ```python
    s = "Olá, Mundo!"
    print(s.replace("Mundo", "Python"))  # Saída: Olá, Python!
    ```

### 2. upper():
- Esta função converte todos os caracteres em letras maiúsculas.
    ```python
    s = "Olá, Mundo!"
    print(s.upper())  # Saída: OLÁ, MUNDO!
    ```

### 3. lower(): 
- Esta função converte todos os caracteres em letras minúsculas.
    ```python
    s = "Olá, Mundo!"
    print(s.lower())  # Saída: olá, mundo!
    ```

### 4. capitalize(): 
- Esta função converte o primeiro caractere da string em maiúscula e torna todos os outros caracteres minúsculos.
    ```python
    s = "olá, MUNDO!"
    print(s.capitalize())  # Saída: Olá, mundo!
    ```

### 5. title():
- Esta função converte a primeira letra de cada palavra para maiúscula e as demais para minúscula.
    ```python
    s = "olá, MUNDO!"
    print(s.title())  # Saída: Olá, Mundo!
    ```

### 6. strip(chars):
- Digitar espaços inicialmente. 
- Esta função retorna uma cópia da string com os caracteres `chars` removidos do início e do fim da string, ou seja os espaços. Se `chars` não for fornecido, todos os espaços em branco serão removidos.
    ```python
    s = "   Olá, Mundo!   "
    print(s.strip())  # Saída: Olá, Mundo!
    ```

## Junção com split()
- É usado para dividir uma string em uma lista onde cada palavra é um item separado na lista.

```python
texto = "Olá, como você está?"
palavras = texto.split()
print(palavras)
```

- Neste exemplo, a string "Olá, como você está?" é dividida em uma lista de palavras, e o resultado seria `['Olá,', 'como', 'você', 'está?']`.

## Junção com o join()
- É usado para combinar os elementos de uma lista em uma única string.

```python
separador.join(iterable)
```
Temosn: 
- separador: Especifica a string a ser usada como separador.
- iterable: Uma sequência iterável, como uma lista, tupla ou conjunto, cujos elementos serão unidos em uma string.

```python
palavras = ['Olá,', 'como', 'você', 'está?']
texto = ' '.join(palavras)
print(texto)
```

- Neste exemplo, a lista de palavras `['Olá,', 'como', 'você', 'está?']` é unida em uma única string, e o resultado seria `"Olá, como você está?"`.

### Variação r
- Lado direito da string

### Variação l
- Lado esquerdo da string