from config.connectDb import get_db
from models.book import Book,BookCreate

async def add_book(book: BookCreate):
    db=get_db()
    # get next id
    last_book = await db.books.find_one(sort=[("id",-1)])
    new_id = 1 if not last_book else last_book["id"]+1

    book_data={
        "id":new_id,
        "title":book.title,
        "author": book.author,
        "copies_available":book.copies_available,
        "total_borrows":0
    }
    await db.books.insert_one(book_data)
    return book_data

async def get_all_books():
    db = get_db()
    books=[]
    cursor=db.books.find({})
    async for b in cursor:
        del b["_id"]
        books.append(b)
    return books

async def search_books(query:str):
    db=get_db()
    books = []
    cursor = db.books.find({
        "$or":[
            {"title":{"$regex":query,"$options":"i"}},
            {"author":{"$regex":query,"$options":"i"}}
        ]
    })
    async for book in cursor:
        del book["_id"]
        books.append(book)
    return books

async def get_book_by_id(bookId:int):
    db = get_db()
    book = await db.books.find_one({"id":bookId})
    if book:
        del book["_id"]
    return book
