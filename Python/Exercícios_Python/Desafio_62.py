# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

limite = int(input("Deseja Quantos Termos?"))
while limite != 0:

    primeiro_termo = int(input('Informe o primeiro termo da progressão: '))
    razao = int(input('Informe a razão da progressão: '))
    i = 0

    while i < limite:
        termo = primeiro_termo + i*razao
        print("Termo {}: {}".format(i+1, termo))
        i += 1
    limite = int(input("Deseja Quantos Termos? "))
print("Saiu!!!")