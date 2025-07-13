import matplotlib.pyplot as plt 
import numpy as np 

ages = np.array([3,5,2,8,6,5,7,9,3,4,4,98,90,40,34,24,45,7,44,66,88,99,22,33,13,5,76,6,8,0,3,5,7,88,44,3,54,22,45,23,33,57,85])
bins= np.array([0,10,20,30,40,50,60,70,80,90,100])


plt.figure(figsize=(5,5))
plt.title("Age Interval")
plt.xticks(ticks=bins,labels=bins)
plt.ylabel("Frequency")
plt.hist(ages,bins,color="red")
plt.show()