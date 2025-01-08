def sum_the_variables_modules(x, y):
    if verification(x, y):
        return x + y

def diference_the_variables_modules(x, y):
    if verification(x, y):
        return x - y

def multiplication_the_variables_modules(x, y):
    if verification(x, y):
       return x * y

def division_the_variables_modules(x, y):
    if y == 0:
            return "\033[91mErro: Não é possível dividir por zero.\033[m"   
     
    if verification(x, y):
       return x / y
    return None

def verification(x, y):
    if not isinstance(x, (float)) and not isinstance(y, (float)):
        print("\033[91mErro: Por Favor Digite um Algarismo válido.\033[m")        
    return True
            
             

