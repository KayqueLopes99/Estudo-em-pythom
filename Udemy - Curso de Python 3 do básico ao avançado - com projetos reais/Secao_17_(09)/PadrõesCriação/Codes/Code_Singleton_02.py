
def singleton(the_class):
    instances = {}
    
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        
        return instances[the_class]
    
    return get_class




@singleton
class AppSettings:
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
    