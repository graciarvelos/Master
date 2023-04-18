#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:42:25 2022

@author: graci
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

df=pd.read_csv("angulo.csv")

pal = sns.color_palette('CMRmap')
#bias=['-5.0','-4.0','-2.5',"-1.5","0.0","3.0",""]

#pal = sns.color_palette([palette_tab10[4], palette_tab10[1], palette_tab10[2], palette_tab10[5]])
#sns.scatterplot(x=df["Bias"],marker='o',y=df["Angulo"])

fig = plt.figure()

ax = fig.add_subplot(111)
ax = sns.scatterplot(x=df["bias"],marker='o',y=df["angulo"],legend=False,color="dodgerblue",label="$\\alpha $")
ax2 = ax.twinx()
sns.scatterplot(x=df["bias"],marker='D',y=df["delta"],legend=False,label="$\Delta $",color="deeppink")


ax.set_xlabel('Bias Potential (eV)',fontsize=12)
ax.set_ylabel('$\\alpha$ ($^{\circ}$)',fontsize=12)
ax2.set_ylabel('$\Delta\;d_{O-Pd}$($\AA$)',fontsize=12)
#fig.suptitle("Inclinação ($\\alpha$) da Molécula de Água e \n Distância delta de acordo com o Potencial",fontsize=14)
fig.legend(loc=9, bbox_to_anchor=(.5,1), bbox_transform=ax.transAxes)
labels = [item.get_text() for item in ax.get_xticklabels()]
x1 = df["bias"]
ax.set_xticks(x1)
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax.set_ylim(-25,23)
ax.tick_params(axis="y",which='minor', direction='in',top=True, length=3)
ax.tick_params(axis="y",which='major', direction='in',top=True, length=3) 
ax2.tick_params(axis="y",which='minor', direction='in',top=True, length=3)
ax2.tick_params(axis="y",which='major', direction='in',top=True, length=3) 
ax.tick_params(axis="x",which='major', direction='in',top=True, length=3) 

#plt.title("Variação da inclinação em função do Campo Elétrico\n$H_2O/Pd(111)$")
ax.set_xticklabels(df["bias"])

plt.savefig("monomer.png", dpi=1500, transparent=False, bbox_inches = 'tight')
