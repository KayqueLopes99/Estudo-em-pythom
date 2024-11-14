# if  / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Entrou.')

elif entrada == 'sair':
    print("Saiu.")

else:
    print("Nada escolhido.")

print("Fora do bloco.")