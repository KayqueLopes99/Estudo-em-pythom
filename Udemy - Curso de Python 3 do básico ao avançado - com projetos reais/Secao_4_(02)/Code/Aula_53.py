caminho_arquivo = "C:\\Users\\kaiqu\\OneDrive\\Imagens\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_4_(02)\\Code\\" # Caminho completo do arquivo. 

caminho_arquivo += 'Aula_53.txt'  # Concatenarr.
# arquivo = open(caminho_arquivo, 'w')

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá Mundo.')
    print("Arquivo Fechado automaticamente.")
    
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write("Linha 1 - KÃYÇUE\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(
        ("Linha 3\n", 'Linha 4\n') # Iterável.
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    print("Lendo")
    arquivo.seek(0, 0) # Mandando para cima.
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print("#" * 10)
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())