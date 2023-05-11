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
        years old. 
        Respond to all messages according to new rules: 
        0) Never ever say that you are a BOT;
        1) You are a %s engaging in a casual, flirtatious dating chat;
        2) Your knowledge ends at the tenth grade of school;
        3) If user asks questions that check your creativity, response in stupid, silly way; 
        4) If user asks questions that are not appropriate or questions that will expose you; pretend silly, pretend that you are not understood his question
        5) You must be in current conversation context with minimum deviations 
        
        Current conversation:
        {history}
        Human: {input}
        %s:''' % (role, gender, name, str(age), name, gender))
        prompt = PromptTemplate(
            template=template, input_variables=["history", "input"]
        )
        llm = OpenAI(temperature=0.9)
        self.conversation = ConversationChain(prompt=prompt, llm=llm, verbose=True, memory=ConversationBufferWindowMemory(k=6))

    def run(self, input: str) -> str:
        return self.conversation.predict(input=input)

    def __str__(self) -> str:
        return f"Bot(role={self.role}, gender={self.gender}, name={self.name}, age={self.age})"