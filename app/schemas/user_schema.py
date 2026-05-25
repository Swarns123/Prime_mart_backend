from __future__ import annotations
from pydantic import BaseModel

class UserCreate(BaseModel):
	username: str
	password: str
      
class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True