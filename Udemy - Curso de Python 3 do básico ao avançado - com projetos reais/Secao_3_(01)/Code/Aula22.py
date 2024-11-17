entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito
print(True or False) # Se uma for True é True.
print(False or False) # False.
print(0 or False or 0 or 'abc') # Retorna ao valor verdadeiro abc.


senha = input('Senha: ') or 'Sem senha'
print(senha)