#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:39:47 2022

@author: graci
"""


import numpy as np
import pandas as pd
import seaborn as sns
from scipy.signal import find_peaks
from ase.io import read
import os.path

##Lendo os arquivos
interface=read("ts_au_layer.xyz")
coord=interface.get_positions()

with open("ts_au_layer.Mode_49.AXSF", "r") as input:
    with open("temp.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if "ATOMS" not in line.strip("\n"):
                output.write(line)

# replace file with original name
os.replace('temp.txt', 'ts_au_layer.txt')


def search_passwords(file,file_out,word,n):
    file_out=open(file_out,"a+")
    file = open(file,  "r")
    search= word
    file_out.write("###Frequência %s" % (word))   
    counter = n
    found = False
    for line in file:
        if search in line:  
           found = True
        if found:
            if counter > 0: 
                counter -= 1
                file_out.write(line)
                #print(line)
            if counter == 0:
                break
    
def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

# =============================================================================
# file_out=open("freq_out.txt","w")
# for i in range(1000):
#     search_passwords("ts_au_layer.Mode_49.AXSF","freq_out.txt","ATOMS    %i"%i,25)
#     search_str("ts_au_layer.vectors.txt","%5.6f"%i)
# =============================================================================
    
eigen=np.genfromtxt("ts_au_layer.txt",skip_header=2)

data = open("mode.AXSF", "w")
for j in range(0,len(eigen),24):
    eig=eigen[j:j+24]
    i=-1
    data.write("ATOMS    %i\n"%(j/24+1))
    for k in range(0,84):
        data.write("79\t%12.8f%12.8f%12.8f\n" % (coord[k][0], coord[k][1], coord[k][2]))
    for k in range(84,108):
        i=i+1
        if i<24:
            data.write("%i\t%12.8f%12.8f%12.8f\n" % (eig[i][0],eig[i][1],eig[i][2],eig[i][3]))
    for k in range(108,len(coord)):
        data.write("79\t%12.8f%12.8f%12.8f\n" % (coord[k][0], coord[k][1], coord[k][2]))
data.close()


# =============================================================================
# for j in max_x: #Função utilizada para encontrar os números do eixo x no espalhamento mais próximos aos do eixo x do eletrodo
#     s,k=find_nearest(bias.values, value=j)
#     freq.append(s) 
#    # ind_s.append(k) #índice dos valores de x
# 
# print("\nValores picos:",max_x)
# print("\nFrequências mais próximas",freq)
# 
# 
# df=pd.read_csv("h_down_au.csv",usecols=(0,1,2,3,4))
# 
# #Encontrando o valor das frequências mais próximo ao máximo 
# def find_nearest(array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return array[idx],idx
# 
# ## Dados do Seaborn. Plotando a distribuição de frequências
# bias=df['8']
# dt=bias[48:56]
# nulo=np.zeros(len(dt))
# bw=0.8
# p=sns.kdeplot(data=dt,color="dodgerblue",linewidth=2.5,linestyle='-',gridsize=1000,common_norm=False,bw_adjust=bw,cut=3,cbar=True,legend=True)
# sns.scatterplot(x=dt,marker='|',color="blue",y=nulo+0.0001)
# #Obtendo os dados x e y do plot
# line = p.lines[0]
# x, y = line.get_data()
# 
# #definindo os valores dos picos
# 
# indices = find_peaks(y)[0]
# max_x=x[indices]
# max_y=y[indices]
# [p.axvline(_x, linewidth=1, color='red',linestyle='-',alpha=1.0) for _x in max_x]
# 
# 
# #Lista que vai receber as frequências máximas exatas
# freq=[]
# 
# col=open("Freq-Bias%s"%(bias.name),'w')
# col.write("Frequências - Bias%s (1/cm):"%(bias.name))
# for i in freq:
#     col.write("\n%g"%(i))
# col.close()
# =============================================================================
