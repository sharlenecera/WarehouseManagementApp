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

def test_successful_login_validation(initial_warehouse_app, valid_login_details):
    is_successful = initial_warehouse_app.login_window.validate_login_details(valid_login_details)
    assert is_successful == True

def test_unsuccessful_login_validation(initial_warehouse_app, invalid_login_details):
    is_successful = initial_warehouse_app.login_window.validate_login_details(invalid_login_details)
    assert is_successful == False

