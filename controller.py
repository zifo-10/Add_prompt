from pymongo import MongoClient

def insert(mongo_uri, db_name, user, system, name):
    try:
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db["prompt"]
        inserted = collection.insert_one({"user": user, "system": system, "name": name})
        if inserted.inserted_id:
            return True
        return False
    except Exception as e:
        return False
