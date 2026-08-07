from langgraph.graph import StateGraph, END
from shared.agentstate import AgentState

# ------------------------------------
# Router Function
# ------------------------------------

def router(state):
    """Returns one of:
    - seo_blog_writer
    - x_blog_writer
    - general
    """
    return state["route"]


# ------------------------------------
# Continue Functions
# ------------------------------------

def should_continue_seo(state):
    """
    Continue calling tools if the LLM requested them.
    """

    last_message = state["seo_messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return END


def should_continue_x(state):
    """
    Continue calling tools if the LLM requested them.
    """

    last_message = state["x_messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return END

from agents.seo.agent import seo_agent_node
from agents.seo.tool import seo_tool_node
from agents.twitter.agent import x_agent_node
from agents.twitter.tool import x_tool_node
from agents.general.agent import general_agent_node
from agents.router.agent import router_node

# ------------------------------------
# Build Graph
# ------------------------------------

builder = StateGraph(AgentState)

builder.add_node("router", router_node)

builder.add_node("seo_blog_writer", seo_agent_node)
builder.add_node("seo_tools", seo_tool_node)

builder.add_node("x_blog_writer", x_agent_node)
builder.add_node("x_tools", x_tool_node)

builder.add_node("general", general_agent_node)

# ------------------------------------
# Entry Point
# ------------------------------------

builder.set_entry_point("router")

# ------------------------------------
# Router Edges
# ------------------------------------

builder.add_conditional_edges(
    "router",
    router,
    {
        "seo_blog_writer": "seo_blog_writer",
        "x_blog_writer": "x_blog_writer",
        "general": "general",
    },
)

# ------------------------------------
# SEO Tool Loop
# ------------------------------------

builder.add_conditional_edges(
    "seo_blog_writer",
    should_continue_seo,
    {
        "tools": "seo_tools",
        END: END,
    },
)

builder.add_edge(
    "seo_tools",
    "seo_blog_writer",
)

# ------------------------------------
# X Tool Loop
# ------------------------------------

builder.add_conditional_edges(
    "x_blog_writer",
    should_continue_x,
    {
        "tools": "x_tools",
        END: END,
    },
)

builder.add_edge(
    "x_tools",
    "x_blog_writer",
)

# ------------------------------------
# General Chat
# ------------------------------------

builder.add_edge(
    "general",
    END,
)

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
# ------------------------------------
# Compile
# ------------------------------------

graph = builder.compile(
    checkpointer=memory
)

config = {
    "configurable": {
        "thread_id": "user_001"
    }
}

response = graph.invoke(
    {
        "user_input": "Write an SEO blog about Agentic AI."
    },
    config=config
)
print(response)