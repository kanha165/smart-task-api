from fastapi import APIRouter,HTTPException
from models import User
from database import get_db_connection
from auth import hash_password, verify_password, create_token, verify_token, verify_token
router = APIRouter()

@router.post("/signup")
def signup(user: User):
    conn=get_db_connection()
    cursor=conn.cursor()
    hashed=hash_password(user.password)
    query="INSERT INTO users (username,password) VALUES (%s,%s)"
    cursor.execute(query,(user.username,hashed))
    conn.commit()
    cursor.close()
    conn.close()
    return{"msg":"User created successfully"}



@router.post("/login")
def login(user: User):
    conn=get_db_connection()
    cursor=conn.cursor()
    query="SELECT * FROM users WHERE username=%s"
    cursor.execute(query,(user.username,))
    db_user=cursor.fetchone()
    if not db_user:
        raise HTTPException(status_code=404,detail="user not found")
    store_password=db_user[2]
    if not verify_password(user.password,store_password):
        raise HTTPException(status_code=401,detail="wrong password")
    token=create_token({"sub":user.username})
    return{"access_token":token}


from fastapi.security import HTTPBearer
from fastapi import Depends

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    return verify_token(token.credentials)


@router.get("/profile")
def profile(user=Depends(get_current_user)):
    return{"msg":"user name  accesssed","user":user}