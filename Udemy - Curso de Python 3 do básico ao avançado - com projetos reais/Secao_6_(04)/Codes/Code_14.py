from threading import Thread, Lock
from time import sleep

class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()
    
    def run(self):
        sleep(self.time)
        print(self.text)


text1 = MyThread('Thread 1', 5)
text2 = MyThread('Thread 2', 10)
text3 = MyThread('Thread 3', 15)
text1.start()
text2.start()
text3.start()



def demore(text, time):
    sleep(time)
    print(text)

text4 = Thread(target=demore, args=('Olá mundo!', 5))
text4.start()

while text1.is_alive():
    print("Aguardando a finalização da Thread.")
    sleep(2)


for i in range(20):
    print(i)
    sleep(1)


# QUANDO REALIZAMOS OPERAÇÕES QUE DEMANDAM TEMPO NO MEIO DO PROCESSO DAS THREADS, OCORRE ERROS. 
class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método para esperar 
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)