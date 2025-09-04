import re
import datetime



def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")

def valida_cpf(cpf):
    # Remover formatações e garantir apenas números
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", '')
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("\033[91mO CPF deve ter exatamente 11 dígitos e conter apenas números.\033[m")
        return False
    
    # Verifica se todos os números são iguais (ex: 00000000000 ou 11111111111)
    if cpf == (cpf[0] * 11):
        print("\033[91mFormato inválido! CPF não pode ter todos os números iguais.\033[m")
        return False

    # Cálculo do primeiro dígito verificador
    lista_com_9_digitos_cpf = []
    contador_regressivo_1 = 10
    for digito in cpf[:9]:
        lista_com_9_digitos_cpf.append(int(digito) * contador_regressivo_1)
        contador_regressivo_1 -= 1
    
    soma_valores_1 = sum(lista_com_9_digitos_cpf)
    resultado_primeiro_digito = (soma_valores_1 * 10) % 11
    resultado_primeiro_digito = resultado_primeiro_digito if resultado_primeiro_digito <= 9 else 0

    # Cálculo do segundo dígito verificador
    lista_com_10_digitos_cpf = []
    contador_regressivo_2 = 11
    for digito in cpf[:10]:  # Inclui o primeiro dígito verificador
        lista_com_10_digitos_cpf.append(int(digito) * contador_regressivo_2)
        contador_regressivo_2 -= 1
    
    soma_valores_2 = sum(lista_com_10_digitos_cpf)
    resultado_segundo_digito = (soma_valores_2 * 10) % 11
    resultado_segundo_digito = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0

    # Verificação final
    if resultado_primeiro_digito == int(cpf[9]) and resultado_segundo_digito == int(cpf[10]):
        cpf_padronizado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        print(f"\033[92mSucesso! CPF: {cpf_padronizado} é válido.\033[m")
        return cpf_padronizado
    else:
        print("\033[91mErro! CPF inválido.\033[m")
        return False


class Tratatives:
    def validate_name(self, name: str) -> str | None:
        if not name.replace(" ", "").isalpha():
            error_message("Invalid user name! Please enter a valid name.")
            return None
        return name.title()
    
    def validateString(self, name: str, text: str) -> str | None:
        if not name.replace(" ", "").isalpha():
            error_message(text)
            return None
        return name.title()

    def validate_date_of_birth(self, day: int, month: int, year: int) -> bool:
        try:
            date = datetime.date(year, month, day)
            if not (1900 <= year <= 2025):
                error_message("Invalid year!")
                return False
            return True
        except ValueError:
            error_message("Invalid date! Check day or month.")
            return False

    def validate_email(self, email: str) -> str | None:
       email_pattern = r'^[a-zA-Z0-9_.+-]+@(gmail\.com|hotmail\.com|outlook\.com|yahoo\.com)$'
       if re.match(email_pattern, email):
         success_message("Email is valid!")
         return email
       else:
        error_message("Email is not valid.")
        return None


    def validate_cpf(self, cpf: str) -> bool:
        result = valida_cpf(cpf) 
        return result

    def validate_integer_option(self, variable) -> int | None:
        """Validate integer option in range 1-7"""
        if isinstance(variable, int) or (isinstance(variable, str) and variable.isdigit()):
            var_int = int(variable)
            if 1 <= var_int <= 7:
                return var_int
            else:
                error_message("Selected option is not in the range [1-7].")
        else:
            error_message("The selected option must be an integer.")
        return None

    def validate_integer(self, variable) -> int | None:
        """Validate a general integer"""
        if isinstance(variable, int):
            return variable
        elif isinstance(variable, str) and variable.isdigit():
            return int(variable)
        else:
            error_message("Please enter a valid integer number.")
            return None

    def validate_float(self, variable) -> float | None:
        """Validate a general float"""
        try:
            return float(variable)
        except ValueError:
            error_message("Please enter a valid number (float).")
            return None