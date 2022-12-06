from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()


# Read All
@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()
# Read specific
@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()
# Create User
@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        account = user.account,
        password = user.password,
        identity = 0
    ))
    return conn.execute(users.select()).fetchall()

# Update User
@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().where(users.c.id == id).values(
        account = user.account,
        password = user.password,
        identity = user.identity
    ))
    return conn.execute(users.select()).fetchall()

# Delete USer
@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id)).fetchall()
    return conn.execute(users.select()).fetchall()