from pydantic import BaseModel

#user model
class User(BaseModel):
    username: str
    password: str
    
    
#task model
class Task(BaseModel):
    title: str
    description: str
      