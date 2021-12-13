#!/usr/bin/env python
import yaml
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import math




def compute_obstacles(obs_type):
    """
    Given the vertices of the obstacle, here we compute a sequence of points all along the perimeter.
    reso: is the distance of these middle points along the perimeter
    obs_type: is the name of the yaml file we want to use as obstacles.
    """
    reso = 0.25
    dirname = '/params/'
    dirname = dirname + obs_type + ".yaml"
    stream = open(dirname)
    val = yaml.safe_load(stream)

    fin_ox = []
    fin_oy = []

    for rig in range(len(val['obstacles'])):
        for col in range(len(val['obstacles'][rig])-1):
            pre_x = val['obstacles'][rig][col][0]
            pre_y = val['obstacles'][rig][col][1]
            succ_x = val['obstacles'][rig][col+1][0]
            succ_y = val['obstacles'][rig][col+1][1]
            
            # add obstacles from vertices

            theta = math.atan2((succ_y-pre_y), (succ_x-pre_x))

            if abs(theta) < math.pi/4 or abs(theta) > 3*math.pi/4:
                lin_x = list(np.linspace(pre_x, succ_x, 1+math.ceil((succ_x - pre_x)/(reso*math.cos(theta)))))
                f = interpolate.interp1d([pre_x, succ_x], [pre_y, succ_y], kind="slinear")
                lin_y = list(f(lin_x))
            else:
                lin_y = list(np.linspace(pre_y, succ_y, 1+math.ceil(abs((succ_y - pre_y)/(reso*math.sin(theta))))))
                f = interpolate.interp1d([pre_y, succ_y], [pre_x, succ_x], kind="slinear")
                lin_x = list(f(lin_y))
            
            fin_ox += lin_x
            fin_oy += lin_y
        
        pre_x = succ_x
        pre_y = succ_y
        succ_x = val['obstacles'][rig][0][0]
        succ_y = val['obstacles'][rig][0][1]
        
        theta = math.atan2((succ_y-pre_y), (succ_x-pre_x))
            
        if abs(theta) < math.pi/4 or abs(theta) > 3*math.pi/4:   
            lin_x = list(np.linspace(pre_x, succ_x, 1+math.ceil((succ_x - pre_x)/(reso*math.cos(theta)))))
            f = interpolate.interp1d([pre_x, succ_x], [pre_y, succ_y], kind="slinear")
            lin_y = list(f(lin_x))
        else:
            lin_y = list(np.linspace(pre_y, succ_y, 1+math.ceil(abs((succ_y - pre_y)/(reso*math.sin(theta))))))
            f = interpolate.interp1d([pre_y, succ_y], [pre_x, succ_x], kind="slinear")
            lin_x = list(f(lin_y))

        fin_ox += lin_x
        fin_oy += lin_y

    assert len(fin_ox) == len(fin_oy)

    return fin_ox, fin_oy

""" To test the function uncomment the following"""
# x,y = compute_obstacles("obstacles")
# print(len(x), len(y))

# plt.figure("Check")
# plt.plot(x, y, 'b.')
# plt.show()

"""For more evaluation tests look obstacle_prova.py in branch team1_gianmarco"""

