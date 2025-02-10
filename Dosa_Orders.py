import json

def process_orders(filename):
    with open(filename, 'r') as file:
        orders = json.load(file)

    customers = {}
    items = {}

    for order in orders:
        customers[order["phone"]] = order["name"]
        for item in order["items"]:
            if item["name"] not in items:
                items[item["name"]] = {"price": item["price"], "orders": 0}
            items[item["name"]]["orders"] += 1

    with open("customers.json", "w") as file:
        json.dump(customers, file, indent=4)

    with open("items.json", "w") as file:
        json.dump(items, file, indent=4)

# Example usage
process_orders("example_orders.json")
