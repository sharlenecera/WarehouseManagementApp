import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem

# GUI Implementation with Tkinter
class WarehouseApp(tk.Tk):
    def __init__(self, inventory_manager):
        super().__init__()
        self.inventory_manager = inventory_manager
        self.title("Warehouse Management System")

        self.create_widgets()
        self.update_inventory()

    def create_widgets(self):
        # Section selection

        tk.Label(self, text="Select Section").pack()
        self.section_var = tk.StringVar(self)
        self.section_menu = tk.OptionMenu(self, self.section_var, *self.inventory_manager.sections.keys())
        self.section_menu.pack()

        # Item adding fields
        tk.Label(self, text="Item Name").pack()
        self.add_item_name = tk.Entry(self)
        self.add_item_name.pack()

        tk.Label(self, text="Item Quantity").pack()
        self.add_item_quantity = tk.Entry(self)
        self.add_item_quantity.pack()


        tk.Label(self, text="Expiry Date (Optional, DD/MM/YYYY) ").pack()
        self.add_item_expiry = tk.Entry(self)
        self.add_item_expiry.pack()

        self.add_item_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_item_button.pack()

        # UI for Managing stock
        tk.Label(self, text="Stock Amount").pack()
        self.stock_amount = tk.Entry(self)
        self.stock_amount.pack()
        self.add_stock_button = tk.Button(self, text="Add Stock", command=self.add_stock)
        self.add_stock_button.pack()
        self.remove_stock_button = tk.Button(self, text="Remove Stock",
        command=self.remove_stock)
        self.remove_stock_button.pack()

        # UI for Moving Stock
        tk.Label(self, text="Destination Section").pack()
        self.move_to_var = tk.StringVar(self)
        self.move_to_section = tk.OptionMenu(self, self.move_to_var,
        *self.inventory_manager.sections.keys())
        self.move_to_section.pack()
        
        tk.Label(self, text="What do you want to move?").pack()
        self.move_item_name = tk.Entry(self)
        self.move_item_name.pack()
        
        tk.Label(self, text="QTY to move").pack()
        self.move_amount = tk.Entry(self)
        self.move_amount.pack()
        self.move_stock_button = tk.Button(self, text="Move Stock",
        command=self.move_stock)
        self.move_stock_button.pack()

        # UI for Inventory Display
        self.inventory_text = tk.Text(self, height=15, width=50)
        self.inventory_text.pack()

        # UI for saving and loading inventory to and from JSON files
        self.save_to_json_button = tk.Button(self, text="Save as JSON", command=self.save_to_json)
        self.save_to_json_button.pack()

        self.load_from_json_button = tk.Button(self, text="Load from JSON", command=self.load_from_json)
        self.load_from_json_button.pack()

    def add_item(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        quantity = int(self.add_item_quantity.get())
        if section_name and name and quantity >= 0:
            if self.add_item_expiry.get():
                print("You tried to add a perishable item")
                item = PerishableItem(name, quantity, self.add_item_expiry.get())
            else:
                print("You tried to add a regular item")
                item = RegularItem(name, quantity)
            self.inventory_manager.add_item(section_name, item)
            self.update_inventory()
        else:
            messagebox.showerror("Error", "Invalid item details")

    def add_stock(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        amount = int(self.stock_amount.get())
        try:
            self.inventory_manager.add_stock(section_name, name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_stock(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        amount = int(self.stock_amount.get())
        try:
            self.inventory_manager.remove_stock(section_name, name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def move_stock(self):
        from_section_name = self.section_var.get()
        to_section_name = self.move_to_var.get()
        item_name = self.move_item_name.get()
        amount = int(self.move_amount.get())
        try:
            self.inventory_manager.move_stock(from_section_name, to_section_name, item_name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_inventory(self):
        self.inventory_text.delete(1.0, tk.END)
        inventory = self.inventory_manager.get_inventory()
        for item in inventory:
            self.inventory_text.insert(tk.END, item + "\n")

    def save_to_json(self):
        file_name = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_name:
            self.inventory_manager.save_to_json(file_name)

    def load_from_json(self):
        file_name = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_name:
            self.inventory_manager.load_from_json(file_name)
            self.update_inventory()
# Initialise and run the application
if __name__ == "__main__":
    
    inventory_manager = InventoryManager()
    # Adding initial sections
    inventory_manager.add_section(InventorySection("Electronics"))
    inventory_manager.add_section(InventorySection("Automotive"))
    app = WarehouseApp(inventory_manager)
    app.mainloop()