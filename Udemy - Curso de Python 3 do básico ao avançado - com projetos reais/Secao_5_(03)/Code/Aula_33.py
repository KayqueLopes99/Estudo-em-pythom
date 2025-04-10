from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        # Índice auxiliar para controle da iteração (__next__)
        self._next_index = 0

    def funcion_append(self, *values):
        # Adiciona um ou mais valores à estrutura, armazenando no dicionário
        for value in values: 
            self._data[self._index] = value
            self._index += 1  

    def __len__(self):
        # Retorna o número de elementos armazenados
        return self._index

    def __getitem__(self, index):
        # Retorna o item correspondente ao índice
        return self._data[index]

    def __setitem__(self, index, value):
        # Atualiza o valor em um índice específico
        self._data[index] = value

    def __iter__(self):
        # Retorna a própria instância como iterador (padrão Python)
        return self

    def __next__(self):
        # Define a lógica para iteração com 'for' ou 'next()'
        if self._next_index >= self._index:
            # Zera ele para realizar a Iteração mais um vez
            self._next_index = 0 
            raise StopIteration

        # Retorna o próximo valor e avança o índice
        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    list_the_data = MyList()

    list_the_data.funcion_append("Kayque", "Samuel")
    list_the_data.funcion_append("Daniel")

    # Atualiza diretamente um valor da estrutura
    list_the_data[2] = 'Daniel Costa'

    # Mostra o dicionário interno
    print(list_the_data._data)

    # Percorre os dados usando o protocolo de iteração
    for item in list_the_data:
        print(item)

    
