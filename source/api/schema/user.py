def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]


def serializeEntity(entity) -> dict:
    return {**{i: str(entity[i]) for i in entity if i == '_id'}, **{i: entity[i] for i in entity if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeEntity(a) for a in entity]
