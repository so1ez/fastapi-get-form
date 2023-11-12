"""Database creation and connection file. If main - configure db with test data"""

import json

import pymongo

from settings import SETTINGS

client = pymongo.MongoClient(SETTINGS.DB_CONNECTION)
db = client[SETTINGS.DB_NAME]
collection = db[SETTINGS.DB_COLLECTION_NAME]


if __name__ == "__main__":
    collection.delete_many({})
    with open('db_test_data.json', encoding='utf-8') as file:
        test_data = json.load(file)
        collection.insert_many(test_data)

    for doc in collection.find():
        print(f"document: {doc}")

    print("--- Конец вывода данных ---")
