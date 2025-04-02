## Métodos de strings
- Métodos de strings mencionados em Python.
## 1. `len()`
- Explicação:
- O método `len()` retorna o número de caracteres (incluindo espaços) de uma string.
- Tamanho da mensagem.
-Sintaxe:
```python
len(string)
```

- Exemplo:
```python
texto = "Python"
tamanho = len(texto)
print(tamanho)  # Saída: 6
```


## 2. `count()`
- Explicação:
- Conta o número de ocorrências de um caractere ou substring dentro da string.

- Sintaxe:
```python
string.count(substring, start, end)
```
- `substring`: O texto que você deseja contar.
- `start`: (Opcional) Índice inicial para começar a busca.
- `end`: (Opcional) Índice final para terminar a busca.

- Exemplo:
```python
frase = "banana"
contagem = frase.count("a")
print(contagem)  # Saída: 3
```


## 3. `find()`
- Explicação:
- Retorna o índice da primeira ocorrência de uma substring dentro da string. Retorna -1 se a substring não for encontrada.

- Sintaxe:
```python
string.find(substring, start, end)
```
- `substring`: O texto a ser procurado.
- `start` e `end`: (Opcional) Limites da busca.

- Exemplo:
```python
texto = "Aprender Python é divertido"
indice = texto.find("Python")
print(indice)  # Saída: 9
```

## OBS:
- s.find(subtexto, ini, fim) Procura subtexto em s começando da posição ini até a posição fim.
- Retorna −1, se o subtexto não for encontrado.
``` python

nome_completo = input('Informe seu nome completo: ')
sobrenome = input('Informe seu sobrenome: ')
pos = nome_completo.find(sobrenome)
if pos != -1:
 print('Seu sobrenome começa na posição ', pos)
else:
 print('Sobrenome não encontrado')
n = float(input('Informe um número: '))
print('{n:.8f}'.format(n=n))
```


## 4. `replace()`
- Explicação:
- Substitui todas as ocorrências de uma substring por outra substring.

- Sintaxe:
```python
string.replace(old, new, count)
```
- `old`: Texto a ser substituído.
- `new`: Novo texto para substituir.
- `count`: (Opcional) Número máximo de substituições.

- Exemplo:
```python
texto = "banana"
novo_texto = texto.replace("a", "o")
print(novo_texto)  # Saída: "bonono"
```


## 5. `upper()`
- Explicação:
- Converte todos os caracteres de uma string para letras maiúsculas.

- Sintaxe:
```python
string.upper()
```

- Exemplo:
```python
texto = "python"
maiusculo = texto.upper()
print(maiusculo)  # Saída: "PYTHON"
```


## 6. `lower()`
- Explicação:
- Converte todos os caracteres de uma string para letras minúsculas.

- Sintaxe:
```python
string.lower()
```

- Exemplo:
```python
texto = "PYTHON"
minusculo = texto.lower()
print(minusculo)  # Saída: "python"
```


## 7. `capitalize()`
- Explicação:
- Converte a primeira letra da string para maiúscula e o restante para minúsculas.

- Sintaxe:
```python
string.capitalize()
```

- Exemplo:
```python
texto = "python é incrível"
capitalizado = texto.capitalize()
print(capitalizado)  # Saída: "Python é incrível"
```


## 8. `title()`
- Explicação:
O método `title()` retorna uma cópia da string onde a primeira letra de cada palavra é transformada em maiúscula, e o restante em minúscula.
- 
- Sintaxe:
```python
string.title()
```

- Exemplo:
```python
texto = "python é incrível"
formatado = texto.title()
print(formatado)  # Saída: "Python É Incrível"
```

## split, join e strip são métodos muito úteis da str
## 9. `strip(chars)`
- Explicação:
- Remove os caracteres especificados (ou espaços em branco, por padrão) do início e do fim da string.
- 
- Sintaxe:
```python
string.strip(chars)
```
- `chars`: (Opcional) Os caracteres que você deseja remover. Se omitido, remove espaços em branco.

