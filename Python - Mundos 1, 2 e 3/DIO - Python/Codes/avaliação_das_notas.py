"""
**Exercício: Sistema de Avaliação de Notas** 
"""
print("\033[38;5;136m------- Simulação dos resultados -------\033[m")
try:
   grade_one = float(input("Informe a Nota da Primeira Unidade: "))
   grade_two = float(input("Informe a Nota da Primeira Unidade: "))
   grade_three = float(input("Informe a Nota da Primeira Unidade: "))

   average = (grade_one + grade_two + grade_three)/3

   if (average >= 7) or (average >= 70):
      print(f"\033[92mMédia: {average} --- Situação: Aprovado!\033[m")

   elif (average >= 5 and average <= 6.9) or (average >= 50 and average <= 69):
      print(f"\033[93mMédia: {average} --- Situação: Recuperação!\033[m")

   else:
      print(f"\033[91mMédia: {average} --- Situação: Reprovado!\033[m")      

except ValueError:
      print("\033[91mErro: Entrada inválida! Certifique-se de digitar números.\033[m")






