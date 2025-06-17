import os

caminho = os.path.join('C:', 'Users', 'User', 'Documents', 'file.txt')

print(caminho)
diretorio, arquivo = os.path.split(caminho)

print(f'Diretorio: {diretorio}')
print(f'Arquivo: {arquivo}')


print(os.path.exists(caminho))

print(os.path.abspath('.'))
print(os.path.basename(caminho))