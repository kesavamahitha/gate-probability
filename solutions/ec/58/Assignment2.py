import matplotlib.pyplot as plt
import numpy as np
def F(x):
  if(x<0):
    return 0
  elif(x>=0 and x<1) :
   return x/2
  elif(x>=1 and x<2) :
   return 3/5
  elif(x>=2 and x<3) :
   return (1/2)+(x/8)
  elif(x>=3):
   return 1
X=np.linspace(-3,5,100000)
Y=[F(x) for x in X]
plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.title('Cumulative Distribution Function')
plt.show