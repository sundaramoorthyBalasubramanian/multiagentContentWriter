from shared.tools import seo_tools
from langchain.messages import  ToolMessage

def seo_tool_node(state):
    """Execute planner tools"""
    seo_msgs = state.get("seo_messages", [])

    # Check if seo_messages exists and has content
    if not seo_msgs:
        return {"seo_messages": []}

    last_message = seo_msgs[-1]

    # Check if last_message has tool_calls
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return {"seo_messages": []}

    seo_tools_by_name = {tool.name: tool for tool in seo_tools}
    result = []

    for tool_call in last_message.tool_calls:
        tool = seo_tools_by_name.get(tool_call["name"])
        if tool:
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))

    return {"seo_messages": result}