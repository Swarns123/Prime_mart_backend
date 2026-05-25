from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import Base, engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Prime Mart Backend Running"}

@app.post("/products/")
def create_product(db: Session = Depends(get_db)):
    return {"message": "Product created successfully"}