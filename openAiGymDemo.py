#-------10--------20--------30--------40--------50--------60--------70-------79

'''
openAiGymDemo.py
Author: Miles Kovach
Created: 2020-10-09
Modified: 2020-10-16
EC601 Assignment big, script 0.1

A program to test openAIgym
based on "Getting Started With OpenAI Gym"
https://www.youtube.com/watch?v=8MC3y7ASoPs
'''

debug_mode = [] # initializing an empty array for debugging purposes

# debug block 0 ~~~~~~~~~~~~~~~~~~~~~~~~

import gym
import agentTypes as aty

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

env_name = 'CartPole-v1'
env = gym.make(env_name)

randAgnt = aty.Agent(env, 'random') # initializing an agent

env.reset()

for q in range(200):
  action = randAgnt.get_action()
  env.step(action)
  env.render()
  
  if 1 in debug_mode:
    print(q)
    
env.close()