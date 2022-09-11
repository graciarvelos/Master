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


# =============================================================================
# filename='initial-watermetal'
# water_orientation=1
# Ele1='Pd'    # Metal 
# Ele2='O'
# Ele3='H'
# if water_orientation == 1:
#     water.rotate(0, 'z')      # does not change for H-down
#     water_orientation_name = 'H-Down'
# elif water_orientation == 2:
#     water.rotate(180, 'y')    # H-Up
#     water_orientation_name = 'H-Up'
# elif water_orientation == 3:
#     water.rotate(90, 'y')    #  Flat
#     water_orientation_name = 'Flat'
# else:
#     print ("Please, set value for the water_orientation correctly!")
#     exit(0);

# data = open("LOG-%s.dat" % filename, "w")
# 
# data.write("Metallic Element:  %s \n" %Ele1)
# data.write("Lattice parameter: %-10.4f\n" %a0) 
# data.write("Water orientation:  %s \n" %water_orientation_name)
# data.write("Output Files: (Units in Ang) \n\n")
# 
# data.write("--------- Number of Particles ---------\n")
# data.write("# metal: %d\n" % len(inter3))
# data.write("# water (H2O): %d\n" % len(water))
# data.write("Total: %i \n\n" %len(inter3))
# 
# data.write("------------------- Cell ----------------------\n")
# box=inter3.get_cell()
# data.write("%f  %f  %f  \n" %  (box[0][0], box[0][1], box[0][2] ) )
# data.write("%f  %f  %f  \n" %  (box[1][0], box[1][1], box[1][2] ) )
# data.write("%f  %f  %f  \n" %  (box[2][0], box[2][1], box[2][2] ) )
# 
# data.write("\n-------------- Reduced Cell ----------------\n\n")
# 
# data.write("LatticeConstant %f Ang\n" % a0)
# data.write("%block LatticeVectors\n")
# box=inter3.get_cell()/a0                             #reduced by a0
# data.write("%f  %f  %f  \n" %  (box[0][0], box[0][1], box[0][2] ) )
# data.write("%f  %f  %f  \n" %  (box[1][0], box[1][1], box[1][2] ) )
# data.write("%f  %f  %f  \n" %  (box[2][0], box[2][1], box[2][2] ) )
# data.write("%endblock LatticeVectors\n")
# 
# data.write("\n----- Atomic_Coordinates   &&   Atomic_Species -----\n")
# data.write("1: %s\n" % Ele1)
# data.write("2: %s\n" % Ele2)
# data.write("3: %s\n\n" % Ele3)
# 
# data.write("AtomicCoordinatesFormat Ang\n")
# data.write("%block AtomicCoordinatesAndAtomicSpecies\n")
# positions_inter3 = inter3.get_positions()
# for k in range(len(positions_inter3)):
#     data.write("%12.6f%12.6f%12.6f\t1\t%d\t%s\n" % (positions_inter3[k][0], positions_inter3[k][1], positions_inter3[k][2], (k+1), Ele1))
# 
# positions_water = water.get_positions()
# data.write("%12.6f%12.6f%12.6f\t2\t%d\t%s\n" % (positions_water[0][0], positions_water[0][1], positions_water[0][2], (len(positions_inter3)+1), Ele2))
# data.write("%12.6f%12.6f%12.6f\t3\t%d\t%s\n" % (positions_water[1][0], positions_water[1][1], positions_water[1][2], (len(positions_inter3)+2), Ele3))
# data.write("%12.6f%12.6f%12.6f\t3\t%d\t%s\n" % (positions_water[2][0], positions_water[2][1], positions_water[2][2], (len(positions_inter3)+3), Ele3))
# data.write("%endblock AtomicCoordinatesAndAtomicSpecies\n")
#     
# 
# 
# =============================================================================
