class AppSettings:
    _instance = None
    
    # Um única instancia
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        
        return cls._instance
    
    # Problema multiplas chamada do __init__
    def __init__(self):
        pass
    
    

if __name__ == "__main__":
    
    as1 = AppSettings()
    as2 = AppSettings()
    
    print(as1)
    print(as2)
    
    