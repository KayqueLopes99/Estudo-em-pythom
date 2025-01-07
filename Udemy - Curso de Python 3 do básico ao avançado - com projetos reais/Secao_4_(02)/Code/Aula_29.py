import sys 

iterable = ['Eu', 'Tenho', '__iter__']
iterable = iter(iterable) # # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista)) # Tamanho em bytes.
print(sys.getsizeof(generator)) # Tamanho em bytes.

print(generator)

#for n in generator:
#    print(n)