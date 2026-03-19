from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from fastapi import HTTPException

import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
ALGORITHM = "HS256"

def hash_password(password: str):
    return pwd_context.hash(password[:72])

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)


def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)   

def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="Invalid token")
        