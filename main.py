from fastapi import FastAPI
from pydantic import BaseModel
from src.bot import Bot
from src.interfaces import MessageRequest



app = FastAPI()

guyBot = Bot(gender="Male", age=22, name="Jabari", role="regular guy")
girlBot = Bot(gender="Female", age=21, name="Caitlyn", role="regular girl")

bots = {
    "regular guy": guyBot,
    "regular girl": girlBot
}


@app.post("/talk/")
async def talk(req: MessageRequest):
    return {"response": bots[req.bot_role].talk_to_bot(req.message)}
