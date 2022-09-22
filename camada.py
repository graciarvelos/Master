import numpy as np
from ase.lattice.hexagonal import *
from ase import Atoms
from ase.visualize import view
from ase.build import molecule
from ase.build import fcc111

Ele='Au'
a0=4.24 #parâmetro de rede
vac=20 #vácuo
h=3 #Distância da molécula flat
d2=0.35 #Distância da molécula up e down em relação à flat
option=1 # Escolha 1 para a camada H-Down, 2 para H-Up e 3 para H-Down/Up
Sx=3 #Tamanho da superfície metálica
Sy=4
Sz=7


#def layer(Ele,a0,vac,h,option):
metal=fcc111(Ele,size=(Sx,Sy,Sz),a=a0,vacuum=vac,orthogonal=True)
metal.rotate(270,"z") ##Rotacionando 
metal.cell=[metal.cell[1,1],metal.cell[0,0],metal.cell[2,2]]
metal.center(axis=(0,1,2))
#metal.rotate(180,"x",rotate_cell=True)
#metal.rotate(180,"y",rotate_cell=True)
#metal.center(axis=(0,1,2))
M=metal.get_positions() ## Pega as posições dos átomos que compõem o metal
zmax = metal.positions[:,2].max() 
Ele2='O'
Ele3='H'
A = metal.get_distance(0,1) #tomando a distância entre os átomos adjacentes no metal
R=A*3**0.5 #distância das moléculas de água
print(R)
c=1
if option==1 or option==2:
    a2=1
    a1=1
if option==3:
    a1=1
    a2=2
hexa=Graphene(symbol = 'O',latticeconstant={'a':R,'c':1},size=(a1,a2,1)) #Definindo a estrutura hexagonal da camada
water1=molecule('H2O') #flat
water1.rotate(90, 'y')
water1.rotate(205, 'z')
water2=molecule('H2O') 
water2.rotate(115, 'z')  #down
#water2.rotate(88, 'x') #down
water2.rotate(-45, 'y') #down
water3=molecule('H2O') 
water3.rotate(180, 'y') #up
water3.rotate(52, 'x') #up
water3.rotate(115, 'z') #up
a=np.array(hexa.get_positions()) ##Substituindo as posições da rede hexagonal pelas moléculas de água.
cel=np.array(hexa.get_cell())
b=np.array(water1.get_positions()) #flat
c=np.array(water2.get_positions()) #down
u=np.array(water3.get_positions()) #up
if option==1:##If option=1 the layer that's going be generate is flat/down-flat
    B=np.concatenate((b, c)) #vetor da molécula flat e down
    d=np.zeros((len(B),3))
    for i in range(0,3):
        d[i]=B[i]+a[0]
    for i in range(3,6):
        d[i]=B[i]+a[1]
        d[i,2]+=d2
    W=Atoms('2(OH2)',positions=d,cell=cel,pbc=[1,1,0])
    W2=W.repeat((4,4,1))
    filename='layer-down'
if option==2:##If option=2 the layer that's going be generate is up/up-flat
    B=np.concatenate((b, u))
    d=np.zeros((len(B),3))
    for i in range(0,3):
        d[i]=B[i]+a[0]
    for i in range(3,6):
        d[i]=B[i]+a[1]
        d[i,2]+=d2
    W=Atoms('2(OH2)',positions=d,cell=cel,pbc=[1,1,0])
    W2=W.repeat((4,4,1))
    filename='layer-up'
if option==3: ##If option=3 the layer that's going be generate is flat/down-flat/up-flat 
    B=np.concatenate((b,c,b,u))
    d=np.zeros((len(B),3))
    for i in range(0,3):
        d[i]=B[i]+a[0]
    for i in range(3,6):
        d[i]=B[i]+a[1]
        d[i,2]+=d2
    for i in range(6,9):
        d[i]=B[i]+a[2]
    for i in range(9,12):
        d[i]=B[i]+a[3]
        d[i,2]+=d2
    W=Atoms('4(OH2)',positions=d,cell=cel,pbc=[1,1,0])
    W2=W.repeat((4,2,1))
    filename='layer-up-down'
