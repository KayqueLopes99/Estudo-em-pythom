# Python Dunder Methods __repr__ e __str__

class Ponto:
    def __init__(self,x, y):
        self.x = x
        self.y = y

     
#    def __str__(self): # Quam olha o código. 
#       return f"({self.x}, {self.y})"

    def __repr__(self): # Para desenvolvedores.
        class_name = type(self).__name__
        return f"{class_name}(x={self.x}, y={self.y})"
    
    # Da soma p1 + p2 
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)
    def __gt__(self, other):
        result_self = self.x + self.y 
        result_other = other.x + other.y
        return  result_self > result_other
    

  




if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2?', p1 > p2)
    print('P2 é maior que P1?', p2 > p1)

# Se definir com algum deve fazer tudo segundo a ele. 
# Se tiver string nos parâmetros de um método? use __str__