# Abstraction: Define abstract class for a generic inventory item
class InventoryItem:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    # if we add ability to change the name
    # @name.setter
    # def name(self, new_name):
    #     self._name = new_name

    @property
    def quantity(self):
        return self._quantity
    
    def add_stock(self, amount):
        raise NotImplementedError
    
    def remove_stock(self, amount):
        raise NotImplementedError
    
    def __str__(self):
        return f"{self._name}: {self._quantity}"