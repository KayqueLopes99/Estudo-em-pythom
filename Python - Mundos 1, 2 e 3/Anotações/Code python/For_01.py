inicio = int(input('Informe o inicio: '))

fim = int(input('Informe o fim: '))

passo = int(input('Informe o passo: '))

for i in range(inicio,fim,passo):
    print(i)
print('Fim')

print("Agora com Calculos.")

s = 0
for c in range(0,3):
    n = int(input('Informe um algarismo: '))
    s += n
print('O somátorio de todos os valores: {}'.format(s))
    