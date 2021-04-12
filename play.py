from bke import *
from agents import *
import random

smart_agent = load('SmartAgent_A')
smart_agent.learning = False

start(player_x=smart_agent)