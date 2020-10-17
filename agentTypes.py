#-------10--------20--------30--------40--------50--------60--------70-------79

'''
agentTypes.py
Author: Miles Kovach
Created: 2020-10-16
Modified: 2020-10-16
CLASS Assignment big, script 0.1

Definition for class agent, and implementation of a few types of agents.
To be used in a situation where openAi Gym is used, with 
import gym
'''

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

import random

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~

class Agent():
  def __init__(self, enviro, strat): # inputs: environment
    self.action_size = enviro.action_space.n
    print("Action Size:\t", self.action_size)
    
  def get_action(self):
    if strat == 'random':
      action = random.choice(range(self.action_size))
    return action