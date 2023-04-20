#!/usr/bin/python3.8
#-*- coding: utf-8 -*-

#from ase.build import molecule
#atoms = molecule('H2O')
#print (atoms.get_positions())

import numpy as np
from math import *
from ase.io import read,write
from ase.visualize import view

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading a file: water.xyz
# 
#  File needs to have the water coordinates: O, H1 and H2
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
dados=np.genfromtxt("./positivo/10.0/ts_au_monomer.xyz",skip_header=1,skip_footer=72)


x = dados[-3::,1]
y = dados[-3::,2]
z = dados[-3::,3]

#----------------- Oxigen ---------------#
rO=[]; rO = np.zeros(3)
rO[0] = x[0]; rO[1] = y[0]; rO[2] = z[0];  
#print(rO)

#----------------- H1 ---------------#
rH1=[]; rH1 = np.zeros(3)
rH1[0] = x[1]; rH1[1] = y[1]; rH1[2] = z[1];  
#print(rH1)

#----------------- H2 ---------------#
rH2=[]; rH2 = np.zeros(3)
rH2[0] = x[2]; rH2[1] = y[2]; rH2[2] = z[2]; 
#print(rH2)

#----------------- Defining vectors ---------------#
vetor1= rH1 - rO  # from O to H1
vetor2= rH2 - rO  # from O to H2
VetorSoma= vetor1+vetor2 # computing the sum vector 
#VetorSoma= rO # computing the sum vector 


print ('------------------------------------------------------------------')
print ('                        WATER                                     ')
print ("O-H:", np.sqrt(np.dot(vetor1,vetor1)))
print ("O-H:", np.sqrt(np.dot(vetor2,vetor2)))

#-----------------  Dot product and computing the angle between two H---------------#
A = np.dot(vetor1,vetor2)
B = np.sqrt(np.dot(vetor1,vetor1))
C = np.sqrt(np.dot(vetor2,vetor2))
costheta= A/(B*C)
theta=180.0*np.arccos(costheta)/np.pi
print ("Angle between H: ", theta) 
print ('------------------------------------------------------------------')

print ('                        WATER/SURFACE                             ')

#-----------------  To verify if the normal is perpendicular to the water plane ---------------#
normal_z=[0,0,1]
A = np.dot(VetorSoma,normal_z)
B = np.sqrt(np.dot(VetorSoma,VetorSoma))
C = np.sqrt(np.dot(normal_z,normal_z))
cosalpha= A/(B*C)
alpha=180.0*np.arccos(cosalpha)/np.pi
print ("Angle between dipolo and normal_z: ", alpha) 
print ("Alpha: ", alpha-90) 
print ('------------------------------------------------------------------')

print ('               LATERAL AND VERTICAL DISPLACEMENT                      ')

Au=dados[-10,1:4]
O=dados[-3,1:4]
#O_inicial=inicial[-3,1:4]
vertical=Au[2]-O[2]
delta=((Au[0]-O[0])**2+(Au[1]-O[1])**2)**0.5
h=(vertical**2+delta**2)**0.5


print ("The Lateral displacement is: ",delta)
print ("Vertical position: ",h) 
print ('------------------------------------------------------------------')

