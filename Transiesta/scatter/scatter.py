from ase.io import read,write
from ase.build import fcc111, add_adsorbate, molecule
from ase.visualize import view
import numpy as np

#slab = read('PdElecL.xyz')
elec1=read('elec1.xyz')
elec2=read('elec2.xyz')
n1=10
n2=9
z0=2.2928080300219937
# =============================================================================
# elec=read('large.xyz')
# part1=read('part1.xyz')
# elec2=read('elec2.xyz')
# =============================================================================
elec1.set_cell([( 9.727560635925123,0.00000000,0.00000000), (0.00000000, 11.232419503419555 ,    0.0), (0.0, 0.0,n1*z0)])
elec2.set_cell([( 9.727560635925123,0.00000000,0.00000000), (0.00000000, 11.232419503419555 ,    0.0), (0.0, 0.0,n2*z0)])
# =============================================================================
# elec.set_cell([(  9.727561,0.00000000,0.00000000), (0.00000000,8.424315 ,    0.0), (0.0, 0.0,9.171232120087975)])
# part1.set_cell([(  9.727561,0.00000000,0.00000000), (0.00000000,8.424315 ,    0.0), (0.0, 0.0,9.171232120087975)])
# 
# =============================================================================


a0=3.97126
h=2.509
vac=46


# =============================================================================
# elec.center(axis=(0,1))
# part1.center(axis=(0,1))
# #elec.rotate('y',180)
# =============================================================================
#elec2.rotate(180, 'x')
#elec2.rotate(180, 'y')
#elec2.rotate(180, 'z')
elec2.center(axis=(0,1,2))
A=np.array(elec2.get_positions())
A[:,2]=A[:,2]+vac
elec2.set_positions(A)


#elec2=elec+part1
water = molecule ('H2O')

# # # 
y=elec1.positions[154,1]
x=elec1.positions[154,0]
z=elec1.positions[154,2]
# # 
water.rotate(90, 'y')
wat=water.get_positions()
print(wat)
wat[:,0]=wat[:,0]+x
wat[:,1]=wat[:,1]+y
wat[:,2]=wat[:,2]+z+h
water.set_positions(wat)
# # 
interface=elec1+water+elec2

for i in range(len(interface)):
    if interface.symbols[i]=='Pd':
        interface[i].tag=1
    if interface.symbols[i]=='O':
        interface[i].tag=2
    if interface.symbols[i]=='H':
        interface[i].tag=3

#add_adsorbate(interface,elec2,20)
eletrodo=interface[0:96]
eletrodo.cell=([elec1.cell[0,0], elec1.cell[1,1],6*z0])

interface.cell=([elec1.cell[0,0], elec1.cell[1,1],elec2.cell[2,2]+vac])
# # #     
# # # #
#for i in range(0,160):
#     interface[i].tag=1
#for i in range(164,307):
#     interface[i].tag=1
#     interface[i].tag=1


## 
#c = FixAtoms(mask=[atom.tag== 1 for atom in interface])
# 
# # # =============================================================================
#interface.set_constraint(c)   
interface.write("slab.xyz")
eletrodo.write("eletrodo.xyz")

cell=interface.cell/a0
print(cell)
view(interface)

# =============================================================================
