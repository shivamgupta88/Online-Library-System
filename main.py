from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.site import router as site_router
from routes.books import router as books_router
from routes.users import router as users_router
from config.connectDb import connect_db,close_db

@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    await connect_db()
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)
app.include_router(site_router)
app.include_router(books_router)
app.include_router(users_router)

@app.get("/health")
def health():
    return {"status":"ok","msg":"service healthy"}