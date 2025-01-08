## Módulos:
- São Pré-definidos.
- Importações de bibliotecas para novas funcionalidades.
- Sintaxe:
. import (<impotar>) nome_da_biblioteca
- Coloca-se no início.
* Podemos importar só o necessário com:
. from <nome_da_biblioteca> import <comando>

# Importando Módulos em Python
- Em Python, um módulo é um arquivo contendo definições e instruções Python. O nome do arquivo é o nome do módulo com o sufixo `.py` adicionado.

## Importando Várias Funções ou Variáveis

Você pode importar várias funções ou variáveis de um módulo usando a sintaxe `from ... import ...`. Por exemplo:

```python
from math import pi, sqrt
```

Neste exemplo, `from math import pi, sqrt` importa as variáveis `pi` e a função `sqrt` de `math.py`. Você pode então usar `pi` e `sqrt` diretamente, sem precisar prefixá-las com `math.`.


```