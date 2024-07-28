from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime  

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False)
    date_published = Column(DateTime, nullable=False)