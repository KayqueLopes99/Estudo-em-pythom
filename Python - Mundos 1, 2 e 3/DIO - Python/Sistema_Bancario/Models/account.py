from datetime import datetime

def checkingAccount(accountList, userList, cpf) -> dict[str] | None:
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


from datetime import datetime

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

    print(f"\032[92mDeposit of ${amount:.2f} successful! New balance: ${balance:.2f}\033[m")
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


def print_statement(history) -> None:
    index: int = 1
    print("-"*42)
    print("\033[38;5;136m============ Account Statement ============\033[m")
    for entry in history:
        print(f"\033[38;5;136m{index}*: {entry}\033[m")
        index += 1
    print("-"*42)
    

def listAccounts(accountList) -> None:
    print("\n" + "=" * 40)
    print("\033[38;5;21m--- = = = > Account List < = = = ---\033[m")
    print("=" * 40)
    if not accountList:
        print("\033[93mNo accounts registered.\033[m")
        return

    for account in accountList:
        print(f"\033[1;38;5;46mAccount Holder: {account['name']}\033[m")
        print(f"\033[1;38;5;46mCPF: {account['cpf']}\033[m")
        print(f"\033[1;38;5;46mAgency: {account['AgencyNumber']}\033[m")
        print(f"\033[1;38;5;46mAccount Number: {account['numberAccount']}\033[m")
        print("-" * 40)

def listDataAccount(cpf: str, accountList) -> None:
    account_found = False
    for account in accountList:
        if account['cpf'] == cpf:
            print("\n" + "=" * 40)
            print("\033[38;5;136m======= Account Data =======\033[m")
            print(f"\033[1;38;5;46mAccount Holder: {account['name']}\033[m")
            print(f"\033[1;38;5;46mCPF: {account['cpf']}\033[m")
            print(f"\033[1;38;5;46mAgency: {account['AgencyNumber']}\033[m")
            print(f"\033[1;38;5;46mAccount Number: {account['numberAccount']}\033[m")
            print("=" * 40 + "\n")
            account_found = True

    if not account_found:
        print("\033[91mError: Account not found.\033[m")
        
if __name__ == "__main__":
    accounts = [
        {"name": "John Doe", "cpf": "10931769469", "AgencyNumber": "0001", "numberAccount": "0001"},
        {"name": "Jane Smith", "cpf": "98765432100", "AgencyNumber": "0001", "numberAccount": "0002"},
        {"name": "Alice Johnson", "cpf": "10931769469", "AgencyNumber": "0001", "numberAccount": "0003"},
    ]

    # newAccount = checkingAccount(accounts, users, "10931769469")

    # if newAccount:
    #     accounts.append(newAccount)
    listDataAccount("10931769469", accounts)
    listAccounts(accounts)