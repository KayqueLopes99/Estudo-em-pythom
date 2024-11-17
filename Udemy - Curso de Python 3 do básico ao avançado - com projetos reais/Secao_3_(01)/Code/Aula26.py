variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:+^10}') # preencher os espaços vazios com +.
print(f'{1000.765434567:,.1f}') # Separar por ,

print(f'{1000.765434567:.1f}')

print(f'{1000.765434567:0=+10,.1f}') # Forçar.
print(f'O hexadecimal de 1500 é {1500:08x}')

# Flags.
print(f'{variavel!r}')
