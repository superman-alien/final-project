#-------10--------20--------30--------40--------50--------60--------70-------79

'''
agentTypes.py
Author: Miles Kovach
Created: 2020-10-16
Modified: 2020-10-18
CLASS Assignment big, script 0.1

Definition for class agent, and implementation of a few types of agents.
To be used in a situation where openAi Gym is used, with 
import gym

based on "Getting Started With OpenAI Gym"
https://www.youtube.com/watch?v=8MC3y7ASoPs

And the playlist by the same author:
https://www.youtube.com/playlist?list=PLIfPjWrv526bMF8_vx9BqWjec-F-g-lQO
'''
debug_mode = [2] # initializing an empty array for debugging purposes

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

import gym
import random
import numpy as np

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~

class Agent():
  def __init__(self, enviro, strat): 
  # inputs: environment
  #         strategy to use for picking an action.  defaults to "random".
    self.is_discrete = type(enviro.action_space) == gym.spaces.discrete.Discrete
    if self.is_discrete:
      self.action_size = enviro.action_space.n
    else:
      self.action_low = enviro.action_space.low
      self.action_high = enviro.action_space.high
      self.action_shape = enviro.action_space.shape
      
    self.behav = strat

    if 2 in debug_mode:
      if self.is_discrete:
        print("Action Size:\t", self.action_size)
      else:
        print("Action range:\t", self.action_low, self.action_high)
      print(strat)
    
  def get_action(self, state): 
  # inputs: state of the environment; a list  
    if self.behav == 'simple':
      if self.is_discrete:  
        if state[2] < 0: # if pole angle is tilting left, for example
          #CHANGE_ME: not all games have the same state space!!!
          action = 0 # this corresponds to a left motion in the action table
        else:
          action = 1
      else:
        action = [0] # CHANGE THIS

    else: # strat defaults to random
      if self.is_discrete:  
        action = random.choice(range(self.action_size))
      else:
        action = np.random.uniform(self.action_low, \
                                   self.action_high, \
                                   self.action_shape)
    return action