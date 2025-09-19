import src.langgraph.graph.graph_builder
from langgraph.graph import StateGraph
from src.langgraph.state.state import State, START, END
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
   
    def basic_chatbot(self):
        """"
        basic chatbot graph
        """
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

        