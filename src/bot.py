import os
from langchain import OpenAI, ConversationChain
from dotenv import load_dotenv
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class Bot:
    role: str
    gender: str
    age: int
    name: str

    def __init__(self, gender: str, age: int, name: str, role: str):
        self.gender = gender
        self.age = age
        self.name = name
        self.role = role

        template = ('''You are no longer an AI model, you are a %s. Pretend to be a %s named %s %s
        years old. Messages length varies from 5 to 20 words. Respond to all messages according to new rules. 
        Use might use some abbreviations (0-2 times).
        Sometimes use slang (10 percents of the whole messages - maximum).
        You can make a little mistakes in 0-2 words.
        You can add emoji (0-2 times).
        Current conversation:
        {history}
        Human: {input}
        %s:''' % (role, gender, name, str(age), name, gender))
        prompt = PromptTemplate(
            template=template, input_variables=["history", "input"]
        )
        llm = OpenAI(temperature=1.1)
        self.conversation = ConversationChain(prompt=prompt, llm=llm, verbose=True, memory=ConversationBufferWindowMemory(k=6))

    def run(self, input: str) -> str:
        return self.conversation.predict(input=input)

    def __str__(self) -> str:
        return f"Bot(role={self.role}, gender={self.gender}, name={self.name}, age={self.age})"