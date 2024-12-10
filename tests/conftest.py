import pytest
import sys
sys.path.append('/Users/sharlene.cera/Library/CloudStorage/OneDrive-VodafoneGroup/Documents/Uni/Object Orientated Programming/Assignment 2/WarehouseManagementApp/app')

from Main import WarehouseApp
from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem

@pytest.fixture
def valid_login_details():
    return {
        "username": "test",
        "password": "test"
    }

@pytest.fixture
def invalid_login_details():
    return {
        "username": "admin",
        "password": "admin"
    }

@pytest.fixture
def initial_warehouse_app():
    inventory_manager = InventoryManager()
    # Adding initial sections
    inventory_manager.add_section(InventorySection("Electronics"))
    inventory_manager.add_section(InventorySection("Automotive"))
    app = WarehouseApp(inventory_manager)
    return app

@pytest.fixture
def stocked_warehouse_app():
    inventory_manager = InventoryManager()
    
    section = InventorySection("Electronics")
    section.add_item(RegularItem("Smartphone", 30))
    section.add_item(RegularItem("Laptop", 20))
    section.add_item(RegularItem("Tablet", 25))
    section.add_item(RegularItem("Headphones", 40))
    inventory_manager.add_section(section)

    section = InventorySection("Automotive")
    section.add_item(RegularItem("Car Battery", 15))
    section.add_item(RegularItem("Tire", 50))
    section.add_item(RegularItem("Engine Oil", 30))
    section.add_item(RegularItem("Brake Pads", 20))
    inventory_manager.add_section(section)

    section = InventorySection("Home Appliances")
    section.add_item(RegularItem("Refrigerator", 10))
    section.add_item(RegularItem("Microwave Oven", 15))
    section.add_item(RegularItem("Washing Machine", 8))
    section.add_item(RegularItem("Air Conditioner", 12))
    inventory_manager.add_section(section)

    section = InventorySection("Furniture")
    section.add_item(RegularItem("Office Chair", 20))
    section.add_item(RegularItem("Dining Table", 5))
    section.add_item(RegularItem("Sofa Set", 7))
    section.add_item(RegularItem("Bed Frame", 10))
    inventory_manager.add_section(section)

    section = InventorySection("Clothing and Apparel")
    section.add_item(RegularItem("T-Shirts", 50))
    section.add_item(RegularItem("Jeans", 40))
    section.add_item(RegularItem("Jackets", 30))
    section.add_item(RegularItem("Sneakers", 25))
    inventory_manager.add_section(section)

    section = InventorySection("Sports Equipment")
    section.add_item(RegularItem("Basketballs", 30))
    section.add_item(RegularItem("Tennis Rackets", 20))
    section.add_item(RegularItem("Soccer Balls", 25))
    section.add_item(RegularItem("Yoga Mats", 15))
    inventory_manager.add_section(section)

    section = InventorySection("Toys and Games")
    section.add_item(RegularItem("Action Figures", 40))
    section.add_item(RegularItem("Board Games", 20))
    section.add_item(RegularItem("Puzzles", 30))
    section.add_item(RegularItem("Dolls", 25))
    inventory_manager.add_section(section)

    section = InventorySection("Books and Stationery")
    section.add_item(RegularItem("Notebooks", 50))
    section.add_item(RegularItem("Pens", 100))
    section.add_item(RegularItem("Novels", 30))
    section.add_item(RegularItem("Textbooks", 20))
    inventory_manager.add_section(section)

    section = InventorySection("Health and Beauty")
    section.add_item(RegularItem("Shampoo Bottles", 40))
    section.add_item(RegularItem("Toothpaste Tubes", 50))
    section.add_item(RegularItem("Face Cream", 30))
    section.add_item(RegularItem("Vitamins", 25))
    inventory_manager.add_section(section)

    section = InventorySection("Groceries and Food Items")
    section.add_item(PerishableItem("Rice Bags", 20, "25/12/2024"))
    section.add_item(PerishableItem("Canned Beans", 50, "20/12/2024"))
    section.add_item(PerishableItem("Pasta Packs", 40, "19/12/2024"))
    section.add_item(PerishableItem("Cooking Oil Bottles", 30, "29/12/2024"))
    inventory_manager.add_section(section)
    
    section = InventorySection("Office Supplies")
    section.add_item(RegularItem("Printer Paper Reams", 50))
    section.add_item(RegularItem("Staplers", 20))
    section.add_item(RegularItem("File Folders", 40))
    section.add_item(RegularItem("Desk Lamps", 15))
    inventory_manager.add_section(section)

    section = InventorySection("Tools and Hardware")
    section.add_item(RegularItem("Hammers", 25))
    section.add_item(RegularItem("Screwdriver Sets", 30))
    section.add_item(RegularItem("Wrenches", 20))
    section.add_item(RegularItem("Drill Machines", 10))
    inventory_manager.add_section(section)

    app = WarehouseApp(inventory_manager)
    return app

