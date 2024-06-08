Lista_Elementar = []
for cont in range(0,5):
    Lista_Elementar.append(int(input("Informe um valor: ")))

for c, v in enumerate(Lista_Elementar):
    print(f'\033[36m*** Posição {c} Valor {v} *** \033[m ')
print("Fim.")