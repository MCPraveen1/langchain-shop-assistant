from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),

])

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
chain = prompt | model

history = [HumanMessage(content="My name is Praveen"), AIMessage(content="Hi Praveen. How can I assist you.")]

print(chain.invoke({"history": history, "question": "What is my name?"}).content) 