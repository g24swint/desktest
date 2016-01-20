
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib nbagg')
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')


# In[2]:

from __future__ import print_function
from __future__ import division

from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3d
import matplotlib.pyplot as plt
from matplotlib import animation

import logo_maps as lm


# In[3]:

lm.print_bu_logo()


# In[4]:

conferred_hash = lm.degree_hash(lm.CONFERRED, lm.INSTITUTION)
lm.print_ascii_face_32(conferred_hash)


# In[6]:

def facemap_to_points(facemap):
    '''Return the points arrays dimension 1 and dimension 2 that correspond to 
    the face map. Assumes 32x32'''
    points = {'x':[],'y':[]}
    for charcount in range(len(facemap)):
        if facemap[charcount]=='1':
            points['x'].append(charcount % 32 )
            points['y'].append(32 - charcount // 32 )
    return points

def facemap_to_bitmap(facemap):
    '''Return a bitmap (numeric binary) of a given facemap. Assumes 32x32'''
    bitmap = []
    for i_hat in range(32):
        row = []
        for j_hat in range(32):
            row.append( 1 if facemap[i_hat * 32 + j_hat] == '1' else 0 )
        bitmap.append(row)
    return bitmap
    


# In[7]:

conferred_degree_points = facemap_to_points(conferred_hash)
logo_map = lm.bu_logo()
logo_points = facemap_to_points(lm.bu_logo())
logo_bitmap = facemap_to_bitmap(logo_map)
conferred_bitmap = facemap_to_bitmap(conferred_hash)


# In[8]:

from matplotlib.pyplot import figure, scatter

def scatter32x32(pointdict):
    plot_fig = figure()
    scatter(pointdict['x'], pointdict['y'])
    return plot_fig


# In[9]:

#%%
logo_fig = scatter32x32(logo_points)
#%%
degree_fig = scatter32x32(conferred_degree_points)


# In[10]:

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


# In[14]:

fig3d = plt.figure()
fig3d.set_figheight(16)
fig3d.set_figwidth(8)


for rot in [-90,-45,0]

ax = fig3d.add_subplot(221, projection='3d', 
                       azim=0, elev=0)
ax.scatter(xs, ys, zs, zdir='y' )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_xlim3d(-1, 33)
ax.set_ylim3d(-1, 33)
ax.set_zlim3d(-1, 33)

ax2 = fig3d.add_subplot(222, projection='3d', 
                       azim=-90, elev=0)
ax2.scatter(xs, ys, zs, zdir='y' )
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

ax2.set_xlim3d(-1, 33)
ax2.set_ylim3d(-1, 33)
ax2.set_zlim3d(-1, 33)

fig3d.show()


# In[ ]:



