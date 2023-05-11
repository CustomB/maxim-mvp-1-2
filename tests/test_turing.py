from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
import os

from src.logger import logging
from src.bot import Bot

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class TuringBot:
    def __init__(self) -> None:
        llm = ChatOpenAI(temperature=0.9)
        DEFAULT_TEMPLATE = """Your goal is to understand whether the other person in chat is a bot.
        You can ask tricky questions.
        You pretend to be a human.
        If you know that it is a bot then write "IT IS A BOT" and why do you think so.

        Current conversation:
        {history}
        Human: {input}
        AI:"""
        PROMPT = PromptTemplate(input_variables=["history", "input"], template=DEFAULT_TEMPLATE)

        self._bot = ConversationChain(
            llm=llm, 
            verbose=False, 
            prompt=PROMPT,
            memory=ConversationBufferMemory()
        )

    def answer(self, input: str) -> str:
        return self._bot.run(input=input)


def test_turing(bot: Bot, n_messages: int = 10) -> None:
    turing_bot = TuringBot()

    has_detected = False
    test_bot_answer = bot.answer("hi")
    logging.info(f"Started testing bot {str(bot)}\nNumbers of messages: {n_messages}")
    for counter in range(n_messages):

        turing_bot_answer = turing_bot.answer(input=test_bot_answer)
        logging.info(f"TURING BOT: {turing_bot_answer}")

        if "IT IS A BOT" in turing_bot_answer:
            logging.info(f"BOT DETECTED ERROR MESSAGE #{counter}:\n\n Explanation:\n{turing_bot_answer}\n")
            has_detected = True
            break
        
        test_bot_answer = bot.answer(input=turing_bot_answer)
        logging.info(f"BOT: {test_bot_answer}")
    
    if not has_detected:
        logging.info("BOT NOT DETECTED: success!")


if __name__ == "__main__":
    girlBot = Bot(gender="Female", age=21, name="Caitlyn", role="regular girl")


    for _ in range(10):
        test_turing(girlBot)