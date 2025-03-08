# Herança Multipla.
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def imprimir_informacao_01(self):
        return f"Nome: {self.nome}"


class Mamifero(Animal):
    def __init__(self, classificacao, animal):
        super().__init__(animal)
        self.classificacao = classificacao
    
    def imprimir_informacao_02(self):
        return f"Classificação: {self.classificacao}"


class Herbivoro(Animal):
    def __init__(self, herbivoro, animal):
        super().__init__(animal)
        self.herbivoro = herbivoro
    
    def imprimir_informacao_03(self):
        return f"Tipo: {self.herbivoro}"


class Aquatico(Mamifero, Herbivoro):
    def __init__(self, nome, ambiente, classificacao, herbivoro):
        Animal.__init__(self, nome)  # Inicializa apenas Animal diretamente
        self.classificacao = classificacao  # Define Mamífero manualmente
        self.herbivoro = herbivoro  # Define Herbívoro manualmente
        self.ambiente = ambiente  # Define o ambiente
    
    def imprimir_informacao_04(self):
        print(f"{self.imprimir_informacao_01()}, {self.imprimir_informacao_02()}, {self.imprimir_informacao_03()}, Ambiente: {self.ambiente}")


# Criando um objeto Aquatico
a1 = Aquatico("Golfinho", "Marinho", "Mamífero", "Herbívoro")
a1.imprimir_informacao_04()

# - A ordem importa: quanto mais no começo, mais ele vai procurar neste local, ou seja, procura no mais a esquerda. 

