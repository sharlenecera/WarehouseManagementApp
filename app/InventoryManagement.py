import json

from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem

class InventoryManager:
    def __init__(self):
        self.__sections = {} # dict

    @property
    def sections(self):
        return self.__sections
    
    @sections.setter
    def sections(self, sections):
        self.__sections = sections

    def add_section(self, section):
        self.sections[section.name] = section

    def get_section(self, name):
        return self.sections.get(name) # None if not found
    
    def add_item(self, section_name, item):
        section = self.get_section(section_name)
        if section:
            section.add_item(item)
        else:
            raise ValueError("Section not found")
        
    def get_items_in_section(self, section_name):
        section = self.get_section(section_name)
        if section:
            return [str(item) for item in section.items.values()]
        return []
    
    def add_stock(self, section_name, name, amount, misc_info="a"):
        section = self.get_section(section_name)
        if section:
            section.add_stock(name, amount, misc_info)
        else:
            raise ValueError("Section not found")
        
    def remove_stock(self, section_name, name, amount):
        section = self.get_section(section_name)
        if section:
            try:
                section.remove_stock(name, amount)
            except ValueError as e:
                raise ValueError("Not enough stock to remove selected amount.")
        else:
            raise ValueError("Section not found")
        
    def move_stock(self, from_section_name, to_section_name, item_name, amount):
        from_section = self.get_section(from_section_name)
        to_section = self.get_section(to_section_name)
        if from_section == to_section:
            raise ValueError("To and from destination must not be the same.")
        elif from_section and to_section:
            try:
                from_section.remove_stock(item_name, amount)
                to_section.add_stock(item_name, amount, "m")
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError("Invalid section has been entered.")
        
    def get_inventory(self):
        inventory = []
        for section in self.sections.values():
            inventory.append(str(section))
            inventory.extend(str(item) for item in section.items.values())
        return inventory
    
    def search_inventory(self, search):
        results = []
        for section in self.sections.values():
            if search.lower() in section.name.lower():
                results.append(str(section))
                results.extend(str(item) for item in section.items.values())
        return results
    
    def save_to_json(self, file_name):
        content = {}
        for section in self.sections.values():
            section_value = {}
            for item in section.items.values():
                section_value[item.name] = item.quantity
            content[section.name] = section_value
        with open(file_name, 'w') as file:
            json.dump(content, file)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as file:
            content = json.load(file)
        # overwriting the current dictionary
        self.sections = {}
        for section_name in content:
            section = InventorySection(section_name)
            for item_name in content[section_name]:
                section.add_item(RegularItem(item_name, content[section_name][item_name]))
            self.add_section(section)