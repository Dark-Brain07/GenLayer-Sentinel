# { "Depends": "py-genlayer:test" }
from genlayer import *

class OracleReputation(gl.Contract):
    """
    GenLayer Sentinel: Oracle Reputation System
    Tracks which validators/nodes provide the most accurate or timely data.
    """
    node_scores: dict[str, u256]

    def __init__(self):
        self.node_scores = {}

    @gl.public.write
    def report_accuracy(self, node_address: str, accurate: bool) -> str:
        """
        Updates the reputation score of a node based on report accuracy.
        """
        current_score = self.node_scores.get(node_address, u256(50)) # Start at 50
        
        if accurate:
            self.node_scores[node_address] = current_score + u256(1)
            return f"Accuracy verified. Score increased for {node_address}."
        else:
            if current_score > u256(0):
                self.node_scores[node_address] = current_score - u256(5) # Heavy penalty
            return f"Inaccuracy reported. Score heavily penalized for {node_address}."

    @gl.public.view
    def get_reputation(self, node_address: str) -> u256:
        return self.node_scores.get(node_address, u256(50))
