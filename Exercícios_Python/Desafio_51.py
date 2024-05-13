# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Informe o primeiro termo da progressão: '))
razao = int(input('Informe a razão da progressão: '))

for i in range(10):
    termo = primeiro_termo + i*razao
    print("Termo {}: {}".format(i+1, termo))
   