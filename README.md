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

3. Run database init:
```bash
py pre_start.py
```

4. Start the server:
```bash
uv run fastapi dev
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

## Screenshots
Login: ![image](https://github.com/user-attachments/assets/8bda2229-6680-49bb-8177-9fbe9e7be9a0)

Create product: ![image](https://github.com/user-attachments/assets/84dc0741-4565-4b02-be1d-3d6b8409fb17)
Get product by id: ![image](https://github.com/user-attachments/assets/64d939dc-9455-4523-b55d-0c78f2cbbc12)
Update Product: ![image](https://github.com/user-attachments/assets/bbbc2ffe-2fbb-44c0-b1d8-a02aa2c405c2)
Get all products: ![image](https://github.com/user-attachments/assets/626170ef-f1ef-4df0-833a-ddd8c70f8912)

Get current user: ![image](https://github.com/user-attachments/assets/f849dbf0-a965-408a-9fc8-b59ddd88e86a)

Create order: ![image](https://github.com/user-attachments/assets/5ff77d47-c857-4938-a7b4-ac804d0013d4)
Get all orders: ![image](https://github.com/user-attachments/assets/110abd8a-e60e-4552-b120-3147ae72cb6f)


