condicao = 10 == 11 # Condição. 
#                       True          False
#                    Vice versa dependendo do código. 
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)


digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)


print('Valor' if False else 'Outro valor' if False else 'Fim')