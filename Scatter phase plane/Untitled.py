#!/usr/bin/env python
# coding: utf-8

# In[50]:



# Reading an excel file using Python
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import math

# Give the location of the file
loc = (r'C:\Users\Ali\Desktop\phas cerve\sam.xlsx')
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
conter=[]
for x in range(1, 14):
    conter.append(x)
a=np.ones(np.size(conter))#r
azm = a
z = conter
for y in range(1, 17):# For row 0 and column 0
    data=[]
    for x in range(1, 14):
        data.append(sheet.cell_value(y, x)*360/(2*math.pi))
    rad = np.radians(data)
    ax = plt.subplot(projection="polar")
    plt.scatter(rad, azm, c=z, cmap='brg')
    ax.set_rgrids([1.5])#ax.grid(which="major")#plt.colorbar()
    plt.savefig(r'C:\Users\Ali\Desktop\phas cerve\pic\frame_'+ str(y)+'_.png', dpi=1200)
    plt.close('all')    #plt.show()


# In[57]:


import matplotlib.pyplot as plt
import numpy as np

data = [[0, 1.200e+01, 1.700e+01, 2.300e+01, 2.800e+01, 3.400e+01, 3.900e+01, 4.500e+01, 5.000e+01, 5.600e+01, 6.200e+01, 6.700e+01, 7.300e+01, 7.800e+01, 8.400e+01, 8.900e+01, 3.934e+01, 4.004e+01, 4.054e+01, 4.114e+01, 4.154e+01, 4.204e+01, 4.254e+01, 4.294e+01, 4.334e+01, 4.374e+01, 4.414e+01, 4.454e+01, 4.494e+01, 4.534e+01, 4.564e+01, 4.604e+01, 4.644e+01, 4.684e+01, 4.714e+01, 4.754e+01, 4.794e+01, 4.824e+01, 4.864e+01, 4.904e+01, 4.944e+01, 4.984e+01, 5.014e+01, 5.054e+01, 5.094e+01, 5.134e+01, 5.174e+01, 5.214e+01, 5.264e+01, 5.304e+01, 5.344e+01, 5.394e+01, 5.444e+01, 5.494e+01, 5.544e+01, 5.604e+01, 5.674e+01, 5.764e+01],
        [1.960e+02, 3.600e+01, 2.360e+02, 7.600e+01, 2.760e+02, 1.160e+02, 3.160e+02, 1.560e+02, 3.560e+02, 1.960e+02, 3.600e+01, 2.360e+02, 7.600e+01, 2.760e+02, 1.160e+02, 3.160e+02, 6.500e+00, 3.400e+00, 3.588e+02, 2.500e+00, 3.594e+02, 3.509e+02, 5.000e-01, 6.900e+00, 1.090e+01, 3.478e+02, 1.250e+01, 1.050e+01, 7.300e+00, 2.700e+00, 3.571e+02, 3.507e+02, 1.060e+01, 3.200e+00, 3.556e+02, 3.480e+02, 7.300e+00, 3.597e+02, 3.527e+02, 1.260e+01, 6.600e+00, 1.200e+00, 3.570e+02, 3.538e+02, 3.520e+02, 3.516e+02, 3.528e+02, 3.560e+02, 1.200e+00, 8.800e+00, 3.567e+02, 1.030e+01, 6.800e+00, 8.300e+00, 3.583e+02, 3.581e+02, 3.568e+02, 3.589e+02],
        [3.580e-04, 6.100e-04, 3.220e-04, 4.850e-04, 4.360e-04, 2.910e-04, 1.120e-03, 2.320e-04, 4.300e-03, 2.680e-04, 1.700e-03, 3.790e-04, 7.460e-04, 8.190e-04, 1.030e-03, 3.650e-03, 3.050e-03, 3.240e-03, 3.340e-03, 3.410e-03, 3.490e-03, 3.290e-03, 3.630e-03, 3.510e-03, 3.320e-03, 3.270e-03, 3.280e-03, 3.470e-03, 3.720e-03, 3.960e-03, 3.980e-03, 3.700e-03, 3.630e-03, 4.100e-03, 4.080e-03, 3.600e-03, 3.990e-03, 4.530e-03, 4.040e-03, 3.630e-03, 4.130e-03, 4.370e-03, 4.340e-03, 4.210e-03, 4.100e-03, 4.090e-03, 4.190e-03, 4.380e-03, 4.460e-03, 4.080e-03, 4.420e-03, 3.960e-03, 4.230e-03, 4.120e-03, 4.440e-03, 4.420e-03, 4.370e-03, 4.380e-03]]

rad = np.radians(data[1])
azm = data[0]
z = data[2]

ax = plt.subplot(projection="polar")
plt.scatter(rad, azm, c=z, cmap='coolwarm')
ax.set_rgrids([100])#ax.grid(which="major")#plt.colorbar()
plt.show()


# In[ ]:




