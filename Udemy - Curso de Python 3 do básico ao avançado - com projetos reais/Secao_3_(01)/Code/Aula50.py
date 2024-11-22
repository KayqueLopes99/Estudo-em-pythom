# Exercício - exiba os índices da lista (aula com solução)

lista_1 = ['Maria Isabelly', 'Letícia vieira', 'Aparecida', 'Maria Eduarda', 'Cibely']
lista_1.append("Karine")


indice = 0
for nomes in lista_1:
    print(f"[{indice}]: [{nomes}]")
    indice += 1

"""
indices = range(len(lista_1))
for indice in indices:
    print(f"[{lista_1[indice]}]: [{indice}]") 
"""