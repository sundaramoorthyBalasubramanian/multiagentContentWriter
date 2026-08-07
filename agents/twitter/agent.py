from langchain.messages import SystemMessage, HumanMessage
from agents.twitter.prompt import twitter_system_prompt
from shared.tools import seo_blog_llm

def x_agent_node(state):
    """Planner agent with its own message history"""

    # Use planner-specific messages
    x_msgs = state.get("x_messages", [])

    messages = [SystemMessage(content=twitter_system_prompt)] + x_msgs

    # If this is first call, add the user query
    if not x_msgs:
        messages.append(HumanMessage(content=state.get("user_query", "")))

    response = seo_blog_llm.invoke(messages)

    return {
        "x_messages": [response],
        "agent_results": [{
            "agent": "x_agent",
            "focus": "twitter content creation",
            "result": response.content
        }] if not response.tool_calls else []
    }