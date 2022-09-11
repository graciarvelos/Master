a0= 3.97126
vacsize=a0
Sx=1
Sy=2
Sz=3
Ele='Pd'


########################################################################################
#Do NOT edit after this point!

#Import ase functions:
from ase.build import fcc111
from ase.visualize import view
import numpy as np

halfvac=vacsize/2.
Slab=fcc111(Ele,size=(Sx,Sy,Sz),a=a0,vacuum=0,orthogonal=True,periodic=False)
c=(Slab.cell[2,2]/(Sz-1))*Sz
#c= 1.66*a0
Slab.cell=[Slab.cell[0],Slab.cell[1],(0,0,c)]
Slab.rotate('z',270)
Slab.cell = [Slab.cell[1, 1], Slab.cell[0, 0], Slab.cell[2,2]]
Slab.center(axis=(0,1,2))
view(Slab)
Slab.write("slab.xyz")
