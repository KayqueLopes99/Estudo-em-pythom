from datetime import datetime



def createCheckingAccount(accountList, userList, cpf) -> dict[str] | None:
    AGENCY_NUMBER: str = "0001"
    user_found = None

    for user in userList:
        if user["cpf"] == cpf:
            user_found = user
            break

    if user_found is None:
        print("\033[91mError: CPF not found. Please register the client first.\033[m")
        return None

    numberAccount: int = len(accountList) + 1
    newUserAccount = {
        "name": user_found["name"],
        "cpf": user_found["cpf"],
        "AgencyNumber": AGENCY_NUMBER,
        "numberAccount": f"{numberAccount:04d}",
    }
    return newUserAccount


def deposit(statement: list[str], balance: float, amount: float, /) -> float:
    DEPOSIT_LIMIT: int = 10000
    timestamp: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    if amount <= 0:
        print("\033[91mError: Deposit amount must be greater than zero.\033[m")
        return balance

    current_balance: float = balance
    current_limit: int = DEPOSIT_LIMIT

    if current_balance + amount > current_limit:
        print(f"\033[91mError: Total balance cannot exceed the bank limit ({current_limit}).\033[m")
        return balance

    current_balance += amount
    balance = current_balance
    statement.append(f"Deposit of ${amount:.2f} - Made on {timestamp} - Available balance: ${balance:.2f}")

    print(f"\033[92mDeposit of ${amount:.2f} successful! New balance: ${balance:.2f}\033[m")
    return balance


def withdraw(*, statement: list[str], balance: float, amount: float, daily_withdrawals: int, overdraft_limit: float) -> tuple[float, int, float]:
    WITHDRAW_LIMIT: int = 1000
    timestamp: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    if amount > WITHDRAW_LIMIT:
        print(f"You cannot withdraw more than ${WITHDRAW_LIMIT} per transaction.")
        return balance, daily_withdrawals, overdraft_limit

    if amount <= 0:
        print("\033[91mError: Withdrawal amount must be greater than zero.\033[m")
        return balance, daily_withdrawals, overdraft_limit

    if daily_withdrawals == 0:
        print(f"\033[91mYou have reached your daily withdrawal limit.\033[m")
        return balance, daily_withdrawals, overdraft_limit

    available_balance: float = balance + overdraft_limit
    print(f"Current balance: ${balance:.2f} | Available overdraft: ${overdraft_limit:.2f}")

    if amount > available_balance:
        print(f"Error: Insufficient funds for withdrawal of ${amount:.2f}.")
        return balance, daily_withdrawals, overdraft_limit

    withdrawn_amount: float = amount

    if amount <= balance:
        balance -= amount
    else:
        difference: float = amount - balance
        balance = 0
        overdraft_limit -= difference

    statement.append(f"Withdrawal of ${withdrawn_amount:.2f} - Made on {timestamp} - Available balance: ${balance:.2f}")
    daily_withdrawals -= 1

    print(f"\033[92mWithdrawal of ${withdrawn_amount:.2f} successful! New balance: ${balance:.2f} | New overdraft: ${overdraft_limit:.2f}\033[m")

    return balance, daily_withdrawals, overdraft_limit



def print_statement(balance: float, /, *, statement: list) -> None:
    print("\n" + "="*42)
    print("\033[38;5;136m============ Account Statement ============\033[m")
    
    if not statement:
        print("No transactions have been made.")
    else:
        for entry in statement:
            print(f"\033[38;5;136m- {entry}\033[m")
            
    print(f"\n\033[92mFinal Balance: ${balance:.2f}\033[m")
    print("="*42)

def listDataAccounts(cpf: str, accountList, balance, statement) -> None:
    account_found = False
    for account in accountList:
        if account['cpf'] == cpf:
            print("\n" + "=" * 40)
            print("\033[38;5;136m======= Account Data =======\033[m")
            print(f"\033[1;38;5;46mAccount Holder: {account['name']}\033[m")
            print(f"\033[1;38;5;46mCPF: {account['cpf']}\033[m")
            print(f"\033[1;38;5;46mAgency: {account['AgencyNumber']}\033[m")
            print(f"\033[1;38;5;46mAccount Number: {account['numberAccount']}\033[m")
            print("=" * 40)
            account_found = True
            
            print(f"\033[92mBalance: ${balance:.2f}\033[m")
            print_statement(balance, statement=statement)

    if not account_found:
        print("\033[91mError: Account not found.\033[m")