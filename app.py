import os
from langchain_groq import Chatgroq
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="Gemma2-9b-It", GROQ_API_KEY=GROQ_API_KEY)

messages=[
    SystemMessage(content="Translate the following from English to French: "),
    HumanMessage(content="Hello, how are you?")
]

result = model.invoke(messages)

#extract only the required content from AI Message
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
parser.invoke(result)



#Prompt Template
from langchain_core.prompts import ChatPromptTemplate

generic_template = "Translate the following into {language}"

prompt = ChatPromptTemplate.from_messages(
    [("system",generic_template),("user","text")]
)
result = prompt.invoke({"language": "French", "text": "Hello"})
result.to_messages()

#Using LCEL Chain the components. LCEL allows us to chain components together
chain = prompt|model|parser
chain.invoke({"language":"French","text":"Hello"})