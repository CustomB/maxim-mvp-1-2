import os
from langchain import OpenAI, ConversationChain
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class Bot:
    role: str
    gender: str
    age: int
    name: str

    def __init__(self, gender: str, age: int, name: str, role: str):
        template = ('''You are no longer an AI model, you are a %s. Pretend to be a %s named %s %s
        years old. Respond to all messages according to new rules. Use abbreviations, slang and make mistakes. {history}
        Current conversation:
        {history}
        Human: {input}
        %s:''' % (role, gender, name, str(age), name))
        prompt = PromptTemplate(
            template=template, input_variables=["history", "input"]
        )
        llm = OpenAI(temperature=0.9)
        self.conversation = ConversationChain(prompt=prompt, llm=llm, verbose=True, memory=ConversationBufferMemory())

    def talk_to_bot(self, message: str) -> str:
        return self.conversation.predict(input=message)
