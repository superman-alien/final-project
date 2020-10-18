#-------10--------20--------30--------40--------50--------60--------70-------79

'''
openAiGymDemo.py
Author: Miles Kovach
Created: 2020-10-09
Modified: 2020-10-17
EC601 Assignment big, script 0.1

A program to test openAIgym
based on "Getting Started With OpenAI Gym"
https://www.youtube.com/watch?v=8MC3y7ASoPs
'''

debug_mode = [1] # initializing an empty array for debugging purposes

# debug block 0 ~~~~~~~~~~~~~~~~~~~~~~~~

import gym
import agentTypes as aty

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

env_name = 'CartPole-v1'
env = gym.make(env_name)
actsLike = 'simple'

currAgnt = aty.Agent(env) # initializing an agent

thisState = env.reset()
thisAction = currAgnt.get_action(thisState, actsLike)

for q in range(200):
  SRDI = env.step(thisAction)
  # SRDI is a list containing four parameters [S, R, D, I]:
  # (S)tate, a description of what the agent knows about its environment
  # (R)eward, the reward the agent gets for taking the last step it took
  # (D)one, a bool which is set when any of the game's termination conditions
  # ...are met
  # (I)nformation, any additional info the agent provides.

  if SRDI[2] == 1: # breaks the loop if done flag is set
    print('done')
    break

  thisAction = currAgnt.get_action(SRDI[0], actsLike)
  env.render()
  
  if 1 in debug_mode:
    print(q, SRDI)
    
env.close()