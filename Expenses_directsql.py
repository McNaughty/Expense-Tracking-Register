class Expense:

    def __init__(self, name, category, amount, expenseuser) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.expenseuser = expenseuser

    # represent outputs as a string
    def __repr__(self):
        return f"Expense Entry: {self.name}, {self.category}, KSH: {self.amount} "