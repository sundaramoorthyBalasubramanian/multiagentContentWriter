from langchain_core.messages import HumanMessage, SystemMessage
from shared.routerllm import router_llm

def router_node(state):
    """
    Router Node

    Responsibilities:
    1. Persist user input into messages.
    2. Classify the request into one of:
       - seo_blog_writer
       - x_blog_writer
       - general
    """

    user_input = state["user_input"]

    # Persist user input into conversation history
    messages = state.get("messages", [])
    messages.append(HumanMessage(content=user_input))

    router_prompt = """
You are a routing agent.

Classify the user's request into exactly ONE of the following categories:

seo_blog_writer
x_blog_writer
general

Rules:
- If the user wants an SEO article, blog, long-form content, website article, or optimized content, return:
seo_blog_writer

- If the user wants an X (Twitter) post, thread, tweet, social media content specifically for X, return:
x_blog_writer

- For everything else, return:
general

Return ONLY one word.
Do not explain.
"""

    response = router_llm.invoke([
        SystemMessage(content=router_prompt),
        HumanMessage(content=user_input),
    ])

    route = response.content.strip().lower()

    # Safety fallback
    if route not in {
        "seo_blog_writer",
        "x_blog_writer",
        "general",
    }:
        route = "general"

    return {
        "messages": messages,
        "route": route,
    }