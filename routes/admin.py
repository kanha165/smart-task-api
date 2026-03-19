from fastapi import APIRouter, Depends
from database import get_db_connection
from routes.user import get_current_user

router = APIRouter()
@router.get("/admin/users")
def get_all_users(user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    return {"users": data}


@router.get("/admin/tasks")
def get_all_tasks(user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()

    return {"tasks": data}