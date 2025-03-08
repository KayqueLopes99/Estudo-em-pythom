# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None 
        self.fabricante = None 
        

    def inserir_informacoes(self,motor, fabricante):
        self.motor = motor
        self.fabricante = fabricante
        
    
    def listar_documentacao(self):
        print("-" * 25)
        print(f"Carro: {self.nome}")
        print(f"Motor: {self.motor.nome}")
        print(f"Fabricante: {self.fabricante.nome}")  
        print("-" * 25)



class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def  __init__(self, nome):
        self.nome = nome


carro_01 = Carro("Fusca")
motor_01 = Motor("Eletrico")
fabricante_01 = Fabricante("Volkswagen")

carro_01.inserir_informacoes(motor_01, fabricante_01)
carro_01.listar_documentacao()

carro_02 = Carro("Uno")
motor_02 = Motor("Combustão")
fabricante_02 = Fabricante("Fiat")

carro_02.inserir_informacoes(motor_02, fabricante_02)
carro_02.listar_documentacao()
