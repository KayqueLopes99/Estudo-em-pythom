# Desafio
# Você está desenvolvendo um sistema simples para um e-commerce que deseja registrar os valores das compras realizadas por um cliente ao longo de um único dia. O sistema deve primeiro receber a quantidade total de compras realizadas e, em seguida, solicitar o valor de cada uma dessas compras. Ao final, o sistema deve exibir o total gasto no dia e a média de valor por compra.

# Entrada
# A entrada deve receber:

# Um número inteiro N que indica a quantidade de compras realizadas no dia.
# Em seguida, N números do tipo double, cada um representando o valor de uma compra.
# Saída
# O programa deverá retornar:

# O total das compras com duas casas decimais
# A média de valor por compra com duas casas decima
# Se N for 0 (ou seja, nenhuma compra registrada), o programa deverá exibir: "Nenhuma compra registrada."

def main():
    purchase_count = int(input())

    if purchase_count == 0:
        print("Nenhuma compra registrada.")
    else:
        total_spent = 0.0
        i = 1

        while i <= purchase_count:
            try:
                purchase_value = float(input())
            except ValueError:
                continue  

            if purchase_value < 0:
                continue  
            else:
                total_spent += purchase_value
                i += 1

        average_purchase = total_spent / purchase_count

        print(f"{total_spent:.2f}")
        print(f"{average_purchase:.2f}")

if __name__ == "__main__":
    main()