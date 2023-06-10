from sqlalchemy import Column, Integer, String
from ..Services.ServiceBase import MySqlServiceBase


class User(MySqlServiceBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
