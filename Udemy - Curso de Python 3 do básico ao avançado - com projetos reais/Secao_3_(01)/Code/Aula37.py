contador = 0

while contador <= 100:
    contador += 1 # Atualização sempre.

    if contador == 6:
        print("Não vou mostrar o 6.")
        continue # Dentro de condições e repetição aninhada.

    if contador >= 10 and contador <= 27:
        print(f"Não vou mostrar o {contador}")
        continue

    print(contador)

    if contador == 40:
        break

print("-"*10)