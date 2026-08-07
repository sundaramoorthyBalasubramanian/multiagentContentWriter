from langchain_openai import ChatOpenAI
import config

router_llm = ChatOpenAI(
    model="gpt-5",
    temperature=0
)