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

sys=read("./siesta_one/inicial.xyz")

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

print("Média Molécula Flat: %3.4f "%(np.average(np.array(flat))))
print("Média Ângulo Flat: %3.4f "%(np.average(np.array(flat_ang))))
print()
print("Média Molécula Down: %3.4f "%(np.average(np.array(down))))
print("Média Ângulo Down: %3.4f "%(np.average(np.array(down_ang))))
#view(sys)


##Inclinação
normal_z=[0,0,1]
dados=sys.get_positions()[84:108]
for i in range(0,len(dados),3):
    x = dados[i:i+3,0]
    y = dados[i:i+3,1]
    z = dados[i:i+3,2]
    rO=[]; rO = np.zeros(3)
    rO[0] = x[0]; rO[1] = y[0]; rO[2] = z[0];  
    rH1=[]; rH1 = np.zeros(3)
    rH1[0] = x[1]; rH1[1] = y[1]; rH1[2] = z[1];  
    rH2=[]; rH2 = np.zeros(3)
    rH2[0] = x[2]; rH2[1] = y[2]; rH2[2] = z[2]; 
    vetor1= rH1 - rO  # from O to H1
    vetor2= rH2 - rO  # from O to H2
    VetorSoma= vetor1+vetor2 # computing the sum vector 
    A = np.dot(VetorSoma,normal_z)
    B = np.sqrt(np.dot(VetorSoma,VetorSoma))
    C = np.sqrt(np.dot(normal_z,normal_z))
    cosalpha= A/(B*C)
    alpha=180.0*np.arccos(cosalpha)/np.pi
    if i%2==0:
        print("Molécula Down")
        print ("Angle between dipolo and normal_z: ", alpha) 
        print ("Alpha: ", 90-alpha) 
    else:
        print("Molécula Flat")
        print ("Angle between dipolo and normal_z: ", alpha) 
        print ("Alpha: ", 90-alpha) 

