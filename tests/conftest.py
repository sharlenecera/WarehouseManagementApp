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
    section.add_item(RegularItem("Rice Bags", 20))
    section.add_item(RegularItem("Canned Beans", 50))
    section.add_item(RegularItem("Pasta Packs", 40))
    section.add_item(RegularItem("Cooking Oil Bottles", 30))
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
            "Smartphone": 30,
            "Laptop": 20,
            "Tablet": 25,
            "Headphones": 40
        },
        "Automotive": {
            "Car Battery": 15,
            "Tire": 50,
            "Engine Oil": 30,
            "Brake Pads": 20
        },
        "Home Appliances": {
            "Refrigerator": 10,
            "Microwave Oven": 15,
            "Washing Machine": 8,
            "Air Conditioner": 12
        },
        "Furniture": {
            "Office Chair": 20,
            "Dining Table": 5,
            "Sofa Set": 7,
            "Bed Frame": 10
        },
        "Clothing and Apparel": {
            "T-Shirts": 50,
            "Jeans": 40,
            "Jackets": 30,
            "Sneakers": 25
        },
        "Sports Equipment": {
            "Basketballs": 30,
            "Tennis Rackets": 20,
            "Soccer Balls": 25,
            "Yoga Mats": 15
        },
        "Toys and Games": {
            "Action Figures": 40,
            "Board Games": 20,
            "Puzzles": 30,
            "Dolls": 25
        },
        "Books and Stationery": {
            "Notebooks": 50,
            "Pens": 100,
            "Novels": 30,
            "Textbooks": 20
        },
        "Health and Beauty": {
            "Shampoo Bottles": 40,
            "Toothpaste Tubes": 50,
            "Face Cream": 30,
            "Vitamins": 25
        },
        "Groceries and Food Items": {
            "Rice Bags": 20,
            "Canned Beans": 50,
            "Pasta Packs": 40,
            "Cooking Oil Bottles": 30
        },
        "Office Supplies": {
            "Printer Paper Reams": 50,
            "Staplers": 20,
            "File Folders": 40,
            "Desk Lamps": 15
        },
        "Tools and Hardware": {
            "Hammers": 25,
            "Screwdriver Sets": 30,
            "Wrenches": 20,
            "Drill Machines": 10
        }
    }