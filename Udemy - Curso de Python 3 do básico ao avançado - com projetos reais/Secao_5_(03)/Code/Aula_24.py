CAMINHO = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_5_(03)\\Code\\Aula_24.txt"
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo Arquivo.")
        arquivo =  open(caminho_arquivo, modo, encoding='utf8')  
        yield arquivo 
    except Exception as e:
        print("Erro:", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()


with my_open(CAMINHO, "w") as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)