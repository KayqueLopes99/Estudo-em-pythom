## Detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
## Iterável (`Iterable`)
- Um **Iterável** é qualquer objeto que pode ser percorrido (iterado) **um item de cada vez**, como listas, tuplas, dicionários, conjuntos e strings.
- Resposabilidade de deter os valores sequencialmente.
- Se um objeto tem o método `__iter__()`, significa que ele **é um Iterável**.

```python
lista = [1, 2, 3]
print(hasattr(lista, "__iter__"))  # True, ou seja, é um Iterável
```

## Iterador (`Iterator`)  
- Um **Iterador** é um objeto que **fornece os elementos de um Iterável um por um** quando usamos a função `next()`.
- Responsabilidade de entregar um valor por vez, ou seja, o próximo valor.
- Ele possui o método `__next__()`, que retorna o próximo item da sequência.  

- Transformar um Iterável em Iterador - `iter()`.
- Funcionamento como um ponteiro que vai se atualizando até o final.
---
## Generator expression, Iterables e Iterators em Python
- Generator: Funções que sabem pausar em determinado ponto. 
- É uma forma compacta de criar **geradores**, parecida com as **List Comprehensions**, mas sem criar toda a lista na memória.  
---

- List Comprehension = Cria toda a lista na memória
- Generator Expression = Gera um valor por vez, sem armazenar tudo.
- Para Percorrer um Generator pode-se usar `next()` ou um `for`.

🔹 **Exemplo Comparativo**  
```python
# List Comprehension (Cria uma lista inteira na memória)
lista = [x * 2 for x in range(5)]
print(lista)  # Saída: [0, 2, 4, 6, 8]

# Generator Expression (Cria um gerador)
generator = (x * 2 for x in range(5))
print(generator)  # Saída: <generator object at 0x...>

# Obtendo valores do generator com next()
print(next(generator))  # 0
print(next(generator))  # 2
print(next(generator))  # 4
```

- A sintaxe é parecida com a List Comprehension, mas usa  `( )` em vez  `[ ]`.
```python
generator = (expressão for item in iterável if condição)
```

- **Verificar o Tamanho**: `com import sys sys.getsizeof(Elemento_para_saber_o_tamanho_em_Bytes)`.
- Com a lista normal podeos *acessar os valores* já do generator não. 























---

##  Funcionamento do For (next, iter, iterável e iterador)
- Iterável -> Tem os valores 
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
