import pymongo

from src.logger import logging


def create_collection_if_not_exists(collection_name: str) -> None:
    try:
        db.create_collection(collection_name)
    except Exception as e:
        logging.info(e)
    else:
        logging.info(f"Succefully created collection {collection_name}.")


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://roma:romapass1234@cluster0.cesn4er.mongodb.net/?retryWrites=true&w=majority")
    db = client['maxim-avatars']
    create_collection_if_not_exists("users_messages")
    create_collection_if_not_exists("bots")

