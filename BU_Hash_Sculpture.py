# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
%matplotlib qt

from __future__ import print_function
from __future__ import division
import hashlib
import binascii
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation

#%%
def degree_hash():
    conferral=b'Galen S. Swint, BSCS, 2000-05-13'
    institution=b'School of Engineering and Computer Science, Baylor University'
    
    print(conferral)
    print(institution)
    m = hashlib.sha512()
    m.update(conferral)
    conferred_hash = '{0:0512b}'.format(int(binascii.hexlify(m.digest()),16))
    
    m2 = hashlib.sha512()
    m2.update(institution)
    institution_hash = '{0:0512b}'.format(int(binascii.hexlify(m2.digest()),16))
    
    # print len(institution_hash)
    return conferred_hash + institution_hash
def print_ascii_face_32(facemap):
    '''Print the face of a 32 wide map'''
    for i in range(len(facemap)):
        print(facemap[i], end='')
        if i % 32 == 31:
            print('')


conferred_hash = degree_hash()
print_ascii_face_32(conferred_hash)

#%%
def bu_logo():
    logo_map = '''
1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	0	1	0	1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	1
1	1	1	0	0	0	0	0	0	0	0	0	0	1	1	0	0	1	1	1	0	0	0	0	0	0	0	0	1	1	1	0
1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	0	1	1	1	0	0	0	0	0	0	1	1	1	0	0
1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	0	0	0
1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	0	0
'''
    logo_map = logo_map.replace('\n','\t').strip().split('\t')
    print(logo_map)
    return logo_map
logo_map = bu_logo()
print_ascii_face_32(logo_map)

#%%

def facemap_to_points(facemap):
    '''Return the points arrays dimension 1 and dimension 2 that correspond to 
    the face map. Assumes 32x32'''
    points = {'x':[],'y':[]}
    for charcount in range(len(facemap)):
        if facemap[charcount]=='1':
            points['x'].append(charcount % 32 )
            points['y'].append(32 - charcount // 32 )
    return points
    
conferred_degree_points = facemap_to_points(conferred_hash)
logo_points = facemap_to_points(logo_map)
    
#%%
def facemap_to_bitmap(facemap):
    '''Return a bitmap (numeric binary) of a given facemap. Assumes 32x32'''
    bitmap = []
    for i_hat in range(32):
        row = []
        for j_hat in range(32):
            row.append( 1 if facemap[i_hat * 32 + j_hat] == '1' else 0 )
        bitmap.append(row)
    return bitmap
logo_bitmap = facemap_to_bitmap(logo_map)

for i in range(len(logo_bitmap)):
    print(logo_bitmap[i])
#%%
conferred_bitmap = facemap_to_bitmap(conferred_hash)
for i in range(len(conferred_bitmap)):
    print(conferred_bitmap[i])



#%%
from matplotlib.pyplot import figure, scatter

def scatter32x32(pointdict):
    plot_fig = figure()
    scatter(pointdict['x'], pointdict['y'])
    return plot_fig
    
#%%
logo_fig = scatter32x32(logo_points)
#%%
degree_fig = scatter32x32(conferred_degree_points)
#%%
import pandas as pd

# each list elemetn is a row
df1 = pd.DataFrame(data=[[1,0], [0,1]] )
df2 = pd.DataFrame(data=[[1,0], [1,0]] )

print("df1:")
print(df1)
print("df2:")
print(df2)

#%%
cubespace = []
xs = []
ys = []
zs = []

for z in range(32):
    for y in range(32):
        for x in range(32):
            # reverse the order of the y -axis as the bitmaps have y=0 in 
            # top left. Use y,x ordering because stores in rows
            xyz_val = (x, 32-y, z, 
                       conferred_bitmap[y][x] & logo_bitmap[y][z] )
            cubespace.append(xyz_val)
            if xyz_val[3] == 1:
                xs.append(xyz_val[0])
                ys.append(xyz_val[1])
                zs.append(xyz_val[2])
#print(cubespace)
#%%
min_az, max_az, stepsize = (0,361,9)
n_steps = (max_az - min_az) // stepsize + 1
print(n_steps) 
#%%
fig3d = plt.figure()
fig3d.set_figheight(6*n_steps)
fig3d.set_figwidth(6)


step = 1
for rotation in range(min_az,max_az,stepsize):
    ax = fig3d.add_subplot(n_steps, 1, step, projection='3d', 
                           azim=rotation, elev=0)
    step = step + 1
    ax.scatter(xs, ys, zs, zdir='y' )
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_zlabel('z label')
    
    ax.set_xlim3d(-1, 33)
    ax.set_ylim3d(-1, 33)
    ax.set_zlim3d(-1, 33)
fig3d.show()
#%%
def animate_rotation(nframe):
    plt.cla()
    plt.plot(projection='3d',azim=(nframe * 9 + 0), elev=0)
    print("type"+str(type(ax)))
    plt.set_xlim3d(-1, 33)
    plt.set_ylim3d(-1, 33)
    plt.set_zlim3d(-1, 33)
    plt.scatter(xs, ys, zs, zdir='y' )

fig3d = plt.figure()
animate_rotation(0)

#animation.FuncAnimation(fig3d, animate_rotation, frames=n_steps)
