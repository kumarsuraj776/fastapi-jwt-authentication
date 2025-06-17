from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.user import CreateUserRequest
from crud.user import create_user_account

# Creating user routes
router=APIRouter(prefix="/users", tags=["users"], responses={404:{"description":"Not found"}})


# Creating a new user
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(data:CreateUserRequest, db:Session=Depends(get_db)):
    user = await create_user_account(data=data, db=db)
    payload={
        "message":"User account created successfully",
        "user":{
            "id":user.id,
            "fullname":f"{user.first_name} {user.last_name}",
            "email":user.email
        }
    }
    return JSONResponse(content=payload)

