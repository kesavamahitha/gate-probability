# program to plot CDF
import numpy as np 
import matplotlib.pyplot as plot

#defining the function for the CDF
def F(x):
  if(x<0):
    return 0
  elif(x>=0) and (x<1/2):
    return x**2
  elif(x>=1/2) and (x<1):
    return 3/4
  elif(x>=1):
    return 1;
  else:
    return 0  

    #plotting Cdf 
X = np.linspace(-2,2,100000)

Y = [F(x) for x in X]
plot.xlabel('x')
plot.ylabel('$F(x)$')
plot.plot(X,Y)
plot.grid()
plot.savefig('Assignment2.png' , dpi=125)
plot.show()    
