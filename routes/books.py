from fastapi import APIRouter,HTTPException
from models.book import Book, BookCreate
from controllers.book_controller import add_book,get_all_books,search_books

router = APIRouter(prefix="/books",tags=["books"])

@router.post("/",response_model=Book)
async def create_book(book:BookCreate):
    result = await add_book(book)
    return result

@router.get("/")
async def list_books():
    books=await get_all_books()
    return books

@router.get("/search")
async def search(q: str):
    if not q:
        raise HTTPException(status_code=400,detail="query parameter required")
    books = await search_books(q)
    return books
