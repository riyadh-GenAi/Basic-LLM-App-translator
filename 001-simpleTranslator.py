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

_ = load_dotenv(find_dotenv())

groq_api_key = os.environ["GROQ_API_KEY"]

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

parser = StrOutputParser()

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

chain = prompt_template | llm | parser

app = FastAPI(
  title="Groq Translator API",
  version="1.0.0",
  description="FastAPI + LangChain + Groq LLM translation service",
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)