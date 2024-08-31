class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register, adjusting the total and items list."""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):
        """Applies the discount to the total, if any."""
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            # Print formatted total with dollar sign but no cents
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Subtracts the last transaction from the total."""
        if self.last_transaction:
            title, price, quantity = self.last_transaction
            self.total -= price * quantity
            # Remove the items from the list
            for _ in range(quantity):
                self.items.remove(title)
            self.last_transaction = None

# Example usage
cash_register_with_discount = CashRegister(20)
cash_register_with_discount.add_item("apple", 1.00, 3)
cash_register_with_discount.apply_discount()
cash_register_with_discount.void_last_transaction()
print(cash_register_with_discount.total)
