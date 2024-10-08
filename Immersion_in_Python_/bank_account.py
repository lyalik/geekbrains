class InsufficientFundsError(Exception):
    """Исключение для недостатка средств на счете."""
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self._balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств на счете.")
        self._balance -= amount

    def get_balance(self):
        return self._balance