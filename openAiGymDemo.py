#-------10--------20--------30--------40--------50--------60--------70-------79

'''
openAiGymDemo.py
Author: Miles Kovach
Created: 2020-10-09
Modified: 2020-10-18
EC601 Assignment big, script 0.1

A program to test openAIgym
based on "Getting Started With OpenAI Gym"
https://www.youtube.com/watch?v=8MC3y7ASoPs

And the playlist by the same author:
https://www.youtube.com/playlist?list=PLIfPjWrv526bMF8_vx9BqWjec-F-g-lQO
'''

debug_mode = [1, 2.1] # initializing an empty array for debugging purposes

# debug block 0 ~~~~~~~~~~~~~~~~~~~~~~~~

import gym
import agentTypes as aty

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

env_name = 'MountainCarContinuous-v0' # what game is being played
# including but not limited to:
# 'CartPole-v1', 'MountainCar-v0', 'MountainCarContinuous-v0'
env = gym.make(env_name)
actsLike = 'simple' # what kind of agent
# including but not limited to:
# 'random', 'simple'

if 1 in debug_mode:
  print("Observation space:\t", env.observation_space)
  print("Action space:\t", env.action_space)

currAgnt = aty.Agent(env, actsLike) # initializing an agent

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~

thisState = env.reset()
thisAction = currAgnt.get_action(thisState)
SRDI = env.step(thisAction)
# SRDI is a list containing four parameters [S, R, D, I]:
# (S)tate, a description of what the agent knows about its environment
# (R)eward, the reward the agent gets for taking the last step it took
# (D)one, a bool which is set when any of the game's termination conditions
# ...are met
# (I)nformation, any additional info the agent provides.

actionsTaken = 1

while not(SRDI[2]):
  SRDI = env.step(thisAction)
  actionsTaken += 1

  thisAction = currAgnt.get_action(SRDI[0])
  env.render()
  
  if 2.0 in debug_mode:
    print(SRDI)

if 2.1 in debug_mode:
  print("actionsTaken:\t", actionsTaken)

env.close()