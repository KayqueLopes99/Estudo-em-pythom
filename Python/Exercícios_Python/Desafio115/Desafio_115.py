from Sistema import Interface
# Importar tudo = *
from Sistema.Arquivo import *
arq = 'Sistema_dados.txt'

if not arquivo_existe(arq):
    criarArquivo(arq)

Interface.Menu(arq)