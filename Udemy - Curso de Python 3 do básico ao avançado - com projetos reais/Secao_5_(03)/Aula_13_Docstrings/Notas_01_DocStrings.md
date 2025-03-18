## dir e help + DocStrings de uma linha (Documentação)

### dir():
- Impressão das funcionalidades do seu módulo.
- dei(module) e retorna a uma lista de strings. 
### Interacive Heap:
- O comando `help` fornece informações detalhadas sobre outros comandos, módulos, classes, métodos e objetos em Python.
-`help()` 
-  Usando `help()` com um argumento, você obtém a documentação desse comando ou objeto específico.

### Impressão Doc
- **Impressão da docstring de uma função ou método específico**:
   Quando uma função tem uma docstring, podemos imprimir essa documentação para entender o que ela faz e como usá-la.

+ Exemplo:
   ```python
   print(input.__doc__)
   ```

- Ao imprimir `__doc__`, o desenvolvedor pode consultar rapidamente o propósito e a forma de usar uma função sem precisar buscar em documentação externa, o que economiza tempo e facilita a codificação.

### Docstrings
- Descrever o que uma função, método, classe ou módulo faz. 
- Elas são declaradas usando aspas triplas `"""`. 

+ **Estrutura das Docstrings**:
   Docstrings são strings de várias linhas que podem incluir:
   - Uma descrição breve da funcionalidade.
   - Uma lista de parâmetros com seus tipos e propósitos.
   - Uma seção de retorno, explicando o tipo de dado retornado e seu significado.

   ``` py
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

- Acessar docstrings:  `print(funcao.__doc__)` para exibir a descrição.

## Em classes
- Segue a mesma lógica.
- 