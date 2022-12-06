#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:57:44 2022

@author: user
"""

import numpy as np
from ase.io import read
from ase.visualize import view
from ase.geometry.analysis import Analysis

sys=read("ts_au_layer.xyz")

au=[]
o=[]
h=[]
for i in range(len(sys)):
    if sys.symbols[i]=='Au':
        au.append(i)
    if sys.symbols[i]=='O':
        o.append(i)
    if sys.symbols[i]=='H':
        h.append(i)

ana = Analysis(sys)
ang=ana.get_angles('H',"O",'H')
val_ang=np.array(ana.get_values(ang))

dist=[]
down=[]
down_ang=[]
flat=[]
flat_ang=[]

for k in au[71:84]:
    for l in o: 
        d=sys.get_distance(k,l)
        if d<4.0:
            dist.append(d)

b=np.reshape(val_ang, (len(dist),1))

for i in range(len(dist)):
    if i%2==0:
# =============================================================================
#         print("\n Molécula Down %i"%i)
#         print(" Distância:%g"%(dist[i]))
#         print("Ângulo: %g"%(b[i]))
# =============================================================================
        flat.append(dist[i])
        down_ang.append(b[i])
    else:
# =============================================================================
#         print("\n Molécula Flat %i"%i)
#         print("Distância:%g"%(dist[i]))
#         print("Ângulo: %g"%(b[i]))
# =============================================================================
        down.append(dist[i])
        flat_ang.append(b[i])

print("Média Molécula Flat: %g "%(np.average(np.array(flat))))
print("Média Ângulo Flat: %g "%(np.average(np.array(flat_ang))))
print()
print("Média Molécula Down: %g "%(np.average(np.array(down))))
print("Média Ângulo Down: %g "%(np.average(np.array(down_ang))))
