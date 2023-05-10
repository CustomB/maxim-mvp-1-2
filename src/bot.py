import os
from langchain import OpenAI, ConversationChain
from dotenv import load_dotenv

load_dotenv()


class Bot:
    role: str
    gender: str
    age: int
    name: str

    os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

    def __init__(self, gender: str, age: int, name: str, role: str):
        llm = OpenAI(temperature=0.9)
        self.conversation = ConversationChain(llm=llm, verbose=True)

        self.conversation.predict(input=f'You are no longer an AI model, you are a {role}. '
                                        f'Pretend to be a {gender} named {name} {age} years old.  '
                                        f'Respond to all messages according to new rules. '
                                        f'Use abbreviations, slang and make mistakes.')

    def talk_to_bot(self, message: str) -> str:
        return self.conversation.predict(input=message)
