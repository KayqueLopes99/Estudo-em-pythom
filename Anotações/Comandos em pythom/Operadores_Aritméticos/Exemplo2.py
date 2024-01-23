# formulas criadas para calculo e treino de precedência. maneira 2
numero_1 = float(input('Digite um algarismo primeiro: \n'))
numero_2 = float( input('Digite um algarismo segundo: \n'))
numero_3 = float( input('Digite um algarismo terceiro: \n'))
resultado = (numero_1 + (numero_2 * numero_3))
resulta = ((numero_1 * numero_2) + (numero_2 ** numero_3))
print('formula:\nnumero_1 + numero_2 * numero_3')
print("Resultado: {}".format(resultado))

print('formula:\n (numero_1 * numero_2) + (numero_2 ** numero_3)')
print("Resultado: {}".format(resulta) )

''' formulas criadas para calculo e treino de precedência. maneira 1
numero_1 = float(input('Digite um algarismo primeiro: \n'))
numero_2 = float( input('Digite um algarismo segundo: \n'))
numero_3 = float( input('Digite um algarismo terceiro: \n'))

print('formula:\n numero_1 + numero_2 * numero_3')
print("Resultado: ", numero_1 + (numero_2 * numero_3))

print('formula:\n (numero_1 * numero_2) + (numero_2 ** numero_3)')
print("Resultado: ", ((numero_1 * numero_2) + (numero_2 ** numero_3)))
'''