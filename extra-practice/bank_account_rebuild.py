class BankAccount:
    def __init__(self, owner_name: str, balance: float = 0):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Not enough balance for withdraw.")
        self.balance -= amount
    
    def check_balance(self) -> None:
        print(f"Balance: {self.balance}")