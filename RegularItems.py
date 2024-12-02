from BaseInventoryItem import InventoryItem

class RegularItem(InventoryItem):
    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= amount

class PerishableItem(RegularItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name} (Expires: {self.expiry_date}): {self.quantity}"