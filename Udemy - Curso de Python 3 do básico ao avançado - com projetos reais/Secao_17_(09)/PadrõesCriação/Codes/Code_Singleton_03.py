# Usando meta classes
class Singleton(type):
    _instances: dict = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        
        return  cls._instances[cls]
    

class AppSettings(metaclass=Singleton):
    # Problema multiplas chamada do __init__
    def __init__(self):
        print("...")
        self.tema = "O tema escuro"
    
    
if __name__ == "__main__":
    
    as1 = AppSettings()
    as1.tema = "O tema claro"
    print(as1.tema)
    
    as2 = AppSettings()
    print(as1.tema)    
    