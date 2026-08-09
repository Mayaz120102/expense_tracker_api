from datetime import date

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String

from database import Base


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)


class Transaction(Base):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String)
    date = Column(Date, default=date.today, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), index=True)
    