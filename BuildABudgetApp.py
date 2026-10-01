class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
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
        output = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    # Calculate total withdrawals
    spent = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]

        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages, rounded down to nearest 10
    percentages = []

    for amount in spent:
        percentage = int((amount / total_spent) * 100)
        percentage = percentage // 10 * 10
        percentages.append(percentage)

    output = "Percentage spent by category\n"

    # Create bars from 100 to 0
    for level in range(100, -1, -10):
        output += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                output += " o "
            else:
                output += "   "

        output += " \n"

    # Horizontal line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find longest category name
    max_length = max(len(category.name) for category in categories)

    # Category names vertically
    for i in range(max_length):
        output += "     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "

        if i < max_length - 1:
            output += "\n"

    return output