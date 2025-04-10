from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.db import Base

class DataModel(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)


class APIData(BaseModel):
    id: int
    user_id: int
    title: str
    body: str