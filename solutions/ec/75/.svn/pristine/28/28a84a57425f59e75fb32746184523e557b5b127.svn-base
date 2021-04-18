import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111, projection='3d')

n=0.01

x = np.arange(0,0.5,n)
y = np.arange(0,0.5,n)
X,Y = np.meshgrid(x,y)

#creating array for storing Z values
Z = ( X * 0) + (Y * 0)
#

for i in range(50):
  for j in range(50):
    if X[i][j]+Y[i][j]<(1/2):
      Z[i][j]=2
    else:
      Z[i][j]=0


ax1.set_title('P(X+Y<1/2)')
ax1.plot_surface(X,Y,Z)
#,cmap='viridis',edgecolor='none'

plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0,1)
plt.ylim(0,1)
#plt.xscale()
#plt.xticks()
plt.xticks(np.arange(0, 1, 0.1))
plt.yticks(np.arange(0, 1, 0.1))
#plt.annotate('point 1',xy=(0,0.5),xytext=(0,0.5),arrowprops = dict(facecolor ='green',
                                 # shrink = 0.05),)
#plt.annotate("point 2",(0.5,0,0))
#plt.annotate(xy=[0.5,0],s='point 1')
ax1.text(0,0.5,0,"(0,0.5,0)",color='black')
ax1.text(0.5,0,0,"(0.5,0,0)",color='yellow')
ax1.text(0.5,0,2,"(0.5,0,2)",color='yellow')
ax1.text(0,0.5,2,"(0,0.5,2)",color='black')
plt.show()