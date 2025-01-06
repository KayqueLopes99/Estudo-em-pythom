# Isinstance: Para saber se o objeto é de determinado tipo
list = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name': 'Kayque'},]
# Temos uma Lista com vários tipos e queremos achar o elemneto com um tipo específico para adicionar algo. Isso demonstra a necessidade de usar
# o .Isinstance()

for item in list:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        print('Str:', item.upper())
    
    elif isinstance(item, (int, float)):
        print('Num:', item, item * 2)
    
    else:
        print("Outher")
        print(item)