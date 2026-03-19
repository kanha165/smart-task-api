from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return{"msg": "Smart Task Manager API is running"}


from database import get_db_connection
@app.get("/tasks-db")
def test_db():
    conn=get_db_connection()
    return{"msg":"DB connected"}


from routes import user
app.include_router(user.router)

from routes import task
app.include_router(task.router)

from routes import admin
app.include_router(admin.router)


from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    print("Response sent")
    return response