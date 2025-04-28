# Dosa Restaurant REST API Final Project Report

## Overview

The Dosa Restaurant REST API project focuses on building a backend system for managing a restaurant's operations. It utilizes FastAPI, a modern and high-performance Python web framework, for API development and SQLite as the database solution for data persistence. The system provides full CRUD (Create, Read, Update, Delete) functionalities for three primary entities: Customers, Items (Dosas), and Orders.

The backend database, `db.sqlite`, is initialized from scratch using a script that processes data from a sample JSON file, `example_orders.json`. This data closely resembles the sample provided in the midterm project, ensuring consistency in application flow and data management processes.

The project directory is organized with key files, including the FastAPI application (`main.py`), the database initialization script (`init_db.py`), input and output JSON files (`example_orders.json`, `customers.json`, `items.json`), and additional helper scripts (`process_orders.py`) that were adapted from earlier coursework. The provided `README.md` file documents setup instructions and usage guidelines for ease of understanding.

## Project Structure

The project's folder hierarchy is designed to separate concerns effectively. The database file (`db.sqlite`) is automatically created through the `init_db.py` script, setting up the necessary database schema. The primary application logic resides in `main.py`, where the API routes are defined. The sample input file (`example_orders.json`) provides realistic order data, which is then processed to generate structured outputs in `customers.json` and `items.json`. These output files serve to map customer phone numbers to names and to organize item-related information such as pricing and order frequency.

## Setup and Execution Instructions

To set up the project environment, it is necessary to use Visual Studio Code or a similar integrated development environment. The user must open the terminal in the correct project directory. Before running the application, a virtual environment must be activated using the appropriate command for the operating system (for example, `venv\Scripts\activate` on Windows).

After activating the virtual environment, the user should start the FastAPI application by executing the command `uvicorn main:app --reload`. This will launch the API server and make it accessible at the local URL `http://127.0.0.1:8000`.

Using this base URL, specific resource endpoints can be accessed. For example, to retrieve order details, the user can navigate to `http://127.0.0.1:8000/order/{order_id}`, substituting `{order_id}` with the actual order number. Similarly, customer and item details can be retrieved using the appropriate URLs: `http://127.0.0.1:8000/customer/{customer_id}` and `http://127.0.0.1:8000/item/{item_id}`, respectively.

For more advanced operations such as creating, updating, or deleting customers, items, and orders, the FastAPI Swagger UI is available at `http://127.0.0.1:8000/docs`. The Swagger interface provides an interactive documentation page where users can execute API calls directly from the browser without the need for external tools like Postman.

## API Endpoints

The API exposes a consistent set of endpoints for managing customers, items, and orders. Each resource supports the standard HTTP methods associated with CRUD operations:

- `POST /customer`: Creates a new customer entry in the database.
- `GET /customer/{id}`: Retrieves the details of a specific customer by their ID.
- `PUT /customer/{id}`: Updates the details of an existing customer using their ID.
- `DELETE /customer/{id}`: Deletes a customer from the database by their ID.
- `POST /items`: Creates a new item (Dosa) entry in the system.
- `GET /item/{id}`: Retrieves details of a specific item based on its ID.
- `PUT /item/{id}`: Updates an existing item entry by ID.
- `DELETE /item/{id}`: Deletes an item from the menu by ID.
- `POST /orders`: Creates a new order.
- `GET /order/{id}`: Retrieves details of a specific order using the order ID.
- `PUT /order/{id}`: Updates the details of an order.
- `DELETE /order/{id}`: Deletes an order from the system by its ID.

Each of these endpoints has been designed to follow RESTful principles, ensuring that interactions with the system are logical, predictable, and aligned with best practices in API design.

## Conclusion

The Dosa Restaurant REST API project successfully demonstrates the design and implementation of a complete backend system for a restaurant management application. By leveraging FastAPI and SQLite, the system achieves efficient performance, ease of deployment, and scalability for small- to medium-sized restaurant operations. The modular project structure, comprehensive API documentation, and user-friendly setup instructions ensure that the system is accessible to both developers and end-users aiming to manage customer information, menu items, and order records efficiently.
