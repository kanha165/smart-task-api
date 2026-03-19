from fastapi import APIRouter, Depends, HTTPException
from database import get_db_connection
from models import Task
from auth import verify_token
from utils import get_priority
from routes.user import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task, user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    priority = get_priority(task.description)

    query = "INSERT INTO tasks (title, description, priority, status, user_id) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(query, (
        task.title,
        task.description,
        priority,
        "pending",
        user["sub"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"msg": "Task created", "priority": priority}




@router.get("/tasks")
def get_tasks(user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE user_id=%s"
    cursor.execute(query, (user["sub"],))

    data = cursor.fetchall()

    return {"tasks": data}



@router.put("/tasks/{id}")
def update_task(id: int, task: Task, user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    priority = get_priority(task.description)

    query = "UPDATE tasks SET title=%s, description=%s, priority=%s WHERE id=%s AND user_id=%s"

    cursor.execute(query, (
        task.title,
        task.description,
        priority,
        id,
        user["sub"]
    ))

    conn.commit()

    return {"msg": "Task updated"}


@router.delete("/tasks/{id}")
def delete_task(id: int, user=Depends(get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id=%s AND user_id=%s"
    cursor.execute(query, (id, user["sub"]))

    conn.commit()

    return {"msg": "Task deleted"}