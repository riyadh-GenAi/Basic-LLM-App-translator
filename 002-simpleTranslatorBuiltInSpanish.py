import warnings
from langchain._api import LangChainDeprecationWarning

warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

import os

# Load environment variables
_ = load_dotenv(find_dotenv())

groq_api_key = os.environ["GROQ_API_KEY"]

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Output parser to extract the translation
parser = StrOutputParser()

# Template for system's prompt to translate text from Spanish to English
system_template = "Traduce lo siguiente al inglés:"

# Construct the prompt template for interaction
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Combine the prompt, LLM, and parser into a runnable chain
chain = prompt_template | llm | parser

# Initialize the FastAPI app with metadata
app = FastAPI(
  title="Groq Translator API",
  version="1.0.0",
  description="A simple API server using LangChain's Runnable interfaces that translates from Spanish to English",
)

# Add routes to the FastAPI app for the runnable chain
add_routes(
    app,
    chain,
    path="/chain",
)

# Run the server if the script is the main program
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
