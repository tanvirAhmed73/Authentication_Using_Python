from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False)
    email = Column(String(50),nullable=False, index=True, unique=True)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=False)
    