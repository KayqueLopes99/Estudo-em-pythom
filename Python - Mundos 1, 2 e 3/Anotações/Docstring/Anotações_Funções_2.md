# Fuções 02:
- Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.

## Interacive Heap:
- O comando `help` fornece informações detalhadas sobre outros comandos, módulos, classes, métodos e objetos em Python.
### Como Usar
#### 1. `help()` sem argumentos
```python
help()
```
#### 2. `help(objecto ou comando)`
Usando `help()` com um argumento, você obtém a documentação desse comando ou objeto específico.
**Exemplo com uma função**:
```python
help(print)
```

**Exemplo com um módulo**:
```python
import math
help(math)
```

### Impressão Doc
- **Impressão da docstring de uma função ou método específico**:
   Quando uma função tem uma docstring, podemos imprimir essa documentação para entender o que ela faz e como usá-la.

+ Exemplo:
   ```python
   print(input.__doc__)
   ```

-  **Aplicação prática**:
   Ao imprimir `__doc__`, o desenvolvedor pode consultar rapidamente o propósito e a forma de usar uma função sem precisar buscar em documentação externa, o que economiza tempo e facilita a codificação.

### Docstrings

- Docstrings são uma prática de documentação em Python e servem para descrever o que uma função, método, classe ou módulo faz. Elas são declaradas usando aspas triplas `"""` logo após a definição do código. 

+ **Estrutura das Docstrings**:
   Docstrings são strings de várias linhas que podem incluir:
   - Uma descrição breve da funcionalidade.
   - Uma lista de parâmetros com seus tipos e propósitos.
   - Uma seção de retorno, explicando o tipo de dado retornado e seu significado.

   Exemplo de docstring para uma função:
   ```python
   def soma(a, b):
       """
       Calcula a soma de dois números.

       Parâmetros:
       a (int, float): O primeiro número a ser somado.
       b (int, float): O segundo número a ser somado.

       Retorna:
       int, float: O resultado da soma entre 'a' e 'b'.
       """
       return a + b
   ```

- Acessar docstrings é fácil: em qualquer função ou método documentado, basta usar `print(funcao.__doc__)` para exibir a descrição.


