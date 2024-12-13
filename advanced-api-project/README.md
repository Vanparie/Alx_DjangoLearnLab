# Advanced API Project

This project demonstrates CRUD operations for a `Book` model using Django REST Framework. It includes fine-grained permission handling and a modular approach for scalability.

## Features
- Generic views for CRUD operations.
- Token-based authentication for protected endpoints.
- Clear documentation and code comments.

## Endpoints
| **Endpoint**                | **Method** | **Description**           | **Access**           |
|-----------------------------|------------|---------------------------|----------------------|
| `/api/books/`               | GET        | List all books            | Public               |
| `/api/books/<id>/`          | GET        | Retrieve details of a book| Public               |
| `/api/books/create/`        | POST       | Create a new book         | Authenticated users  |
| `/api/books/<id>/update/`   | PUT        | Update an existing book   | Authenticated users  |
| `/api/books/<id>/delete/`   | DELETE     | Delete a book             | Authenticated users  |

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/advanced_api_project
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Authentication
To access protected endpoints:
1. Obtain a token:
    ```bash
    python manage.py drf_create_token <username>
    ```

2. Include the token in your API requests:
    ```http
    Authorization: Token <your-token>
    ```

## Testing
Use Postman or curl to test CRUD operations. Verify authentication by attempting access with and without tokens.


## Advanced Query Capabilities for Book API

### Features
1. **Filtering:**
   - Filter books by `title`, `author`, or `publication_year`.
   - Example: `/api/books/?author__name=George Orwell`

2. **Searching:**
   - Search books by `title` or `author`.
   - Example: `/api/books/?search=1984`

3. **Ordering:**
   - Order books by `title` or `publication_year` (ascending or descending).
   - Example (ascending): `/api/books/?ordering=publication_year`
   - Example (descending): `/api/books/?ordering=-title`

### How to Test
Use Postman, curl, or any HTTP client to test the API endpoints with query parameters.

### URL Endpoints
- **Base URL:** `/api/books/`
- **Query Parameters:** `?field=value`, `?search=query`, `?ordering=field`
