from ..Interface.__init__ import cabeçalho_Center
def arquivo_existe(nome):
    """ Função para verificar se o arquivo existe no local

    Args:
        nome (srt): Nome do arquivo

    Returns:
        _True/False_: existe ou não?
    """
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        # WT+ = Criar o arquivo
        arquivo_constrir = open(nome, 'wt+')
        arquivo_existe.close()
    except FileExistsError:
        print('\033[91mHouve um ERRO na criação do arquivo.\033[m')
    else:
        print(f'\033[92mArquivo {nome} Criado com sucesso.\033[m')

def lerArquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except:
        print(f"\033[91mArquivo {nome} com Erro na criação\033[m")
    else:
        cabeçalho_Center('Usuários Cadastrados')
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f'{dado[0]:<30} {dado[1]:>3} anos')


        print(abrir.read())
    finally: 
        abrir.close()

def cadastrar_pessoas(arq, nome='Desconhecido', idade=0):
    try:
        abrir_arquivo = open(arq, 'at')
    except:
        print(f"\033[91mArquivo {nome} com Erro para Abertura\033[m")
    else:
        try:
            abrir_arquivo.write(f'{nome};{idade}\n')
        except:
            print(f"\033[91mArquivo {nome} com Erro para Escrita\033[m")
        else: 
            print(f"\033[92mNovo Registro Adicionado de {nome}.\033[m")
            abrir_arquivo.close()
            
            

       

    