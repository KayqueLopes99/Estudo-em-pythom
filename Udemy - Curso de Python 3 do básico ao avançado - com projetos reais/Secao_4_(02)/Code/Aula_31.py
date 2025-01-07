def generator_01():
    print("Start 01")
    yield 1
    yield 2
    yield 3
    print("End 01")


def generator_03():
     print("Start 03")
     yield 7
     yield 8
     yield 9
     print("End 03")
    


def generator_02(gen=None): # Parametro padrão
    print("Start 02")
    if gen is not None:
        yield from gen

    yield 4
    yield 5
    yield 6
    print("End 02")

g1 = generator_02(generator_01())
g2 = generator_02(generator_03())
g3 = generator_02()

for sequence_number in g1:
    print(sequence_number)

for sequence_number in g2:
    print(sequence_number)

for sequence_number in g3:
    print(sequence_number)