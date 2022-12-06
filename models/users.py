from sqlalchemy import Table, Column, Index
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta
users = Table(
    'users',meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('account',String(255)),
    Column('password',String(255)),
    Column('identity',Integer)
)


# class users(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     account = Column(String(255))
#     password = Column(String(255))
#     identity = Column(Integer)