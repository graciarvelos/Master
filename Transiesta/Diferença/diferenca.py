import numpy as np
import matplotlib.pyplot as plt
from ase.io import read,write
from ase.visualize import view

coor_in=read("inicial.xyz")
coor_out=read("final.xyz")
rel=read("ts_pd_scatt-cut.xyz")
new=np.genfromtxt("ts_pd_scatt-cut.xyz",skip_header=1,usecols=(1,2,3))# A partir do átomo Pd 176-207 inicia a segunda camada abaixo da molécula de água
new2=np.zeros_like(new)
# =============================================================================
# for i in range(len(inicial)):
#     r[i]=((final[i,0]-inicial[i,0])**2+(final[i,1]-inicial[i,1])**2+(final[i,2]-inicial[i,2])**2)**0.5
# =============================================================================
#coor_in.center(axis=(0,1,2))
coor_in.rotate(270,'z',rotate_cell=True)
#coor_in.center(axis=(0,1,2))

# =============================================================================
# coor_in.rotate(180,'x')
# coor_in.rotate(180,'y')
# =============================================================================
#coor_out.center(axis=(0,1,2))
coor_out.rotate(270,'z',rotate_cell=True)
#coor_out.center(axis=(0,1,2))


# =============================================================================
# coor_out.rotate(180,'x')
# coor_out.rotate(180,'y')
# 
# =============================================================================
inicial=coor_in.get_positions()
final=coor_out.get_positions()

dif=final-inicial
## 32:63
new2[0:176]=new[0:176]
new2[208:211]=new[208:211]
new2[160:208,0]=new[160:208,0]+(dif[16:64,0])
new2[160:208,1]=new[160:208,1]+(dif[16:64,1])
new2[160:208,2]=new[160:208,2]+(dif[16:64,2])

#ALinhando a molécula de água
coor_out2=read("final.xyz")
coor_out2.center(axis=(0,1,2))
coor_out2.rotate(270,'z')
coor_out2.cell=[(9.727560635925123,0.00000000000,0.0000000000000 ),(0.000000000,11.232419503419555,0.0000000000),( 0.0000000000000,0.000000000000000,20.635272270197945)]
coor_out2.center(axis=(0,1,2))

#coor_out2.center(axis=(0,1,2))
final2=coor_out2.get_positions()

new2[208:211,0]=final2[64:67,0]
new2[208:211,1]=final2[64:67,1]
new2[208:211,2]=new2[208:211,2]+(-2.715+3.002)+dif[-3,2]-(2.566-2.509)
new[209,2]=new[209,2]+dif[-2,2]
new[210,2]=new[210,2]+dif[-1,2]


rel.set_positions(new2)
rel.cell=[(9.727560635925123,0.00000000000,0.0000000000000 ),(0.000000000,11.232419503419555,0.0000000000),( 0.0000000000000,0.000000000000000,54.80650439028592-7.179)]
rel.write("one-electrode.xyz")
view(rel)
