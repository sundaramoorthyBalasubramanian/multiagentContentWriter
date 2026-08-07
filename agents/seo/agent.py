from langchain.messages import SystemMessage, HumanMessage
from agents.seo.prompt import seo_system_prompt
from shared.tools import seo_blog_llm

def seo_agent_node(state):
    """Planner agent with its own message history"""

    # Use planner-specific messages
    seo_msgs = state.get("seo_messages", [])

    messages = [SystemMessage(content=seo_system_prompt)] + seo_msgs

    # If this is first call, add the user query
    if not seo_msgs:
        messages.append(HumanMessage(content=state.get("user_query", "")))

    response = seo_blog_llm.invoke(messages)

    return {
        "seo_messages": [response],
        "agent_results": [{
            "agent": "seo_agent",
            "focus": "seo optimization",
            "result": response.content
        }] if not response.tool_calls else []
    }