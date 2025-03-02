class Animal:
    # name = "lion"

    def __init__(self, name):
        self.name = name

        variable = "value"
        print(variable)

    def eating(self, food):
        return f"{self.name} eat {food}"
    
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)
    


lion = Animal(name="Lion")
print(lion.name)
print(lion.execute("Apple"))
