from __future__ import annotations
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    price: float
    

class ProductBase(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float
    class Config:
        orm_mode = True
