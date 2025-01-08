## Módulos - import, from, as e *
### *01* Comando `import`:
- Importa tudo. 
- Importações de bibliotecas para novas funcionalidades.

- Sintaxe:
- ``import (<impotar>) nome_da_biblioteca``
- Coloca-se no início.
- A palavra-chave `import` é usada para importar um módulo para o seu script. Por exemplo:
```python
import sys # <- nomespace
print(sys.platform)
```

- Inteiro: `import nome_modulo`
- Vantagens: você tem o nomespace do módulo.
- Desvantagens: nomes grandes.

- Site com  informações de outras bibibliotecas:
- **# https://docs.python.org/3/py-modindex.html**
## *02* Comando `from`:
- A palavra-chave `from` é usada para importar uma função ou variável específica de um módulo. 
- Podemos importar só o necessário com:
- ``from <nome_da_biblioteca> import <comando>``
```python
from math import pi
```
- Partes: `from nome_modulo import objeto01, ...` 
- Vantagens: nomes pequenos
- Desvantagens: Sem o nomespace do módulo. (variavel com o mesmo nome).


- Neste exemplo, `from math import pi` importa apenas a variável `pi` de `math.py`. Você pode então usar `pi` diretamente, sem precisar prefixá-la com `math.`. Por exemplo:

```python
from math import pi

print(pi)  # Imprime o valor de pi
```
- Podemos colocar para não adicionar várias vezes.

## *03* Comando `as`:
- O comando `as` em Python é usado em várias situações para **atribuir um apelido (alias)** a um item, tornando-o mais fácil de referenciar. 

### Sintaxe
```python
Nome_do_Comando as alias_name_Apelido
```
### `as` em importação do módulo 
- Se quiser usar o mesmo nome do módulo em uma variavel (sobrescrever - Mudar o valor do módulo se colocar o Mesmo nome que ele).
```python
import sys as alias_name_Apelido # será o nome para sys.
from sys import platform as alias_name_Apelido

sys = 123
print(alias_name_Apelido.plataform)
```
- Mude o nome da sua variavel e não do módulo.
- Vantagens: você pode reservar nomes para seu código.
- Desvantagens: pode ficar fora do padrão.


### `as` em Gerenciamento de Contexto (`with`)

Quando usado com `with`, o `as` permite nomear o recurso que está sendo gerenciado, como um arquivo, para facilitar o uso dentro do bloco `with`.

```python
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()  # 'arquivo' é o alias para o arquivo aberto
    print(conteudo)
```

**Vantagens**:
- A variável `arquivo` permite acessar o conteúdo do arquivo com facilidade.
- Quando o bloco termina, o arquivo é fechado automaticamente.

## *04* Comando `*tudo`:
- Má prática de programação. 
- Importar todos dentro de um comando no import.
- `from sys import *`