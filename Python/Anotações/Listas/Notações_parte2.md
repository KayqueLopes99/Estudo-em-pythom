# Listas parte 2 em python
## Varíaveis Compostas.
### Colocar uma lista dentro de outra
```` python
dados = list()
dados.append('Pedro')
dados.append('25')
pessoas = list()
# Dá append numa estrutura.
pessoas.append(dados[:])
# Temos uma copia de dados para a lista pessoas da lista dados.
````
- Logo a lista vai ficar:
````
pessoas
[['Pedro'][25]]  [['Maria'][19]]  
[    0      1 ]  [    0      1 ]  ...
        0                 1
````

-> Declarar: 
``` python
pessoas = [['Pedro', 25], ['Maria', 23], ['Marta',35]]
# Teremos três Lista, ou seja listas compostas.
```
## Declaração de listas compostas:
````python
lista = list()
lista1 = [[], []]
lista2 = []
lista3 = []
lista.append(lista2, lista3)
````
- No exercicio 84 e 85 tem umas sugestões.
# Comandos:
### No print
``` python
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]
```
- [Indice_da_Lista][Posição_do_elemento]
### A diferença entre usar `[:]` e não usar `[:]` 
```python 
teste = list()
teste.append("Kay")
teste.append(19)
galera = list()
# A partir desse momentos as listas estão ligadas se alterar uma coisa em uma a outra também vai alterar.
'''
galera.append(teste)
teste[0] = "Maria"
teste[1] = 20
galera.append(teste)
print(galera)
saida: [['Maria', 20], ['Maria', 20]]
'''

galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 20
galera.append(teste[:])
print(galera)
```

- **Sem `[:]` (Cópia por Referência):**
    - Em `galera.append(teste)`, adicionamos uma **referência** à lista `teste` à lista `galera`. Isso significa que ambas as listas apontam para o **mesmo objeto** na memória.
    - Qualquer alteração feita em `teste` também afetará `galera`, porque elas compartilham os mesmos dados.
    - No exemplo, quando altera `teste[0]` e `teste[1]`, essas mudanças são refletidas em ambas as listas, resultando em `[['Maria', 20], ['Maria', 20]]`.

- **Com `[:]` (Cópia por Valor):**
    - Em `galera.append(teste[:])`, criamos uma **cópia** dos elementos da lista `teste` e adicionando essa cópia à lista `galera`.
    - logo, `galera` contém uma cópia independente dos dados originais em `teste`.
    - Portanto, ao alterar `teste[0]` e `teste[1]`, essas mudanças **não afetam** a lista `galera`. A saída será `[['Kay', 19], ['Maria', 20]]`.

- Em modificação nos elementos da lista dentro do loop (por exemplo, alterando valores ou adicionando/removendo elementos), aí sim seria relevante usar [:].


#### Em resumo:
- Sem `[:]`: As listas compartilham o mesmo objeto (alterações em uma afetam a outra).
- Com `[:]`: As listas são independentes (alterações em uma não afetam a outra).
## clear()
- Usado para **remover todos os elementos de uma lista**. Quando você chama `lista.clear()`, a lista fica vazia, sem nenhum item.
- **Exemplo**:
  ```python
  frutas = ['maçã', 'banana', 'cereja', 'laranja']
  frutas.clear()
  print(frutas)  # Saída: []
  ```