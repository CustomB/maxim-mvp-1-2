from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from src.bot import Bot
from src.interfaces import MessageRequest

app = FastAPI()
client = MongoClient("mongodb+srv://roma:romapass1234@cluster0.cesn4er.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))


@app.post("/talk/")
async def talk(req: MessageRequest):
    db = client["maxim-avatars"]

    bots_collection = db["users_messages"]

    bot_filter = {"user_id": req.user_id, "bot_role": req.bot_role}
    existing_bot = bots_collection.find_one(bot_filter)

    if existing_bot is None:
        new_bot = {
            "bot_role": req.bot_role,
            "user_id": req.user_id,
            "messages": [{"role": "user", "content": req.message}]
        }
        bots_collection.insert_one(new_bot)
        messages = new_bot["messages"]
    else:
        messages = existing_bot["messages"]
        user_message_formatted = {"role": "user", "content": req.message}
        messages.append(user_message_formatted)
        bots_collection.update_one(bot_filter, {"$push": {"messages": user_message_formatted}})

    context_collection = db["bots"]
    context = context_collection.find_one({"role": req.bot_role})

    bot = Bot(gender=context['gender'], age=context['age'], name=context['name'], role=context['role'], history=messages)
    bot_answer = bot.run(messages[-6:])
    bot_answer_formatted = {"role": "assistant", "content": bot_answer}
    messages.append(bot_answer_formatted)

    bots_collection.update_one(bot_filter, {"$push": {"messages": bot_answer_formatted}})
    return messages[-6:]
