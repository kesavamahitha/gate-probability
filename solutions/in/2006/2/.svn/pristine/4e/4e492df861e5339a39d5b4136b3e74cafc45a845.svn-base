import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal

#verifying the result obtained with numerical value
c=2 

#generating two uniform distributions 
y_1 = stats.uniform(loc=-c/4, scale=c/2)
y_2 = stats.uniform(loc=(2/c)+(c/4), scale=c/2)

dx = 0.0001
x = np.arange(-4,4,dx)

pmf1 = y_1.pdf(x)*dx
pmf2 = y_2.pdf(x)*dx
conv_pmf = signal.fftconvolve(pmf1,pmf2,'same')

pdf1 = pmf1/dx
pdf2 = pmf2/dx
conv_pdf = conv_pmf/dx


print("Area under pdf of Y_1: " +str(np.trapz(pdf1,x)))
print("Area under pdf of Y_2: " +str(np.trapz(pdf2,x)))
print("Area under convoluted pdf: " +str(np.trapz(conv_pdf,x)))

# Region 1 of PDF
x_1 = np.arange(-4, 1, 0.1)
y_1 = x_1*0
# Region 2 of PDF
x_2 =   np.arange(1, 2, 0.1)
y_2=  x_2 - 1
# Region 3 of PDF
x_3 =   np.arange(2, 3, 0.1)
y_3=  3-x_3
# Region 4 of PDF
x_4 =   np.arange(3, 4, 0.1)
y_4=  x_4*0


# Plotting the points


#plotting pdfs of uniform distributions and convoluted function
plt.plot(x_1, y_1,'b',marker='o',label='X-Theory')
plt.plot(x_2, y_2,'b',marker='o')
plt.plot(x_3, y_3,'b',marker='o')
plt.plot(x_4, y_4,'b',marker='o')
plt.plot(x,pdf1, label='$Y_2$')
plt.plot(x,pdf2, label='$Y_1$')
plt.plot(x,conv_pdf,'r',label='X-Simulation')
plt.legend(loc='best')
plt.suptitle('PDFs')
plt.grid()
plt.show()

# Normalize the data to a proper PDF
Z=conv_pdf/ (dx * conv_pdf).sum()

# Compute the CDF
cdf = np.cumsum(Z * dx)

#Region 1 of CDF
x_1 = np.arange(-4, 1, 0.1)
y_1 = x_1*0
# Region 2 of CDF
x_2 =   np.arange(1, 2, 0.1)
y_2=  (x_2**2-2*x_2+1)/2
# Region 3 of CDF
x_3 =   np.arange(2, 3, 0.1)
y_3=  (6*x_3-x_3**2-7)/2
# Region 4 of CDF
x_4 =   np.arange(3, 4, 0.1)
y_4=  x_4**0

plt.plot(x_1, y_1,'b',marker='o',label='Theory')
plt.plot(x_2, y_2,'b',marker='o')
plt.plot(x_3, y_3,'b',marker='o')
plt.plot(x_4, y_4,'b',marker='o')
plt.plot(x,cdf,'r',label='Simulation')
plt.xlabel('Random Variable , X')
plt.ylabel('$F_{X}(x)$')
plt.suptitle('CDF of X')
plt.legend(loc='best')
plt.grid()
plt.show()
