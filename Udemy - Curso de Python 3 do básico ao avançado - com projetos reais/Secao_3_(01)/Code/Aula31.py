condicao = True # False.
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo.")
else:
    print("Não faça algo.")

if passou_no_if is None:
    print("Não passou no if.")

if passou_no_if is not None:
    print("Não passou p if.")
# Colocar uma bandeira em determinado local do código, usa-se o None para verificar se essa varíavel em ou não valor(Bandeira está ou não fincada).
# Is e is not checa o id do objeto na memória. 