- Exemplo:
```python
texto = "  Python  "
limpo = texto.strip()
print(f"'{limpo}'")  # Saída: 'Python'

texto2 = "xxPythonxx"
limpo2 = texto2.strip("x")
print(limpo2)  # Saída: "Python"
```
- `rstrip()` -> espaços da direita.
- `lstrip()` -> espaços da esquerda. 

## 10. Junção com `split()`
- Explicação:
- O método `split()` divide uma string em uma lista, com base em um delimitador (padrão é o espaço).
- retorna uma list.
- Sintaxe:
```python
string.split(delimiter, maxsplit)
```
- `delimiter`: (Opcional) O caractere usado para dividir a string.
- `maxsplit`: (Opcional) Máximo de divisões a serem realizadas.

- Exemplo:
```python
texto = "Python é incrível"
lista = texto.split()
print(lista)  # Saída: ['Python', 'é', 'incrível']



# Separação pela vírgula.
texto2 = "Python,Código,Simples"
lista2 = texto2.split(",")
print(lista2)  # Saída: ['Python', 'Código', 'Simples']
```


## 11. Junção com `join()`
- Explicação:
- O método `join()` junta os elementos de uma lista ou iterável em uma string, usando um delimitador.

- Sintaxe:
```python
delimiter.join(iterable)
```
- `delimiter`: O separador entre os elementos.
- `iterable`: Lista ou iterável cujos elementos serão unidos.

- Exemplo:
```python
lista = ["Python", "é", "incrível"]
texto = " ".join(lista)
print(texto)  # Saída: "Python é incrível"
```

## 12. Método `startswith()`
- Explicação:
- Verifica se a string começa com uma sequência específica de caracteres. Retorna `True` se for o caso, caso contrário retorna `False`.

- Sintaxe:
```python
string.startswith(prefix, start, end)
```
- `prefix`: O texto a ser verificado no início da string.
- `start` e `end`: (Opcional) Intervalo da string onde o prefixo será verificado.

- Exemplo:
```python
texto = "Python é incrível"
resultado = texto.startswith("Python")
print(resultado)  # Saída: True
```


## 13. Método `endswith()`
- Explicação:
- Verifica se a string termina com uma sequência específica de caracteres. Retorna `True` se for o caso, caso contrário retorna `False`.

- Sintaxe:
```python
string.endswith(suffix, start, end)
```
- `suffix`: O texto a ser verificado no final da string.
- `start` e `end`: (Opcional) Intervalo da string onde o sufixo será verificado.

- Exemplo:
```python
texto = "Python é incrível"
resultado = texto.endswith("incrível")
print(resultado)  # Saída: True
```

## 14. `zfill()`
- Explicação:
O método `zfill()` preenche a string com zeros à esquerda até atingir um comprimento especificado.

- Sintaxe:
```python
string.zfill(width)
```
- `width`: Comprimento total desejado da string após o preenchimento.

- Exemplo:
```python
numero = "42"
numero_completo = numero.zfill(5)
print(numero_completo)  # Saída: "00042"
```

## 15. Método `rjust()`
- Explicação:
- O método `rjust()` retorna a string alinhada à direita, preenchendo o espaço à esquerda com um caractere especificado.

- Sintaxe:
```python
string.rjust(width, fillchar)
```
- **`width`**: O comprimento total desejado para a string.
- **`fillchar`**: (Opcional) O caractere de preenchimento (padrão é um espaço).

```python
texto = "42"
resultado = texto.rjust(5, '0')
print(resultado)  # Saída: 00042
```



## 16. `enumerate()`
- Explicação:
A função `enumerate()` retorna um objeto enumerado que contém pares de índice e valor de um iterável (como uma lista ou string). É útil para iterar com acesso ao índice.

- Sintaxe:
```python
enumerate(iterable, start=0)
```
- `iterable`: O iterável a ser enumerado.
- `start`: (Opcional) Índice inicial (padrão é 0).

- Exemplo:
```python
lista = ["Python", "é", "incrível"]
for indice, valor in enumerate(lista, start=1):
    print(f"{indice}: {valor}")
# Saída:
# 1: Python
# 2: é
# 3: incrível
```
