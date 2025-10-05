from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from models import book,user

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL","mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME","library_db")

client = None
db = None

async def connect_db():
    global client,db
    try:
        client = AsyncIOMotorClient(MONGO_URL)
        db = client[DB_NAME]
        await book.setup_indexes(db)
        await user.setup_indexes(db)
        print("connected to mongodb")
    except Exception as e:
        print(f"error connecting to db: {e}")

async def close_db():
    global client
    if client:
        client.close()
        print("db connection closed")

def get_db():
    return db
