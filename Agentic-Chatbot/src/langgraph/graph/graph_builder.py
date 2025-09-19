
from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
   
    def basic_chatbot(self):
        """"
        basic chatbot graph
        """
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase):
        """
        Sets up the graph based on the use case and returns the compiled graph.
        """
        if usecase == "basic_chatbot":
            self.basic_chatbot()
            return self.graph_builder.compile()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")

        