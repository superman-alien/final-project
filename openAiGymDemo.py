#-------10--------20--------30--------40--------50--------60--------70-------79

'''
openAiGymDemo.py
Author: Miles Kovach
Created: 2020-10-09
Modified: 2020-10-19
EC601 Assignment big, script 0.1

A program to test openAIgym
based on "Getting Started With OpenAI Gym"
https://www.youtube.com/watch?v=8MC3y7ASoPs

And the playlist by the same author:
https://www.youtube.com/playlist?list=PLIfPjWrv526bMF8_vx9BqWjec-F-g-lQO
'''

debug_mode = [1, 2.0, 2.1, 2.2] # initializing an empty array for debugging purposes

# debug block 0 ~~~~~~~~~~~~~~~~~~~~~~~~

import gym
import agentTypes as aty
import time
from os import system

def clrOut():
  system('cls')

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

env_name = 'FrozenLake-v0' # what game is being played
# including but not limited to:
# 'CartPole-v1', 'MountainCar-v0', 'MountainCarContinuous-v0','FrozenLake-v0'
env = gym.make(env_name)
actsLike = 'simple' # what kind of agent
# including but not limited to:
# 'random', 'simple'

if 1 in debug_mode:
  print("Observation space:\t", env.observation_space)
  print("Action space:\t", env.action_space)

currAgnt = aty.Qagent(env) # initializing an agent

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~

total_reward = 0

for ep in range(100):

  oldState = env.reset() # this will be a holder for the prior state
  thisAction = currAgnt.get_action(oldState)
  SRDI = env.step(thisAction)
  # SRDI is a list containing four parameters [S, R, D, I]:
  # (S)tate, a description of what the agent knows about its environment
  # (R)eward, the reward the agent gets for taking the last step it took
  # (D)one, a bool which is set when any of the game's termination conditions
  # ...are met
  # (I)nformation, any additional info the agent provides.

  actionsTaken = 1

  while True:
    currAgnt.train((oldState, thisAction, SRDI[0], SRDI[1], SRDI[2]))
    total_reward += SRDI[1]
    print(total_reward)

    if 2.0 in debug_mode:
      clrOut()

    env.render()
    
    if 2.1 in debug_mode:
      print(SRDI, '\n', currAgnt.q_table)


    if SRDI[2]:
      break

    oldState = SRDI[0]
    thisAction = currAgnt.get_action(oldState)
    SRDI = env.step(thisAction)
    actionsTaken += 1

  if 2.2 in debug_mode:
    print('ep:\t', ep, \
          '\nactionsTaken:\t', actionsTaken, \
          '\ntotalRwd:\t', total_reward, \
          '\nepsilon:\t', currAgnt.eps)
    time.sleep(1)

env.close()