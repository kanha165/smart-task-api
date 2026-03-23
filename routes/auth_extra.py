otp_store = {}

from utils import send_email
import random

def generate_otp():
    return str(random.randint(1000, 9999))


from fastapi import APIRouter

router = APIRouter()

from utils import send_email

@router.post("/send-otp")
def send_otp(email: str):
    otp = generate_otp()

    otp_store[email] = otp

    print("OTP:", otp)   # debug

    send_email(email, otp)  

    return {"msg": "OTP sent successfully"}


@router.post("/verify-otp")
def verify_otp(email: str, otp: str):
    if otp_store.get(email) == otp:
        return {"msg": "OTP verified"}
    else:
        return {"msg": "Invalid OTP"}
    
    
    
from auth import hash_password
from database import get_db_connection

@router.post("/reset-password")
def reset_password(email: str, otp: str, new_password: str):

    # Step 1: OTP check
    if otp_store.get(email) != otp:
        return {"msg": "Invalid OTP"}

    # Step 2: Password hash
    hashed = hash_password(new_password)

    # Step 3: Update DB
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE users SET password=%s WHERE username=%s"
    cursor.execute(query, (hashed, email))
    conn.commit()

    cursor.close()
    conn.close()

    return {"msg": "Password updated successfully"}    