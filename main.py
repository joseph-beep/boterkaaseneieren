import random
from bke import EvaluationAgent, start

class RandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

random_agent = RandomAgent()
start(player_o=random_agent)