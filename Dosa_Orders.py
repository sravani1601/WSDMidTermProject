import json

def process_orders(filename):
    with open(filename, 'r') as file:
        orders = json.load(file)

    customers = {order["phone"]: order["name"] for order in orders}
    items = {}

    for order in orders:
        for item in order["items"]:
            name = item["name"]
            items[name] = items.get(name, {"price": item["price"], "orders": 0})
            items[name]["orders"] += 1

    json.dump(customers, open("customers.json", "w"), indent=4)
    json.dump(items, open("items.json", "w"), indent=4)

process_orders("example_orders.json")
