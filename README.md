**Dosa Restaurant REST API (Final Project)**

**Overview**
This project implements a REST API backend for a Dosa restaurant. It uses FastAPI for building the API and SQLite for database storage. The API provides full CRUD (Create, Read, Update, Delete) operations for three key entities:CustomersItems (Dosas)Orders.The backend database (db.sqlite) is initialized from scratch using a provided script based on data similar to the midterm project's example_orders.json.

**dosa_restaurant_project file:**
├── db.sqlite          # SQLite database (created by init_db.py)
├── init_db.py         # Initializes the database schema
├── main.py            # FastAPI application with endpoints
├── example_orders.json # Sample input data
├── process_orders.py  # (From midterm) Processes example_orders.json
├── customers.json     # (Generated output) Mapping phone -> customer names
├── items.json         # (Generated output) Item prices and order counts
├── README.md          # This documentation

**Setup Instructions**
Go to visual studio editor go to the desired terminal to run main.py a python file that has all the rest api's in it.Navigate the terminal to the right path and activate the virtual enviormet setup using venv activcate scipts.Then use fastapi dev main.py command to run it. Then api calls will runa dn genberate thius url 
http://127.0.0.1:8000 use this to run orders like http://127.0.0.1:8000/order/orderno.similarly do it for items and customers to get the details based on the order no , item no and customer id.To do put, post and delete go to Swagger UI: http://127.0.0.1:8000/docs which helps yoyu perform all other api actions


Method	Path	Description
POST	/customer	Create a customer
GET	/customer/{id}	Retrieve a customer by ID
PUT	/customer/{id}	Update a customer by ID
DELETE	/customer/{id}	Delete a customer by ID
POST	/items	Create an item
GET	/item/{id}	Retrieve an item by ID
PUT	/item/{id}	Update an item by ID
DELETE	/item/{id}	Delete an item by ID
POST	/orders	Create an order
GET	/order/{id}	Retrieve an order by ID
PUT	/order/{id}	Update an order by ID
DELETE	/order/{id}	Delete an order by ID

