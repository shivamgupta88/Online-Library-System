from fastapi import APIRouter, HTTPException
from models.user import User,UserCreate
from controllers.user_controller import register_user,get_all_users,get_user

router=APIRouter(prefix="/users", tags=["users"])

@router.post("/",response_model=User)
async def create_user(user: UserCreate):
    result=await register_user(user)
    return result

@router.get("/")
async def list_users():
    users = await get_all_users()
    return users

@router.get("/{user_id}")
async def get_user_detail(user_id:int):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user
