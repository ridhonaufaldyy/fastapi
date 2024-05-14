from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    nik = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    telp = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)