@pytest.fixture
def stocked_warehouse_json():
    return {
        "Electronics": {
            "Smartphone": { "name": "Smartphone", "quantity": 30 },
            "Laptop": { "name": "Laptop", "quantity": 20 },
            "Tablet": { "name": "Tablet", "quantity": 25 },
            "Headphones": { "name": "Headphones", "quantity": 40 }
        },
        "Automotive": {
            "Car Battery": { "name": "Car Battery", "quantity": 15 },
            "Tire": { "name": "Tire", "quantity": 50 },
            "Engine Oil": { "name": "Engine Oil", "quantity": 30 },
            "Brake Pads": { "name": "Brake Pads", "quantity": 20 }
        },
        "Home Appliances": {
            "Refrigerator": { "name": "Refrigerator", "quantity": 10 },
            "Microwave Oven": { "name": "Microwave Oven", "quantity": 15 },
            "Washing Machine": { "name": "Washing Machine", "quantity": 8 },
            "Air Conditioner": { "name": "Air Conditioner", "quantity": 12 }
        },
        "Furniture": {
            "Office Chair": { "name": "Office Chair", "quantity": 20 },
            "Dining Table": { "name": "Dining Table", "quantity": 5 },
            "Sofa Set": { "name": "Sofa Set", "quantity": 7 },
            "Bed Frame": { "name": "Bed Frame", "quantity": 10 }
        },
        "Clothing and Apparel": {
            "T-Shirts": { "name": "T-Shirts", "quantity": 50 },
            "Jeans": { "name": "Jeans", "quantity": 40 },
            "Jackets": { "name": "Jackets", "quantity": 30 },
            "Sneakers": { "name": "Sneakers", "quantity": 25 }
        },
        "Sports Equipment": {
            "Basketballs": { "name": "Basketballs", "quantity": 30 },
            "Tennis Rackets": { "name": "Tennis Rackets", "quantity": 20 },
            "Soccer Balls": { "name": "Soccer Balls", "quantity": 25 },
            "Yoga Mats": { "name": "Yoga Mats", "quantity": 15 }
        },
        "Toys and Games": {
            "Action Figures": { "name": "Action Figures", "quantity": 40 },
            "Board Games": { "name": "Board Games", "quantity": 20 },
            "Puzzles": { "name": "Puzzles", "quantity": 30 },
            "Dolls": { "name": "Dolls", "quantity": 25 }
        },
        "Books and Stationery": {
            "Notebooks": { "name": "Notebooks", "quantity": 50 },
            "Pens": { "name": "Pens", "quantity": 100 },
            "Novels": { "name": "Novels", "quantity": 30 },
            "Textbooks": { "name": "Textbooks", "quantity": 20 }
        },
        "Health and Beauty": {
            "Shampoo Bottles": { "name": "Shampoo Bottles", "quantity": 40 },
            "Toothpaste Tubes": { "name": "Toothpaste Tubes", "quantity": 50 },
            "Face Cream": { "name": "Face Cream", "quantity": 30 },
            "Vitamins": { "name": "Vitamins", "quantity": 25 }
        },
        "Groceries and Food Items": {
            "Rice Bags": { "name": "Rice Bags", "quantity": 20, "expiry date": "25/12/2024" },
            "Canned Beans": { "name": "Canned Beans", "quantity": 50, "expiry date": "20/12/2024" },
            "Pasta Packs": { "name": "Pasta Packs", "quantity": 40, "expiry date": "19/12/2024" },
            "Cooking Oil Bottles": { "name": "Cooking Oil Bottles", "quantity": 30, "expiry date": "29/12/2024" }
        },
        "Office Supplies": {
            "Printer Paper Reams": { "name": "Printer Paper Reams", "quantity": 50 },
            "Staplers": { "name": "Staplers", "quantity": 20 },
            "File Folders": { "name": "File Folders", "quantity": 40 },
            "Desk Lamps": { "name": "Desk Lamps", "quantity": 15 }
        },
        "Tools and Hardware": {
            "Hammers": { "name": "Hammers", "quantity": 25 },
            "Screwdriver Sets": { "name": "Screwdriver Sets", "quantity": 30 },
            "Wrenches": { "name": "Wrenches", "quantity": 20 },
            "Drill Machines": { "name": "Drill Machines", "quantity": 10 }
        }
    }