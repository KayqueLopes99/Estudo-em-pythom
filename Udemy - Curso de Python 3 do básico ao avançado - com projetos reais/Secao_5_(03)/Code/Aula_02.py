class Car:
    # Inicialização.
    def __init__(self, name="-"):
        self.name = name
    
    # Métodos e Ações
    def accelerate(self):
        print(f'{self.name} está acelerando!')

model_fusca = Car("Fusca")
print(model_fusca.name)
model_fusca.accelerate

model_celta = Car("Celta")
print(model_celta.name)
model_celta.accelerate
