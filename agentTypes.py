#-------10--------20--------30--------40--------50--------60--------70-------79

'''
agentTypes.py
Author: Miles Kovach
Created: 2020-10-16
Modified: 2020-10-19
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

class Qagent(Agent):
  def __init__(self, enviro, strat = 'Q',\
               discount_rate = 0.97,\
               learning_rate = 0.99):
    super().__init__(enviro, strat)
    self.state_size = enviro.observation_space.n
    
    self.eps = .3 # threshold for choosing a random vs policy action
    self.DR = discount_rate
    self.LR = learning_rate
    self.build_model()
    
  def build_model(self):
    self.q_table = 1e-4 * np.random.random([self.state_size, self.action_size])

  def get_action(self, state):
    q_state = self.q_table[state]
    action_greedy = np.argmax(q_state)
    action_random = super().get_action(state)
    action = action_random if random.random() < self.eps else action_greedy
    return action

  def train(self, experience):
    SANRD = experience
    # a list like this:
    # (S)tate
    # (A)ction
    # (N)ext state
    # (R)eward
    # (D)one

    q_next = self.q_table[SANRD[2]]
    if SANRD[4]:
      q_next = np.zeros([self.action_size]) 
    q_target = SANRD[3] + self.DR * np.max(q_next)
    # adjusting q-table propotionally to the difference between reward and max

    q_update = q_target - self.q_table[SANRD[0], SANRD[1]]
    self.q_table[SANRD[0], SANRD[1]] += self.LR * q_update

    if SANRD[4]:
      self.eps *= .99 # steering the algorithm towards determinism