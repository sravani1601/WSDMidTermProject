from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel,conlist
import json
from typing import List

class Item(BaseModel):
    item_id:int
    name:str
    price:float

class Customer(BaseModel):
    cust_id:int
    name:str
    phone:str

class Order(BaseModel):
    order_id:int=0
    timestamp:int=0
    cust_id:int
    notes:str
    item_list:conlist(int,min_length=1)



app = FastAPI()

@app.get("/order/{order_id}")

def get_order(order_id: int):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    initializeDB()

    # Fetch the order
    cursor.execute("SELECT id, timestamp, cust_id, notes FROM orders WHERE id = ?;", (order_id,))
    row = cursor.fetchone()

    if not row:
        print('Requested OrderId not found in DB')
        connection.close()
        return {
            "order_id": "not_found"
        }

    order_id, timestamp, cust_id, notes = row

    # Fetch item IDs associated with the order
    cursor.execute("SELECT item_id FROM item_list WHERE order_id = ?;", (order_id,))
    item_list = [r[0] for r in cursor.fetchall()]

    connection.close()

    return {
        "order_id": order_id,
        "timestamp": timestamp,
        "cust_id": cust_id,
        "notes": notes,
        "items": item_list
    }

@app.post("/order")
async def create_order(order:Order):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("SELECT * FROM customers WHERE id=?;",(order.cust_id,))
    if res.fetchone()==None:
        raise HTTPException(404,"Customer not found")
    for item_id in order.item_list:
        res=cursor.execute("SELECT * FROM items WHERE id=?;",(item_id,))
        if res.fetchone()==None:
            raise HTTPException(404,"Item id not in DB")



    res=cursor.execute("INSERT INTO orders (cust_id, notes) VALUES (?, ?);", (order.cust_id, order.notes))
    order_id = cursor.lastrowid
    res=cursor.execute("SELECT timestamp FROM orders WHERE id=?;",(order_id,))
    row=res.fetchone()
    timestamp=row[0]
    for item_id in order.item_list:
        cursor.execute("INSERT INTO item_list (order_id, item_id) VALUES (?, ?);", (order_id, item_id))
    connection.commit()
    connection.close()
    order.order_id=order_id
    order.timestamp=timestamp
    return order

    

@app.delete("/order/{order_id}")
def delete_item(order_id):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("DELETE FROM orders WHERE id=?;", (order_id,))
    if cursor.rowcount==0:
        connection.commit()
        connection.close()
        raise HTTPException(404,"Item not found")
    connection.commit()
    connection.close()
    return

@app.get("/item/{item_id}")
def get_item(item_id):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    initializeDB()
    res=cursor.execute("select id,name,price,item_id from items where id=?;",(item_id,))
    row=res.fetchone()
    item_id, name, price = row


    return {
            "item_id":row[0],
            "name":row[1],
            "price":row[2],
        }

@app.post("/item")
async def create_item(item:Item):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("INSERT INTO items (name, price) VALUES (?, ?);", (item.name, item.price))
    item_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return {
        "item_id":item_id,
        "name":item.name,
        "price":item.price,
    }

@app.delete("/item/{item_id}")
def delete_item(item_id):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("DELETE FROM items WHERE id=?;", (item_id,))
    if cursor.rowcount==0:
        connection.commit()
        connection.close()
        raise HTTPException(404,"Item not found")
    connection.commit()
    connection.close()
    return


@app.get("/customer/{cust_id}")
def get_item(cust_id):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("select id,name,phone from customers where id=?;",(cust_id,))
    row=res.fetchone()
    cust_id, name, phone = row

    return {
        "cust_id":row[0],
        "name":row[1],
        "phone":row[2],

    }


@app.post("/customer")
async def create_customer(customer:Customer):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?);", (customer.name, customer.phone))
    cust_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return {
        "cust_id":cust_id,
        "name":customer.name,
        "phone":customer.phone,
    }

@app.delete("/customer/{cust_id}")
def delete_item(cust_id):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    res=cursor.execute("DELETE FROM customers WHERE id=?;", (cust_id,))
    if cursor.rowcount==0:
        connection.commit()
        connection.close()
        raise HTTPException(404,"Item not found")
    connection.commit()
    connection.close()
    return




def initializeDB():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price REAL NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            cust_id INTEGER NOT NULL,
            notes TEXT,
            FOREIGN KEY (cust_id) REFERENCES customers(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS item_list (
            order_id INTEGER,
            item_id INTEGER,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (item_id) REFERENCES items(id)
        );
    """)

    # Load data from JSON
    with open("example_orders.json") as fp:
        orders = json.load(fp)

        for order in orders:
            name = order["name"]
            phone = order["phone"]
            timestamp = order["timestamp"]
            notes = order["notes"]
            item_list = order["items"]

            # Insert customer if not exists
            cursor.execute("SELECT id FROM customers WHERE phone = ?;", (phone,))
            result = cursor.fetchone()
            if result:
                cust_id = result[0]
            else:
                cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?);", (name, phone))
                cust_id = cursor.lastrowid

            # Insert order
            cursor.execute("INSERT INTO orders (timestamp, cust_id, notes) VALUES (?, ?, ?);",
                           (timestamp, cust_id, notes))
            order_id = cursor.lastrowid

            for item in item_list:
                item_name = item["name"]
                item_price = item["price"]

                # Insert item if not exists
                cursor.execute("SELECT id FROM items WHERE name = ?;", (item_name,))
                item_res = cursor.fetchone()
                if item_res:
                    item_id = item_res[0]
                else:
                    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?);", (item_name, item_price))
                    item_id = cursor.lastrowid

                # Link item to order
                cursor.execute("INSERT INTO item_list (order_id, item_id) VALUES (?, ?);", (order_id, item_id))

    connection.commit()
    connection.close()
