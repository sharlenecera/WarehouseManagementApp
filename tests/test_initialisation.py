import pytest
import sys
sys.path.append('/Users/sharlene.cera/Library/CloudStorage/OneDrive-VodafoneGroup/Documents/Uni/Object Orientated Programming/Assignment 2/WarehouseManagementApp/app')

from Main import WarehouseApp
from InventoryManagement import InventoryManager
from Sections import InventorySection

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_inventory_has_initial_sections(initial_warehouse_app):
    assert list(warehouse_app.inventory_manager.sections.keys()) == ['Electronics', 'Automotive']

def test_initial_sections_are_empty(initial_warehouse_app):
    for section in warehouse_app.inventory_manager.sections.values():
        assert section.items == {}