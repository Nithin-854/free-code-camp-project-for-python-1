class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spent = [sum(-item["amount"] for item in cat.ledger if item["amount"] < 0) for cat in categories]
    total_spent = sum(spent)
    spent_percentage = [int((s / total_spent) * 10) * 10 for s in spent] if total_spent > 0 else [0] * len(categories)


    chart = "Percentage spent by category\n"


    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| " + "  ".join("o" if p >= i else " " for p in spent_percentage) + "  \n"


    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]

    for row in zip(*names):
        chart += "     " + "  ".join(row) + "  \n"

    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(200, "car repair")

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
