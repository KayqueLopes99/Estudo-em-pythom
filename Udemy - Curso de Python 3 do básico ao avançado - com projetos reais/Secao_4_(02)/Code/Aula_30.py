# Introdução às Generator functions
# Temos um range generator
def funcion_generator(start=0, end=100):
    while True:
        yield start
        start += 1

        if start >= end:
            
            return 'End'
        
generator_variable = funcion_generator(end=150)
for traverse in generator_variable:
    print(traverse)
