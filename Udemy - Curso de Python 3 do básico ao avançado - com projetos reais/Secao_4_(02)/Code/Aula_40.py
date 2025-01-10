# Exercício - Adiando (Só depois) execução de funções (Closure)
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# *args = x.
def criar_funcao(funcao, *args):
    """
    Closure: Esta função recebe outra função (funcao) e argumentos fixos (*args).
    Ela retorna uma nova função (mandar) que "lembra" desses argumentos e 
    adia a execução da função original até receber o argumento final (y).
    """
    def mandar(y):  
        # A função interna "mandar" recebe 'y' quando for chamada mais tarde.
        # Ela "lembra" dos argumentos (*args) que foram passados antes,
        # mesmo depois que 'criar_funcao' já terminou sua execução.
        return funcao(*args, y)  
    
    return mandar  # Retorna a função interna sem executá-la ainda (Closure)


# Criando novas funções a partir da função base, com argumentos pré-definidos
soma_com_cinco = criar_funcao(soma, 5)  # A função retornada sempre somará 5 ao valor passado depois
multiplica_por_dez = criar_funcao(multiplica, 10)  # Sempre multiplicará o valor passado por 10

# Chamando as funções armazenadas
print(soma_com_cinco(4))  # 5 + 4 = 9
print(multiplica_por_dez(4))  # 10 * 4 = 40
