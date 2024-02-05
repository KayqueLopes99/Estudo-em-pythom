# Dolares

dinheiro = float(input("Informe a quantidade de dinheiro que você tem: "))
taxa_dolar = float(input("Informe a taxa de câmbio atual do dólar: "))
taxa_euro = float(input("Informe a taxa de câmbio atual do euro: "))

dolares = dinheiro * taxa_dolar
euro = dinheiro * taxa_euro

print('Quantidade de dinheiro: {:.2f}'.format(dinheiro))
print('Quantidade de DOLAR convertido: {:.2f}'.format(dolares))
print('Quantidade de EURO convertido: {:.2f}'.format(euro))
