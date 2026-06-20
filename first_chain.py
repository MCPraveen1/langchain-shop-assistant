from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms."
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke(
    {"topic": "Machine Learning"}
)

print(response)