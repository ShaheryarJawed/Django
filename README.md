# Stock Management API

This project is a Django-based stock management system that allows users to register, manage stock prices, and handle stock transactions (buy/sell). The API also provides endpoints for user balance management and transactions.

## Features

- **User Management**: Create and retrieve users.
- **Stock Management**: Add new stocks and list available stocks.
- **Transaction Management**: Perform stock transactions (buy/sell) with balance validation.
- **Transaction History**: Retrieve transaction history by user and filter by timestamp.

## Tech Stack

- **Django**: 5.1.1
- **Django REST Framework**: 3.15.2
- **PostgreSQL**: via psycopg2
- **drf-yasg**: 1.21.7 for API documentation

## Requirements

- Python 3.x
- PostgreSQL
- pip

## Installation

1. Clone the repository:
   ```bash
   [git clone https://github.com/your-repository-link.git](https://github.com/shaheryarjawed/django)

2. Navigate into the project directory: 
   
    cd stock_exchange_project

3. Install the required dependencies: 
     pip install -r requirements.txt
   
5. Set up the PostgreSQL database and configure the connection in settings.py.

6. Run migrations to set up the database schema: 

   python manage.py migrate
  
7. Start the development server:
   python manage.py runserver

   
## API Endpoints

| Endpoint                                      | Method | Description                                       |
|-----------------------------------------------|--------|---------------------------------------------------|
| `/users/`                                     | POST   | Create a new user.                                |
| `/users/<str:username>/`                      | GET    | Retrieve user details by username.                |
| `/create_stock/`                              | POST   | Create a new stock.                               |
| `/stocks/`                                    | GET    | List all available stocks.                        |
| `/stocks/<str:ticker>/`                       | GET    | Retrieve stock data by ticker.                    |
| `/transactions/`                              | POST   | Create a new transaction (Buy/Sell stock).        |
| `/transactions/<str:username>/`               | GET    | List all transactions for a specific user.        |
| `/transactions/<str:username>/<str:start_time>/<str:end_time>/` | GET | List transactions by user within a time range.    |


API Documentation
This project uses drf-yasg to generate and display interactive API documentation. You can view it at:
http://127.0.0.1:8000/swagger/

Contact
If you have any questions, feel free to contact me at shaheryar.jawed000@gmail.com





## GIVEN TASK:

## API Endpoints
- **POST** `/users/`: To register a new user with a username and initial balance.
- **GET** `/users/{username}/`: To retrieve user data.
- **POST** `/stocks/`: To ingest stock data and store it in the Postgres database.
- **GET** `/stocks/`: To retrieve all stock data.
- **GET** `/stocks/{ticker}/`: To retrieve specific stock data.
- **POST** `/transactions/`: To post a new transaction. This should take `user_id`, `ticker`, `transaction_type`, and `transaction_volume` as inputs. The endpoint should calculate the `transaction_price` based on the current stock price and update the user's balance.
- **GET** `/transactions/{user_id}/`: To retrieve all transactions of a specific user.
- **GET** `/transactions/{user_id}/{start_timestamp}/{end_timestamp}/`: To retrieve transactions of a specific user between two timestamps.

## Instructions

- Add Swagger documentation.
- Ensure the processing validates the transaction (e.g., check if the user has enough balance for a buy transaction) and updates the `Users` and `Transactions` tables accordingly.
- Send a Pull Request (PR) for the REST API app.
- Add a `README.md` file to provide clear instructions on setting up and running the project on any machine.
- Follow the standard practices for writing the REST API app.



## pending
- authentication
- Implementing required fields in Swagger for improved validation.
