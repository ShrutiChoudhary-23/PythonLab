def merge_inventory(*stores):
    inventory = {}

    for store in stores:
        for item, quantity in store.items():
            inventory[item] = inventory.get(item, 0) + quantity

    return inventory

def display_inventory(inventory):
    print("\nInventory Details:")
    for item, quantity in inventory.items():
        print(item, ":", quantity)

def check_item(inventory):
    item = input("\nEnter item name to check: ")

    if item in inventory:
        print("Available Quantity:", inventory.get(item, 0))
    else:
        print("Item not found.")

store1 = {"Pen": 20, "Book": 15, "Pencil": 30}
store2 = {"Pen": 10, "Book": 25, "Eraser": 12}
store3 = {"Pencil": 15, "Eraser": 8}

inventory = merge_inventory(store1, store2, store3)

display_inventory(inventory)

updated_inventory = {
    item: quantity for item, quantity in inventory.items()
}

extra_stock = {"Pen": 5, "Marker": 10}

for item, quantity in extra_stock.items():
    updated_inventory[item] = updated_inventory.get(item, 0) + quantity

print("\nUpdated Inventory:")
display_inventory(updated_inventory)

check_item(updated_inventory)
