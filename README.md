# Order Processing Script

## Description
This Python script processes a JSON file containing customer orders and generates two output files:
- `customers.json`: A dictionary mapping customer phone numbers to their names.
- `items.json`: A dictionary that tracks the number of times each item was ordered, along with its price.

## Design Overview
The script follows these steps:
1. Reads the input JSON file (`example_orders.json`) which contains a list of orders.
2. Extracts customer names and phone numbers, storing them in `customers.json`.
3. Extracts item names, their prices, and counts how many times each item was ordered, storing the result in `items.json`.

## File Structure
- process_orders.py - The main script.
- example_orders.json - Input file containing customer orders.
- customers.json - Output file mapping phone numbers to customer names.
- items.json- Output file tracking item prices and order counts.


### Running the Script
Run your code Dosa_Orders.py using visual studio
Then it creates two files items.josn and customers.json
Below are the sample input and output format:

**Input(example_orders.json):**
{
        "timestamp": 1702219784,
        "name": "Damodhar",
        "phone": "732-555-5509",
        "items": [
            {
                "name": "Cheese Madurai Masala Dosa",
                "price": 13.95
            },
            {
                "name": "Onion Chilli Masala Dosa",
                "price": 11.95
            }
        ],
        "notes": "extra spicy"
}

**Output:
items.json:**
{"Cheese Madurai Masala Dosa": {"price": 13.95, "orders": 1232}, "Onion Chilli Masala Dosa": {"price": 11.95, "orders": 1234}, "Cheese & Onion Chilli Masala Dosa": {"price": 12.95, "orders": 1200}, "Onion Rava Mysore Masala Dosa": {"price": 14.95, "orders": 1152}, "Butter Masala Dosa": {"price": 12.95, "orders": 3632}, "Madurai Masala Dosa": {"price": 12.95, "orders": 1239}, "Sada Dosa": {"price": 9.95, "orders": 1233}, "Gun Powder Dosa": {"price": 13.95, "orders": 2461}, "Onion Chilli Rava Masala Dosa": {"price": 14.95, "orders": 1236}, "Masala Dosa": {"price": 10.95, "orders": 4802}, "Butter Mysore Masala Dosa": {"price": 11.95, "orders": 1220}, "Malgudi Onion Rava Masala Dosa": {"price": 14.95, "orders": 1173}, "Cheese Mysore Masala Dosa": {"price": 13.95, "orders": 1219}, "Ghee Roast Masala Dosa": {"price": 11.95, "orders": 1197}, "Mysore Masala Dosa": {"price": 11.95, "orders": 1184}, "Onion Rava Masala Dosa": {"price": 13.95, "orders": 1136}, "Onion Rava Sada Dosa": {"price": 12.95, "orders": 1205}, "Cheese Masala Dosa": {"price": 11.95, "orders": 1172}, "Paper Masala Dosa": {"price": 11.95, "orders": 1169}}

**Customers.json**
{"732-555-5509": "Damodhar", "609-555-2301": "Tom", "609-555-5508": "Kunal", "609-555-0326": "Bhargavi", "732-555-1919": "Shanmukhi", "732-555-4109": "Matt", "732-555-0021": "Mohit", "609-555-4030": "Ryan", "609-555-1102": "Durga", "418-555-4321": "Dhanush", "609-555-9181": "Bhaskara", "732-555-5508": "Swetha", "732-555-8123": "Devarsh", "732-555-2181": "Thanmayi", "609-555-7522": "Mohammad", "609-555-3289": "Keith", "609-555-5509": "Nimay", "732-555-1112": "Pranit", "732-555-1813": "Dhruvik", "732-555-1812": "Parth", "418-555-0123": "Rajkumar", "609-555-1290": "Saurabh", "609-555-6090": "Sri", "732-555-9001": "Shivrishvith", "732-555-4198": "Pranav", "609-555-4031": "Venkat", "732-555-2222": "Nirmal", "609-555-2000": "Karthik", "609-555-9189": "Sarathi", "732-555-0124": "Jennifer"}



