from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END, add_messages

# 1. Define our State with the add_messages reducer
class AgentState(TypedDict):
    user_input: str
    route: str
    output: str
    messages: Annotated[list[AnyMessage], add_messages]

# 2. Node 1: Chatbot Node
def chatbot_node(state: AgentState):
    print("--- CHATBOT NODE RUNNING ---")
    print(f"Current messages in state: {len(state['messages'])}")
    print(f"Current messages in state: {state['messages']}")
    
    # Simulating an LLM response message
    ai_reply = AIMessage(content="Here is a drafted marketing email.")
    
    # We only return the NEW message. The reducer appends it automatically.
    return {"messages": [ai_reply]}

# 3. Node 2: Reviewer Node
def reviewer_node(state: AgentState):
    print("\n--- REVIEWER NODE RUNNING ---")
    print(f"Current messages in state: {len(state['messages'])}")
    print(f"Current messages in state: {state['messages']}")
    
    # Simulating a system validation message
    review_note = AIMessage(content="Review complete: The email looks good!")
    
    # We only return the NEW message. The reducer appends it too!
    return {"messages": [review_note]}

# 4. Build the Graph
builder = StateGraph(AgentState)
builder.add_node("chatbot", chatbot_node)
builder.add_node("reviewer", reviewer_node)

# Flow: START -> Chatbot -> Reviewer -> END
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", "reviewer")
builder.add_edge("reviewer", END)

graph = builder.compile()

# 5. Run the Graph with an initial HumanMessage
initial_input = {
    "user_input": "Write an email",
    "route": "continue",
    "output": "",
    "messages": [HumanMessage(content="Can you write a promo email?")]
}

final_state = graph.invoke(initial_input)

# 6. Print final message history length and contents
print("\n--- FINAL GRAPH STATE ---")
print(f"Total messages in history: {len(final_state['messages'])}")
for msg in final_state['messages']:
    print(f"- {type(msg).__name__}: {msg.content}")
