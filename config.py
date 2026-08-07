from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("OPENAI API Key Found:", OPENAI_API_KEY is not None)

if not OPENAI_API_KEY:
    print("OPENAI API Key Found:", OPENAI_API_KEY is  None)
    raise ValueError("OPENAI_API_KEY not found")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
print("TAVILY API Key Found:", TAVILY_API_KEY is not None)

if not TAVILY_API_KEY:
    print("TAVILY API Key Found:", TAVILY_API_KEY is  None)
    raise ValueError("TAVILY_API_KEY not found")

AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
print("AVIATIONSTACK API Key Found:", AVIATIONSTACK_API_KEY is not None)

if not AVIATIONSTACK_API_KEY:
    print("AVIATIONSTACK API Key Found:", AVIATIONSTACK_API_KEY is  None)
    raise ValueError("AVIATIONSTACK_API_KEY not found")

