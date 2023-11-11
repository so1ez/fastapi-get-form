"""db connection fil. If main - configure db with test data"""

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["testcollection"]

if __name__ == "__main__":
    collection.delete_many({})
    test_data = [{
        "name": "login template",
        "username": "text",
        "password": "text"
    },
    {
        "name": "register template",
        "username": "text",
        "email": "email",
        "phone": "phone"
    },
    {
        "name": "feedback template",
        "email": "email",
        "feedback": "text"
    },
    {
        "name": "logs template",
        "info": "text",
        "created_date": "date"
    },
    {
        "name": "simple date template",
        "created_date": "date"
    }]

    collection.insert_many(test_data)
    for doc in collection.find():
        print(f"document = {doc}")
