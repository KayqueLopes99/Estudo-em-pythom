# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Informe o primeiro termo da progressão: '))
razao = int(input('Informe a razão da progressão: '))
i = 0
while i < 10:
    termo = primeiro_termo + i*razao
    print("Termo {}: {}".format(i+1, termo))
    i += 1
