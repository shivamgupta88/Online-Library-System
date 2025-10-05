from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id:int
    name: str
    borrowed_books: List[int] = []

class UserCreate(BaseModel):
    name:str

async def setup_indexes(db):
    await db.users.create_index("id", unique=True)
