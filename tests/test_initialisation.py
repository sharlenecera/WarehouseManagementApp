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

@pytest.fixture
def warehouse_app():
    inventory_manager = InventoryManager()
    # Adding initial sections
    inventory_manager.add_section(InventorySection("Electronics"))
    inventory_manager.add_section(InventorySection("Automotive"))
    app = WarehouseApp(inventory_manager)
    return app

def test_inventory_has_initial_sections(warehouse_app):
    assert list(warehouse_app.inventory_manager.sections.keys()) == ['Electronics', 'Automotive']

def test_initial_sections_are_empty(warehouse_app):
    for section in warehouse_app.inventory_manager.sections.values():
        assert section.items == {}