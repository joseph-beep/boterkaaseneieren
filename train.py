from bke import *
from agents import *
import random

random.seed(1)

smart_agent = SmartAgent(alpha=1, epsilon=0.1)
random_agent = RandomAgent()

train_and_plot(
    agent=smart_agent,
    validation_agent=random_agent,
    iterations=100,
    trainings=100,
    validations=1000)

save(smart_agent, 'SmartAgent_A')