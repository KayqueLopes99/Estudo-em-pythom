# Atributos de classe
class Usuario:
    ano_atual = 2025 # Usada em todas as funções

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Usuario.ano_atual - self.idade
        

p1 = Usuario("Kayque", 20)
p2 = Usuario("Aparecida", 19)

print(Usuario.ano_atual)

# se mudar o ano aqui muda os cálculos relacionados. 

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


## Dicionario

print(p1.__dict__)