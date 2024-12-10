import pytest
import os
import json
import sys
sys.path.append('/Users/sharlene.cera/Library/CloudStorage/OneDrive-VodafoneGroup/Documents/Uni/Object Orientated Programming/Assignment 2/WarehouseManagementApp/app')

from Main import WarehouseApp
from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_save_inventory_to_json(stocked_warehouse_app, stocked_warehouse_json):
    file_name = "inventory.json"
    content = stocked_warehouse_json

    stocked_warehouse_app.inventory_manager.save_to_json(file_name)

    # check if file exists
    assert os.path.exists(file_name)

    # check the contents are in the expected form
    with open(file_name, 'r') as file:
        saved_content = json.load(file)

    assert saved_content == content

    # delete file
    os.remove(file_name)

def test_load_inventory_from_json(initial_warehouse_app, stocked_warehouse_app, stocked_warehouse_json):
    file_name = "inventory.json"
    content_to_load = stocked_warehouse_json

    # Create a test file using the expected content
    with open(file_name, 'w') as file:
        json.dump(content_to_load, file)
    
    # verify the starting inventory is different to the inventory to load
    assert initial_warehouse_app != stocked_warehouse_app

    # use the load function to load data from this file
    initial_warehouse_app.inventory_manager.load_from_json(file_name)

    # check initial inventory sections is same as expected sections
    assert initial_warehouse_app.inventory_manager.get_inventory() == stocked_warehouse_app.inventory_manager.get_inventory()
    
    # delete file
    os.remove(file_name)

    