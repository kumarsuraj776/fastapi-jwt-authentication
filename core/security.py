from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/token")

# To hash the plain password
def get_password_hash(password):
    return pwd_context.hash(password)

# To verify the plain password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)