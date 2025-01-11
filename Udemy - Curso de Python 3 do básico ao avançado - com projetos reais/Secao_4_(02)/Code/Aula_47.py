from itertools import count

c1 = count(start=8, step=8)
r1 = range(1,11)

print('c1', hasattr(c1, '__iter__')) # iteravel
print('c1', hasattr(c1, '__next__')) # Iterator
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print("Count")
for index in c1: # index = next.
    if index > 100:
        break
    print(index, end=' ')

print()

print("Range")
for index in r1: # index = next.
    print(index, end=' ')
