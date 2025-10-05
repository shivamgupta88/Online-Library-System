# Online Library System

A simple REST API for managing library operations built with FastAPI and MongoDB.

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
git clone <your-repo-url>
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

### Books

**Create Book**
```
POST /books/
{
  "title": "Book Title",
  "author": "Author Name",
  "copies_available": 5
}
```

**Get All Books**
```
GET /books/
```

**Search Books**
```
GET /books/search?q=query
```

### Users

**Create User**
```
POST /users/
{
  "name": "User Name"
}
```

**Get All Users**
```
GET /users/
```

**Get User by ID**
```
GET /users/{user_id}
```

### Library Operations

**Borrow Book**
```
POST /library/borrow
{
  "user_id": 1,
  "book_id": 1
}
```

**Return Book**
```
POST /library/return
{
  "user_id": 1,
  "book_id": 1
}
```

**Get Reports**
```
GET /library/reports
```

Returns most borrowed book and user with most books borrowed.

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
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"1984","author":"George Orwell","copies_available":3}'

# Create a user
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe"}'

# Borrow a book
curl -X POST http://localhost:8000/library/borrow \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"book_id":1}'
```