W2.rotate(270,"z",rotate_cell=True) ##Rotacionando 
W2.rotate('z',30,rotate_cell=True)
C=metal.get_cell()
W2.set_cell(C)
W2.center(axis=(0,1))
W2.positions[:,2] += zmax + h
nw=30 #Posições da matriz hexagonal e do átomo do metal que coincidirão
nO=74
deltax=metal.get_positions()[nO,0]-W2.get_positions()[nw,0]
deltay=metal.get_positions()[nO,1]-W2.get_positions()[nw,1]
W2.positions[:,1] += deltay
W2.positions[:,0] += deltax
#del[W2[0:9],W2[12:29],W2[42:57],W2[69:95]] 
layer = metal + W2
for i in range(len(layer)):
    if layer.positions[i,0]<0:
        layer[i].tag=3
    elif layer.positions[i,1]<0:
        layer[i].tag=3
    elif layer.positions[i,0]>metal.cell[0,0]:
        layer[i].tag=3   
    elif layer.positions[i,1]>metal.cell[1,1]:
        layer[i].tag=3 
    else:
        layer[i].tag=0
del layer[[atom.index for atom in layer if atom.tag==3]]

data = open("LOG-%s.dat" % filename, "w")
data.write("Metallic Element:  %s \n" %Ele)
data.write("FCC - 111:   (%i, %i, %i)\n" % (6, 6,4))
data.write("Lattice parameter: %-10.4f\n" %a0) 
data.write("Water orientation:  %s \n" %filename)
data.write("Output Files: (Units in Ang) \n\n")
data.write("--------- Number of Particles ---------\n")
data.write("# metal: %d\n" % len(metal))
data.write("# water (H2O): %d\n" % len(W2))
data.write("Total: %i \n\n" %len(layer))
data.write("------------------- Cell ----------------------\n")
box=layer.get_cell()
data.write("%f  %f  %f  \n" %  (box[0][0], box[0][1], box[0][2] ) )
data.write("%f  %f  %f  \n" %  (box[1][0], box[1][1], box[1][2] ) )
data.write("%f  %f  %f  \n" %  (box[2][0], box[2][1], box[2][2] ) )
data.write("\n-------------- Reduced Cell ----------------\n\n")
data.write("LatticeConstant %f Ang\n" % a0)
data.write("%block LatticeVectors\n")
box=layer.get_cell()/a0 #reduced by a0
data.write("%f  %f  %f  \n" %  (box[0][0], box[0][1], box[0][2] ) )
data.write("%f  %f  %f  \n" %  (box[1][0], box[1][1], box[1][2] ) )
data.write("%f  %f  %f  \n" %  (box[2][0], box[2][1], box[2][2] ) )
data.write("%endblock LatticeVectors\n")
data.write("\n----- Atomic_Coordinates   &&   Atomic_Species -----\n")
data.write("1: %s\n" % Ele)
data.write("2: O\n")
data.write("3: H\n\n")
data.write("AtomicCoordinatesFormat Ang\n")
data.write("%block AtomicCoordinatesAndAtomicSpecies\n")
ele=layer.get_chemical_symbols()
coord=layer.get_positions()
n=np.zeros(len(coord))
for k in range(len(coord)):
    if ele[k]==Ele:
        n[k]=1
    elif ele[k]=='O':
        n[k]=2
    elif ele[k]=='H':
        n[k]=3
    data.write("%12.6f%12.6f%12.6f\t%d\t%d\t%s\n" % (coord[k,0], coord[k,1], coord[k,2],n[k], (k+1), ele[k]))
data.write("%endblock AtomicCoordinatesAndAtomicSpecies\n")
layer.write("%s.xyz" % filename)
view(layer)



    