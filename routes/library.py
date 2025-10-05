from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from controllers.library_controller import borrow_book,return_book, get_reports

router = APIRouter(prefix="/library",tags=["library"])

class BorrowRequest(BaseModel):
    user_id: int
    book_id:int

class ReturnRequest(BaseModel):
    user_id:int
    book_id: int

@router.post("/borrow")
async def borrow(req: BorrowRequest):
    result = await borrow_book(req.user_id,req.book_id)
    if "error" in result:
        raise HTTPException(status_code=400,detail=result["error"])
    return result

@router.post("/return")
async def return_book_route(req:ReturnRequest):
    result=await return_book(req.user_id, req.book_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/reports")
async def reports():
    report = await get_reports()
    return report
