numero = int(input('Informe um número: '))
limite = int(input('Informe um Limite: '))
while limite < numero:
     limite = int(input('Informe um Limite valido: '))
if limite == numero:
     print('Algarismos Iguais!')
else:
    for i in range(numero,limite):
         print(numero)
         numero += 1
         
print('Fim!')