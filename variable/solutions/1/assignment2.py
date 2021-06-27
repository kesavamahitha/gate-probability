import matplotlib.pyplot as plt
import numpy as np
x0=np.linspace(-1,0,200)
x1=np.linspace(0,1,200)
y0=x0*x0/2+x0+0.5
y1=-x1*x1/2+x1+0.5
plt.plot(x0,y0,label='line 1')
plt.plot(x1,y1,label='line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('F(x)PLOT')
plt.legend()
plt.show()
