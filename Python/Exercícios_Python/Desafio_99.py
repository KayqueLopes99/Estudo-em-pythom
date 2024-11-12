def maior(numero, maior_numero_atual):
    if numero > maior_numero_atual:
        maior_numero_atual = numero
    return maior_numero_atual


maior_numero = 0
numeros_digitados = []

while True:
   print("-"*20)
   resposta = int(input("Deseja Começar?\n(1-sim)\n(2-não)\nResposta: "))
   if resposta == 1:
    qtd = int(input("Informe a Quantidade de Números: "))
    
    for i in range(qtd):
       numero = int(input(f"Informe o {i + 1} Número:"))
       numeros_digitados.append(numero)
       maior_numero = maior(numero, maior_numero)

    print("-"*20)
    print(f"Números digitados: {numeros_digitados}")
    print(f"O maior número informado é: {maior_numero}\nNúmero de Valore: {qtd}")
    print("-"*20)
    
   if resposta == 2:
      print("\033[91mSaindo...\033[m")
      break
