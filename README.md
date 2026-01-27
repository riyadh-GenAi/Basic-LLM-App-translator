# Groq Translator API

A lightweight translation API built with **LangChain**, **LangServe**, **FastAPI**, and **Groq LLMs**.  
This project exposes LangChain **Runnable chains** as REST endpoints using Groq instead of OpenAI.

---

## What This Project Does

This repository provides two translation services:

1. **Generic Translator** – Translate text into any target language.
2. **Spanish → English Translator** – Fixed translation from Spanish to English.

Both services run on **Groq’s `llama-3.1-8b-instant` model** and return clean text output only.

---

## Requirements

- Python 3.11
- Poetry
- Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here


## After starting the server, open the interactive playground in your browser:

## http://localhost:8000/chain/playground/
