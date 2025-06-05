# Cashier App API

A FastAPI-based REST API for managing products, orders, and users.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Set up environment variables:
```bash
# Create .env file with the following variables
DATABASE_URL=postgresql://user:password@localhost:5432/cashier_db
SECRET_KEY=your-secret-key
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=admin123
```

4. Run database init:
```bash
py pre_start.py
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Endpoints

### Authentication

- `POST /auth/login` - Login to get access token
- `POST /auth/register` - Register a new user

### Users

- `GET /users/me` - Get current user info
- `GET /users/id/{user_id}` - Get user by ID

### Products

- `GET /products` - List all products
- `GET /products/{product_id}` - Get product by ID
- `POST /products` - Create new product (superuser only)
- `PUT /products/{product_id}` - Update product (superuser only)
- `DELETE /products/{product_id}` - Delete product (superuser only)

### Orders

- `GET /orders` - List all orders for current user
- `GET /orders/{order_id}` - Get order by ID
- `POST /orders` - Create new order
