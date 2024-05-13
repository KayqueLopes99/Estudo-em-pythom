# Comparação de peso 
maior_peso = 0
menor_peso = 0
for i in range(1,6):
    peso = float(input('Informe o peso da {} pessoa: '.format(i))) 
    if i == 1: # Primeira pessoa, passando os pessos para inicializar o menor com 0.
      maior_peso = peso
      menor_peso = peso
    else:
        # Se outro peso for maior que o primeiro, teremos.
        if peso > maior_peso:
           maior_peso = peso

print("A pessoa com o maior peso. Seu peso é {}.".format(maior_peso))
print("A pessoa com menor peso. Seu peso é {}.".format(menor_peso))
