## Operador de associação:
- São operadores utilizados para verificar se um objeto está presente em uma sequência. 
## Operadores in e not in
- **in: está entre**.
- Strings são iteráveis (Navegar Item por Item).
- Se um Item está ou não está no Local escolhido podendo ser uma variavel, estrutura e etc
- not in: não está entre.
- **Retorna a um boll**
- Começo do Zero.
```
 0 1 2 3 4 5
 O t á v i o
-6-5-4-3-2-1
```

- tipo(Varíavel[indice]) -> Retorna a Letra.
- Sintaxe:
```
Item in Local
```
- Retorna a um boll(False ou True).

```python
nome = 'Kayque'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[-3])
print(nome[-2])
print(nome[-1])

print("-" * 10)

print('que' in nome) # True
print('Ky' in nome) # False
print("-" * 10) 
print('que' not in nome) # False
print('Ky' not in nome) # True

nome = input("Digite seu nome: ")
encontrar = input("Digite o ue deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está no seu Nome {nome}.")
else:
    print(f"{encontrar} não está em {nome}")
```


## Comando In 2.0:
- O operador **`in`** em Python é utilizado para verificar se um determinado elemento está presente em uma sequência, estrutura de dados ou iterável. Ele retorna um valor **booleano (`True` ou `False`)**, dependendo da existência do item.

- Sintaxe:

```python
elemento in estrutura
```

- Verificando a Presença de um Item em uma Lista
- Verificando em Tuplas
- Verificando em Conjuntos (`set`)
- Verificando a Existência de uma Chave em um Dicionário
- Verificando Caracteres em Strings

📌 Para grandes coleções, **prefira `set` ao invés de `list`**