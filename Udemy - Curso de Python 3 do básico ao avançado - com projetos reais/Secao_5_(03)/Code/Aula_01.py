class Pessoa:
    # O **self** representa o próprio objeto e
    # é usado para armazenar os valores passados na criação da instância. 
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def apresentar(self):
        print(f"Olá me chamo {self.nome} e meu sobrenome é {self.sobrenome}")
    

p1 = Pessoa('Kayque', 'José')
# p1.nome = 'José'
# p1.sobrenome = 'Kayque'

p2 = Pessoa('Isabelly', 'Maria')
# p2.nome = 'Maria'
# p2.sobrenome = 'Isabelly'

p1.apresentar()
p2.apresentar()