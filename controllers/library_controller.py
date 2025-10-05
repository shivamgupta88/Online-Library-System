from config.connectDb import get_db
from controllers.book_controller import get_book_by_id
from controllers.user_controller import get_user

async def borrow_book(user_id:int, book_id: int):
    db=get_db()

    user=await get_user(user_id)
    if not user:
        return {"error":"user not found"}

    book = await get_book_by_id(book_id)
    if not book:
        return {"error": "book not found"}

    if book["copies_available"] <=0:
        return {"error":"no copies available"}

    if book_id in user["borrowed_books"]:
        return {"error":"book already borrowed by user"}

    # update book
    await db.books.update_one(
        {"id":book_id},
        {"$inc":{"copies_available":-1,"total_borrows":1}}
    )

    # update user
    await db.users.update_one(
        {"id": user_id},
        {"$push":{"borrowed_books": book_id}}
    )

    return {"message":"book borrowed successfully"}

async def return_book(user_id: int,book_id:int):
    db = get_db()

    user = await get_user(user_id)
    if not user:
        return {"error":"user not found"}

    book=await get_book_by_id(book_id)
    if not book:
        return {"error":"book not found"}

    if book_id not in user["borrowed_books"]:
        return {"error": "user hasn't borrowed this book"}

    await db.books.update_one(
        {"id": book_id},
        {"$inc": {"copies_available":1}}
    )

    await db.users.update_one(
        {"id":user_id},
        {"$pull":{"borrowed_books":book_id}}
    )

    return {"message":"book returned successfully"}

async def get_reports():
    db = get_db()

    # most borrowed book
    most_borrowed = await db.books.find_one(sort=[("total_borrows",-1)])

    # user with most books borrowed
    pipeline=[
        {"$project": {"id":1, "name":1,"count": {"$size":"$borrowed_books"}}},
        {"$sort":{"count":-1}},
        {"$limit": 1}
    ]
    cursor = db.users.aggregate(pipeline)
    top_user = await cursor.to_list(length=1)
    top_user = top_user[0] if top_user else None

    report = {
        "most_borrowed_book": {
            "id": most_borrowed["id"],
            "title":most_borrowed["title"],
            "total_borrows": most_borrowed["total_borrows"]
        } if most_borrowed else None,
        "top_user":{
            "id":top_user["id"],
            "name": top_user["name"],
            "books_count":top_user["books_borrowed"]
        } if top_user else None
    }

    return report
