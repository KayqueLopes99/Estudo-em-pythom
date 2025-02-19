## Problema dos parâmetros mutáveis em funções Python
- Utilização em funções com lista [] no parâmetro. Isso parece correto,mas não é, pois o parâmetro sempre deve ser colocado(o mesmo). 
- Reutilização de um parâmetro mutável.
- Uma das soluções séria usar a lista fora do escopo da estrutura. A ideal é não usar parâmetro pradrões mutaveis.
- Ou seja, podemos associar um valor imutável como **none** para este parâmetro imutável.
- Assim, para não ficar sempre repetindo e utilizando a mesma estrutura (o mesmo parâmetro) pode-se fazer isso. 

- Exemplo da solução: 


```py
# Problema dos parâmetros mutáveis em funções Python
# Lista = None para não ser preciso ficar revendo a llista a cada chamada da função.
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)
print(cliente1)
print(cliente2)
print(cliente3)
```