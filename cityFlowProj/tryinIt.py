import sys
sys.path.append('/home/ece-student/Desktop/Shared/CityFlow/tools/generator/')

if 0:
  import generate_grid_scenario as ggs

import cityflow

eng = cityflow.Engine('/media/sf_Shared_VM/cityFlowProj/attempt20201102/config.json')

for i in range(100):
  eng.next_step()
