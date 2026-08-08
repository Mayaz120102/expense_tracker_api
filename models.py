from datetime import date

from sqlalchemy import Column, Date, ForeignKey, Integer, String

from database import Base


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)


class Transaction(Base):

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(String)
    category = Column(Integer)
    date = Column(Date, default=date.today, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    