from BaseInventoryItem import InventoryItem

class RegularItem(InventoryItem):
    def add_stock(self, amount):
        self._quantity += amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock")
        self._quantity -= amount

class PerishableItem(RegularItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self._expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self._expiry_date

    def __str__(self):
        return f"{self.name} (Expires: {self.expiry_date}): {self.quantity}"