import re
import datetime



def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")

def validateCpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", '')
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("\033[91mThe CPF must have exactly 11 digits and contain only numbers.\033[m")
        return False
    
    if cpf == (cpf[0] * 11):
        print("\033[91mInvalid format! CPF cannot contain all identical digits.\033[m")
        return False

    cpfFirst9DigitsList = []
    countdown1 = 10
    for digit in cpf[:9]:
        cpfFirst9DigitsList.append(int(digit) * countdown1)
        countdown1 -= 1
    
    sumValues1 = sum(cpfFirst9DigitsList)
    firstDigitResult = (sumValues1 * 10) % 11
    firstDigitResult = firstDigitResult if firstDigitResult <= 9 else 0

    cpfFirst10DigitsList = []
    countdown2 = 11
    for digit in cpf[:10]:  
        cpfFirst10DigitsList.append(int(digit) * countdown2)
        countdown2 -= 1
    
    sumValues2 = sum(cpfFirst10DigitsList)
    secondDigitResult = (sumValues2 * 10) % 11
    secondDigitResult = secondDigitResult if secondDigitResult <= 9 else 0

    if firstDigitResult == int(cpf[9]) and secondDigitResult == int(cpf[10]):
        standardizedCpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        print(f"\033[92mSuccess! CPF: {standardizedCpf} is valid.\033[m")
        return standardizedCpf
    else:
        print("\033[91mError! Invalid CPF.\033[m")
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
        result = validateCpf(cpf) 
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