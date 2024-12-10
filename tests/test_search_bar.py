import pytest
import sys
sys.path.append('/Users/sharlene.cera/Library/CloudStorage/OneDrive-VodafoneGroup/Documents/Uni/Object Orientated Programming/Assignment 2/WarehouseManagementApp/app')


def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_search_one_section(stocked_warehouse_app):
    query = "Electronics"
    expected_results = ['Section: Electronics', 'Smartphone: 30', 'Laptop: 20', 'Tablet: 25', 'Headphones: 40']
    
    assert stocked_warehouse_app.inventory_manager.search_inventory(query) == expected_results

def test_search_partial_section(stocked_warehouse_app):
    query = "APP"
    expected_results = [
        'Section: Home Appliances', 'Refrigerator: 10', 'Microwave Oven: 15', 'Washing Machine: 8', 'Air Conditioner: 12',
        'Section: Clothing and Apparel', 'T-Shirts: 50', 'Jeans: 40', 'Jackets: 30', 'Sneakers: 25'
    ]
    
    assert stocked_warehouse_app.inventory_manager.search_inventory(query) == expected_results

def test_search_no_match(stocked_warehouse_app):
    query = "Space Vehicle"
    expected_results = []
    
    assert stocked_warehouse_app.inventory_manager.search_inventory(query) == expected_results