
# Ex:
# with open("aula21.txt", "w") as arquivo:
# ...

CAMINHO = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_5_(03)\\Code\\Aula_23.txt"


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print("Abrindo Arquivo.")
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding='utf8')   
        return self._arquivo
    

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()
        

with MyOpen(CAMINHO, "w") as arquivo: # algo: Do enter
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)