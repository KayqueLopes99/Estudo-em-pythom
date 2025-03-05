# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class People:
    year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @classmethod
    def method_the_class(cls):
        print("Hey")


    @classmethod
    def create_with_50_years_old(cls, name):
        return cls(name, 50)

    @classmethod
    def create_anonymous(cls, idade):
        return cls("Anônimo(a)", idade)
    
p1 = People('João', 34)
p2 = People.create_with_50_years_old('Helena')
p3 = People('Anônima', 23)
p4 = People.create_anonymous(25)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)
print(p4.name, p4.age)



    
