from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author:str
    copies_available: int
    total_borrows: int = 0

class BookCreate(BaseModel):
    title: str
    author: str
    copies_available:int

async def setup_indexes(db):
    await db.books.create_index("id",unique=True)
