from fastapi import FastAPI
from routes.site import router as site_router

app = FastAPI()
app.include_router(site_router)

@app.get("/health")
def health():
    return {"status":"ok","msg":"service healthy"}