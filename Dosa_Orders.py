import json

def dosa_orders(filename):
    with open(filename, 'r') as file:
        orders = json.load(file)

    customers = {}
    items = {}

    with open("customers.json", "w") as file:
        json.dump(customers, file, indent=4)

    with open("items.json", "w") as file:
        json.dump(items, file, indent=4)

dosa_orders("example_orders.json")
