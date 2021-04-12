from bke import *
from agents import *
 
my_agent = load('SmartAgent_A')
my_agent.learning = False
 
validation_agent = RandomAgent()
 
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)