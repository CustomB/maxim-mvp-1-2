import os
import pymongo
from dotenv import load_dotenv
from src.logger import logging

load_dotenv()

def create_collection_if_not_exists(collection_name: str) -> None:
    try:
        db.create_collection(collection_name)
    except Exception as e:
        logging.info(e)
    else:
        logging.info(f"Succefully created collection {collection_name}.")


if __name__ == "__main__":
    client = pymongo.MongoClient(os.getenv('MONGO_URL'))
    db = client['maxim-avatars']
    create_collection_if_not_exists("users_messages")
    create_collection_if_not_exists("bots")

