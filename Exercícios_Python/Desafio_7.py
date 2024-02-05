# Converção de metros
numero_metro = float(input("Insira o algarismo para conversao de metro -> centimentro e depois em milimetros"))
centimentro = numero_metro * 100
milimetro = numero_metro * 1000
kilometro = numero_metro / 1000

print('Metro convertido em CM: {:.2f}'.format(centimentro))
print('Metro convertido em MM: {:.2f}'.format(milimetro))
print('Metro convertido em KM: {:.2f}'.format(kilometro))