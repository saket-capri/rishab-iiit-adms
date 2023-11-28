from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.orm import Session
from database.db import *
from schema.schemas import *
from fastapi import Depends, FastAPI, HTTPException, status

from typing import Annotated , Optional, Any, Union 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class UserModel(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    email = Column(String, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    
def fake_hash_password(password: str):
    return "fakehashed" + password 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(username: str, password: str, 
                      db: Session) -> Union[UserModel, None]:
    user = db.query(UserModel).filter(UserModel.username == username).first()
    password = fake_hash_password(password)
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # You should use a secure password hashing library like bcrypt in a real-world scenario
    return plain_password == hashed_password
    
async def fake_decode_token(token: str = Depends(oauth2_scheme), 
            db: Session = Depends(get_db)):
    username = verify_token(token)
    if username is None:
        return None
    
    user = db.query(UserModel).filter(UserModel.username == username).first()
    return user

def verify_token(token: str) -> Optional[str]:
    return token

async def get_current_user(current_user: User = Depends(fake_decode_token)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

