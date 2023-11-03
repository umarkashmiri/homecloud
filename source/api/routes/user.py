from fastapi import APIRouter

from models.user import User

from config.db import con
from bson import ObjectId

from schema.user import userEntity, usersEntity

user = APIRouter()


@user.get('/')
async def find_all_users():
    print(con.local.user.find())
    print(usersEntity(con.local.user.find()))
    return usersEntity(con.local.user.find())

@user.get('/{id}')
async def find_one(id):
    return userEntity(con.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    con.local.user.insert_one(dict(user))
    return usersEntity(con.local.user.find())


@user.put('/{id}')
async def update_user(id, user: User):
    con.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set", dict(user)})
    return userEntity(con.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id, user: User):
    con.local.user.find_one_and_delete({"_id": ObjectId(id)})
    return userEntity(con.local.user.find_one({"_id": ObjectId(id)}))