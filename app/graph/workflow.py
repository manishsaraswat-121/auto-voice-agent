from langgraph.graph import StateGraph
from app.agents.conversation import ConversationAgent
from app.agents.knowledge import KnowledgeAgent
from app.agents.booking import BookingAgent

conv = ConversationAgent()
kb = KnowledgeAgent()
booker = BookingAgent()


def conversation_node(state):
    state["slots"] = conv.extract_slots(state["user_text"])
    return state


def knowledge_node(state):
    models = kb.get_models(state["slots"]["vehicle_type"])
    state["selected_model"] = models[0]["model"]
    return state


def booking_node(state):
    booking = booker.book(
        state["selected_model"],
        state["slots"]["date"],
        state["slots"]["time"]
    )
    state["booking"] = booking
    return state


graph = StateGraph(dict)
graph.add_node("conversation", conversation_node)
graph.add_node("knowledge", knowledge_node)
graph.add_node("booking", booking_node)

graph.set_entry_point("conversation")
graph.add_edge("conversation", "knowledge")
graph.add_edge("knowledge", "booking")

workflow = graph.compile()
