def Print():
    print("Bloco de código 1.")
    print("Bloco de código 2.")
    print("Bloco de código 3.")
    print("Bloco de código 4.")

# Parametro
def imprimir(a,b,c):
    print(a, b, c)
    print(a+b+c)



# argumento
imprimir(1, 2, 3)

# Mudar
imprimir(4, 5, 6)

# Se não passar um valor
def saudacao(nome='Desconhecido'):
    print(f"Olá, {nome}!")

saudacao("Kay")
saudacao()