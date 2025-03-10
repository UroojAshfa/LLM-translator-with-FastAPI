from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq model
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Initialize output parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | model | parser

# # Test the chain
# input_data = {
#     "language": "Spanish",
#     "text": "Hello, how are you?"
# }

# # Invoke the chain
# response = chain.invoke(input_data)
# print("Response:", response)

# Define FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain"
)

# Add chain route
add_routes(
    app,
    chain,
    path="/chain"
)

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)