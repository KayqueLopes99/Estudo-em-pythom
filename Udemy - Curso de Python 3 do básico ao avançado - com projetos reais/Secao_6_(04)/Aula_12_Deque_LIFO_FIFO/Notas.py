# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
#
# Lifo  e fifo
# pilha e fila

# -> O primeiro a entrar na fila vai ser o primeiro a siair a fila.

# -> O primeiro a entrar na pilha será o ulltimoa sair

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Legal (LIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)
#  0  1  2  3  4  5  6  7  8  9  10, 11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ultimo_removido = lista.pop()
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Último: ', ultimo_removido)
print('Lista:', lista)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🚫 Ruim (FIFO com lista) -> REPASSANDO OS ELEMENTOS PARA UM LADO QUANDO INSERE UM ELEMENTO NO INDICE 0.
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 10)
#   0  1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 11)
#  0   1   2  3  4  5  6  7  8  9, 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista.pop(0)  # 11
#  0   1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro: ', primeiro_removido)  # 11
print('Lista:', lista)  # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante

# ✅ Legal (FIFO com deque)
# De forma resumida, deque é mais rápido para inserir e remover elementos da frente da fila (no índice 0).
fila_correta: deque[int] = deque()
fila_correta.append(3)  # Adiciona no final
fila_correta.append(4)  # Adiciona no final
fila_correta.append(5)  # Adiciona no final
fila_correta.appendleft(2)  # Adiciona no começo
fila_correta.appendleft(1)  # Adiciona no começo
fila_correta.appendleft(0)  # Adiciona no começo
print(fila_correta)  # deque([0, 1, 2, 3, 4, 5])
fila_correta.pop()  # 5
fila_correta.popleft()  # 0
print(fila_correta)  # deque([1, 2, 3, 4])

# REMOVEU O PRIMEIRO ELEMENTO.
head = fila_correta.popleft()
print(head)