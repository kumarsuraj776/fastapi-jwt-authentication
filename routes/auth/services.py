from fastapi import HTTPException
from models.user import User
from core.security import verify_password
from core.config import get_settings

settings=get_settings()

async def get_token(data, db):
    # Check if the user exist or not
    user=db.query(User).filter(User.email==data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found", headers={"WWW-Authenticate":"Bearer"})
    
    # Check if the password is correct or not (Verify the user)
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=404, detail="Incorrect password", headers={"WWW-Authenticate":"Bearer"})
    
    
    _verify_user_access(user=user)
    
    # Generate and return access token and refresh token
    access_token = await get_access_token(user=user, db=db)
    refresh_token = await get_refresh_token(user=user, db=db)
    
    payload={
        "access_token":access_token,
        "refresh_token":refresh_token
    }
    return payload
    
    
     
def _verify_user_access(user:User):
    if not user.is_active:
        raise HTTPException(status_code=404, detail="User is not active. Please contact support", headers={"WWW-Authenticate":"Bearer"})
    
    if not user.is_verified:
        # User email account verification/Trigger user account verification email
        raise HTTPException(status_code=404, detail="User account is not verified. We have resent account verification email. Please check your email", headers={"WWW-Authenticate":"Bearer"})


# To generate refresh token(if we already have it, we will send it)
def _get_user_token(user:User, refresh_token:str=None):
    
    access_token_expiry:int=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    refresh_token_expiry:int=settings.REFRESH_TOKEN_EXPIRE_MINUTES
    

    

        