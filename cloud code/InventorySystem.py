# Student A
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_cost(self):
        return self.price * self.quantity

# Student B
class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]
    
    def total_inventory_value(self):
        return sum(item.total_cost() for item in self.items)

# Student C
def test_inventory_system():
    inventory = Inventory()
    
    item1 = Item("Laptop ASUS", 40000, 2)
    item2 = Item("Mouse Zeus", 500, 3)
    item3 = Item("Keyboard Inplay", 900, 4)
    
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    
    print(f"Total inventory value: ${inventory.total_inventory_value()}")
    
    inventory.remove_item("Mouse")
    print(f"Total inventory value after removing Mouse: ${inventory.total_inventory_value()}")

# Student D
test_inventory_system()
