import matplotlib.pyplot as plt
  
# x axis values of line 1
x = [0,0.5]
# corresponding y axis values of line 1
y = [0,0.25]
  
# plotting the points 
plt.plot(x, y, marker='o', markerfacecolor='blue', markersize='12')

# x axis values of line 2
x = [0.5,0.5]
# corresponding y axis values of line 2
y = [0.25,0.5]

# plotting the points 
plt.plot(x, y, marker='o', color='blue', linestyle='dashed', markerfacecolor='white', markersize='12')

# x axis values of line 2
x = [0.5,1]
# corresponding y axis values of line 2
y = [0.5,1]

# plotting the points 
plt.plot(x, y, marker='o', color='blue', markerfacecolor='blue', markersize='12')
  
# naming the x axis
plt.xlabel('x')
# naming the y axis
plt.ylabel('CDF')
  
# giving a title to my graph
plt.title('CDF function')
  
# function to show the plot
plt.show()
