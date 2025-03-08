# Classe Pai generica.
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def imprimir_dados(self):
        print(self.nome, self.sobrenome, self.idade, self.__class__.__name__)

    def exibir_info(self):
        return f"Nome: {self.nome}, Sobrenome: {self.sobrenome}, Idade: {self.idade}"

# Classe Filha.
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, idade, cpf):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
    
    def exibir_info(self):
        return f"{super().exibir_info()}, Cpf: {self.cpf}"

c1 = Cliente("Kayque", "Lopes", 20, 12345678)
print()

print(c1.exibir_info())
