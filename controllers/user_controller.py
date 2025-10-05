from config.connectDb import get_db
from models.user import User,UserCreate

async def register_user(user:UserCreate):
    db = get_db()
    last_user=await db.users.find_one(sort=[("id", -1)])
    newId = 1 if not last_user else last_user["id"] + 1

    user_data = {
        "id": newId,
        "name":user.name,
        "borrowed_books":[]
    }
    await db.users.insert_one(user_data)
    return user_data

async def get_all_users():
    db=get_db()
    users = []
    cursor = db.users.find({})
    async for u in cursor:
        del u["_id"]
        users.append(u)
    return users

async def get_user(userId: int):
    db=get_db()
    user = await db.users.find_one({"id":userId})
    if user:
        del user["_id"]
    return user
