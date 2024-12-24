def create_operation(multiplicador):
   def operation_number(numero):
      return f"Resultado: {numero * multiplicador}"
   return operation_number # Só o local de memória


while True:
   multiplicador = int(input("Informe o Algarismo que será o multiplicador: "))
   result_doble = create_operation(multiplicador) # <- guardou o multiplicador. 

   number = int(input("Informe o Número: "))
   print(result_doble(number))
   op = int(input("\033[92m1 - sair || 0 - Cotinuar: \033[m"))
   if op == 1:
      print("Saindo...")
      break



# Com funções padrão - Usamos isto.