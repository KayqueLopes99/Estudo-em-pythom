# Desafio
# Uma biblioteca está implementando um sistema automatizado para liberar o acesso à área de livros raros. O sistema deve permitir a entrada apenas para visitantes autorizados e com idade mínima de 18 anos. Para isso, é necessário utilizar operadores lógicos, estruturas condicionais (if, else, else if) e conceitos básicos como tipos primitivos e palavras-chave. Desenvolva um programa que verifique se o visitante pode acessar a sala especial.

# Entrada
# O programa deve receber os seguintes valores:

# Um valor booleano indicando se o visitante possui autorização (true ou false)
# Um número inteiro representando a idade do visitante
# Saída
# Deverá retornar uma String com as mensagens:

# "Acesso permitido" se o usuário tiver permissão e for maior ou igual a 18 anos.
# "Acesso negado" se o usuário não tiver permissão.
# "Idade insuficiente" se o usuário tiver permissão, mas for menor de idade.
def main():
    print("Seja bem-vindo a Biblioteca!")
    print("Verificação de idade: ")
    authorized_input = input("Um valor booleano indicando se o visitante possui autorização (true ou false): ").strip().lower()
    authorized = authorized_input == "true"
    age = int(input("Informe sua idade: "))

    if not authorized:
        print("Acesso negado")
    elif age < 18:
        print("Idade insuficiente")
    else:
        print("Acesso permitido")

if __name__ == "__main__":
    main()
