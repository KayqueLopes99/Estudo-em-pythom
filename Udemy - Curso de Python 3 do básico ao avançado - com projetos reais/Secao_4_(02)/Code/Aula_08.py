# Funções são da mesma classe que as varíaveis no python.
def saudacao(msg):
    return msg


saudacao_2 = saudacao # Aponta para mesma função de saudacao.
# referenciando na memória. 

variavel = saudacao_2("Good")
print(variavel)



# Está função executa vai fazer funcionar a outra função saudacao.

def executa(funcao, msg):
    return funcao(msg)

variavel_01 = executa(saudacao, "Great")
print(variavel_01)



# Empacotar no parametro e desempacotar no return.
def saudacao2(msg, nome):
    return f'{msg}, {nome}!'


def executa1(funcao, *args):
    return funcao(*args)


print(
    executa1(saudacao2, 'Bom dia', 'Luiz')
)
print(
    executa1(saudacao2, 'Boa noite', 'Maria')
)