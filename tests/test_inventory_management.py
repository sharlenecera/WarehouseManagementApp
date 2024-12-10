import pytest
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

def test_add_new_item(initial_warehouse_app):
    name = "Tablet"
    quantity = 100
    section_name = "Electronics"
    item = RegularItem(name, quantity)

    section = initial_warehouse_app.inventory_manager.sections[section_name]
    section.add_item(item)

    assert item in initial_warehouse_app.inventory_manager.sections["Electronics"].items.values()

# def test_delete_item(initial_warehouse_app):
#     pass

#     # implement this

def test_add_stock(stocked_warehouse_app):

    name = "Tablet"
    quantity_to_add = 25
    section_name = "Electronics"
    
    item = stocked_warehouse_app.inventory_manager.sections[section_name].get_item(name)
    starting_quantity = item.quantity

    item.add_stock(quantity_to_add)

    quantity_after = stocked_warehouse_app.inventory_manager.sections[section_name].get_item(name).quantity

    assert quantity_after - starting_quantity == quantity_to_add

def test_remove_stock(stocked_warehouse_app):

    name = "Tablet"
    quantity_to_remove = 15
    section_name = "Electronics"
    
    item = stocked_warehouse_app.inventory_manager.sections[section_name].get_item(name)
    starting_quantity = item.quantity

    item.remove_stock(quantity_to_remove)

    quantity_after = stocked_warehouse_app.inventory_manager.sections[section_name].get_item(name).quantity

    assert starting_quantity - quantity_after == quantity_to_remove

def test_new_items_details_added_correctly(initial_warehouse_app):
    name = "Tablet"
    quantity = 100
    section_name = "Electronics"
    item = RegularItem(name, quantity)

    section = initial_warehouse_app.inventory_manager.sections[section_name]
    section.add_item(item)

    assert name in initial_warehouse_app.inventory_manager.sections["Electronics"].items.keys()
    assert quantity == initial_warehouse_app.inventory_manager.sections["Electronics"].items[name].quantity

def test_move_item_to_different_section(stocked_warehouse_app):
    name = "Tablet"
    amount_to_move = 20
    from_section = "Electronics"
    to_section = "Toys and Games"

    # calculating before quantities in both sections
    from_starting_quantity = stocked_warehouse_app.inventory_manager.sections[from_section].get_item(name).quantity

    to_starting_quantity = 0
    if stocked_warehouse_app.inventory_manager.sections[to_section].get_item(name):
        to_starting_quantity = stocked_warehouse_app.inventory_manager.sections[to_section].get_item(name).quantity

    # moving stock
    stocked_warehouse_app.inventory_manager.move_stock(from_section, to_section, name, amount_to_move)

    # checking item is present in new location
    assert stocked_warehouse_app.inventory_manager.sections[to_section].get_item(name)

    # checking correct amount moved
    from_quantity_after = stocked_warehouse_app.inventory_manager.sections[from_section].get_item(name).quantity
    assert from_starting_quantity - from_quantity_after == amount_to_move

    to_quantity_after = stocked_warehouse_app.inventory_manager.sections[to_section].get_item(name).quantity
    assert to_quantity_after - to_starting_quantity == amount_to_move