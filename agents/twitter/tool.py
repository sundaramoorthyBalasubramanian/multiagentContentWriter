from shared.tools import x_tools
from langchain.messages import  ToolMessage

def x_tool_node(state):
    """Execute planner tools"""
    x_msgs = state.get("x_messages", [])

    # Check if x_messages exists and has content
    if not x_msgs:
        return {"x_messages": []}

    last_message = x_msgs[-1]

    # Check if last_message has tool_calls
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return {"x_messages": []}

    x_tools_by_name = {tool.name: tool for tool in x_tools}
    result = []

    for tool_call in last_message.tool_calls:
        tool = x_tools_by_name.get(tool_call["name"])
        if tool:
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))

    return {"x_messages": result}