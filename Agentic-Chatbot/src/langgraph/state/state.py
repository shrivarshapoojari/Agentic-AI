from typing_extensions import TypedDict,List
from  langgraph.graph import add_message
from typing import Annotated


class State(TypedDict):
    """
    Represents the structure of state used in the graph.
    """
    message:Annotated[list,add_message]
    