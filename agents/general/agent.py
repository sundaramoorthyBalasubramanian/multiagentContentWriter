from langchain.messages import SystemMessage, HumanMessage
from agents.general.prompt import gen_system_prompt
from shared.tools import seo_blog_llm

def general_agent_node(state):
    """Planner agent with its own message history"""

    # Use planner-specific messages
    gen_msgs = state.get("gen_messages", [])

    messages = [SystemMessage(content=gen_system_prompt)] + gen_msgs

    # If this is first call, add the user query
    if not gen_msgs:
        messages.append(HumanMessage(content=state.get("user_query", "")))

    response = seo_blog_llm.invoke(messages)

    return {
        "gen_messages": [response],
        "agent_results": [{
            "agent": "gen_agent",
            "focus": "general assistance",
            "result": response.content
        }] if not response.tool_calls else []
    }