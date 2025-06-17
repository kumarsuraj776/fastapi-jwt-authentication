from models.user import User as UserModel
from fastapi import HTTPException
from sqlalchemy.sql import func
from core.security import get_password_hash

# Create/Register a user
async def create_user_account(data, db):
    user=db.query(UserModel).filter(UserModel.email==data.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    new_user=UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_password_hash(data.password),
        is_active=False
    )
    
    # Saving the user in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user