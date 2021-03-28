import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {12:0, 13:0.05, 14:0.1, 15:0.15, 16:0.2, 17:0.2, 18:0.15, 19:0.10, 20:0.05, 21:0}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (8, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='blue',
        width = 0.2)
 
plt.xlabel("n")
plt.ylabel("Pr(X=n)")
plt.show()