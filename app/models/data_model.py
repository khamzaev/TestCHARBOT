from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.db import Base


class DataModel(Base):
    """
    Модель для представления данных в базе данных.
    """
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)


class APIData(BaseModel):
    """
    Pydantic-модель для валидации данных, полученных из API.
    """
    id: int
    user_id: int
    title: str
    body: str
