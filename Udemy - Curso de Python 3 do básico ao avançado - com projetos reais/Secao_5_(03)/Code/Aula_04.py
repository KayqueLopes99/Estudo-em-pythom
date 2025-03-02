class Camera:
    # Inicializando com estados primários.
    def __init__(self, nome, filmando='False'):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return
        
        # Se ele não está filmando
        print(f'{self.nome} está filmando.')
        self.filmando = True

    
    def parar_de_filmar(self):
        if not self.filmando: 
            print(f'{self.nome} não está filmando.')
            return
        
        # Se estiver filmando
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando.')


camera_01 = Camera("Canon")
camera_02 = Camera("Sony")

camera_01.filmar()
camera_01.filmar()
camera_01.fotografar()
camera_01.parar_filmar()
camera_01.fotografar()

print("--"*10)

camera_02.filmar()
camera_02.filmar()
camera_02.fotografar()
camera_02.parar_filmar()
camera_02.fotografar()