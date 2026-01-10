"""
Lab 2 Task 1: Type Annotations
Add type hints to make mypy --strict pass with zero errors.
"""

# TODO: Add type hints to this class and all methods
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]
    
    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def apply_discount(self, percentage):
        total = self.get_total()
        return total * (1 - percentage / 100)


# TODO: Add type hints to these functions
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def process_data(data, transformer, filter_func):
    return [transformer(x) for x in data if filter_func(x)]
