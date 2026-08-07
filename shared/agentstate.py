from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages

class AgentState(TypedDict):
    """Shared state for the agentic workflow."""
    user_input: str
    route: str
    output: str
    # The add_messages reducer appends new messages to the list automatically
    seo_messages: Annotated[list[AnyMessage], add_messages]
    x_messages: Annotated[list[AnyMessage], add_messages]
    gen_messages: Annotated[list[AnyMessage], add_messages]