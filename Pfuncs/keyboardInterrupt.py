# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:02:50 2020

@author: MKovach
"""

import time

for i in range(0,10):
    try:
        print(i)
        time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        print('interrupt success')
        break

print('o joy')