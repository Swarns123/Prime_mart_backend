from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base_products, Base_users
import datetime
import hashlib
import hmac
import os

class Product(Base_products):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

class User(Base_users):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    def set_password(self, password: str):
        """Hash the password and store it."""
        salt = os.urandom(16)  # Generate a random salt
        self.password_hash = self.hash_password(password, salt)

    def verify_password(self, password: str) -> bool:
        """Verify the provided password against the stored hash."""
        return hmac.compare_digest(self.password_hash, self.hash_password(password))

    @staticmethod
    def hash_password(password: str, salt: bytes) -> str:
        """Hash the password using HMAC with SHA256."""
        return hmac.new(salt, password.encode('utf-8'), hashlib.sha256).hexdigest()