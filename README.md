# Online Library System

A simple REST API for managing library operations built with FastAPI and MongoDB.

## Live Demo

API is deployed at: https://online-library-system-nk64.onrender.com/docs

## Features

- Book Management (CRUD operations)
- User Management
- Borrow and Return books
- Search books by title or author
- Generate reports (most borrowed books, most active users)

## Tech Stack

- **FastAPI** - Web framework
- **MongoDB** - Database
- **Motor** - Async MongoDB driver
- **Pydantic** - Data validation

## Setup

### Prerequisites
- Python 3.9+
- MongoDB running locally or connection string

### Installation

1. Clone the repo
```bash
git clone https://github.com/shivamgupta88/Online-Library-System
cd Online-Library-System
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file
```
MONGO_URL=mongodb://localhost:27017
DB_NAME=library_db
```

5. Run the server
```bash
uvicorn main:app --reload
```

Server will start at `http://localhost:8000`

API docs available at `http://localhost:8000/docs`

## API Endpoints

Base URL: https://online-library-system-nk64.onrender.com

### Books

**Create Book**
```
POST /books/
{
  "title": "book1",
  "author": "writer1",
  "copies_available": 5
}

Response:
{
  "id": 1,
  "title": "book1",
  "author": "writer1",
  "copies_available": 5,
  "total_borrows": 0
}
```

**Get All Books**
```
GET /books/

Response:
[
  {
    "id": 1,
    "title": "book1",
    "author": "writer1",
    "copies_available": 5,
    "total_borrows": 0
  }
]
```

**Search Books**
```
GET /books/search?q=book

Response: Array of matching books
```

### Users

**Create User**
```
POST /users/
{
  "name": "shivam"
}

Response:
{
  "id": 1,
  "name": "shivam",
  "borrowed_books": []
}
```

**Get All Users**
```
GET /users/

Response:
[
  {
    "id": 1,
    "name": "shivam",
    "borrowed_books": []
  }
]
```

**Get User by ID**
```
GET /users/1

Response:
{
  "id": 1,
  "name": "shivam",
  "borrowed_books": [1, 2]
}
```

### Library Operations

**Borrow Book**
```
POST /library/borrow
{
  "user_id": 1,
  "book_id": 1
}

Response:
{
  "message": "book borrowed successfully"
}
```

**Return Book**
```
POST /library/return
{
  "user_id": 1,
  "book_id": 1
}

Response:
{
  "message": "book returned successfully"
}
```

**Get Reports**
```
GET /library/reports

Response:
{
  "most_borrowed_book": {
    "id": 1,
    "title": "book1",
    "total_borrows": 5
  },
  "top_user": {
    "id": 1,
    "name": "shivam",
    "books_count": 3
  }
}
```

## Project Structure

```
.
├── main.py              # Entry point
├── config/
│   └── connectDb.py     # DB connection
├── models/
│   ├── book.py          # Book schema
│   └── user.py          # User schema
├── controllers/
│   ├── book_controller.py
│   ├── user_controller.py
│   └── library_controller.py
└── routes/
    ├── books.py
    ├── users.py
    └── library.py
```

## Notes

- IDs are auto-generated integers (not MongoDB _id)
- No authentication implemented (not required for this assignment)
- Books can be borrowed only if copies are available
- Users cannot borrow same book twice

## Testing

Use the interactive API docs at `/docs` or use curl/Postman

Example:
```bash
# Create a book
curl -X POST https://online-library-system-nk64.onrender.com/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"book1","author":"writer1","copies_available":3}'

# Create a user
curl -X POST https://online-library-system-nk64.onrender.com/users/ \
  -H "Content-Type: application/json" \
  -d '{"name":"shivam"}'

# Borrow a book
curl -X POST https://online-library-system-nk64.onrender.com/library/borrow \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"book_id":1}'
```
