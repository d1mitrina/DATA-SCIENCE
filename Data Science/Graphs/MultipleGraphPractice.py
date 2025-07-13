#Take any dataset and practice all the matplotlib functions used in the session 

import matplotlib.pyplot as plt 
import numpy as np 

#graph

x = ["2s","4s","6s","8s"]
car1 = np.array([20,40,60,80])
car2 = np.array([10,23,34,102])

plt.figure(figsize=(10,5))
plt.title("Velocity Time Graph")
plt.xlabel("Time in Seconds")
plt.ylabel("Velocity in m/s")
plt.plot(x,car1,label="CAR1",color="red",linewidth=5)
plt.plot(x,car2,label="CAR2",color="blue",linewidth=5)
plt.legend()
plt.show()

#BarChart

x = ["Strawberry","Vanilla","Chocolate","Mint Chocolate","Cherry"]
y = np.array([40,90,78,50,13])

plt.figure(figsize=(10,8))
plt.title("Type of Ice cream flavours sold in 1 day")
plt.xlabel("Flavor")
plt.ylabel("Amount Sold")
plt.bar(x,y,color="red")
plt.show()

#mathsGraph 

x = np.arange(0,50)
y1 = x**2
y2 = x**4

plt.figure(figsize=(5,5))
plt.title="Graphs with x to power of indicies"
plt.xlabel="x"
plt.ylabel="y"
plt.plot(x,y1,color="red",label="to power of 4")
plt.plot(x,y2,color="blue",label="to power of 9")
plt.legend()
plt.axis([0,100,0,200])
plt.show()

#historgram


ages = np.array([15,93,12,27,62,61,92,2,76,77,24,49,37,71,33,60,87,31,28,26,6,23,30,64,55,91,46,82,7,43,72,98,16,5,14,1,80,10,52,50,95,47,39,11,70,68,75,51,57,73,84,99,36,79,97,59,22,20,53,88,65,41,89,74,96,19,78,54,86,66,58,56,63,34,13,18,40,83,29,17,100,25,21,3,81,44,9,35,4,48,85,90,32,67,45,69,94,42,8,38])
intervals= np.array([0,10,20,30,40,50,60,70,80,90,100])

plt.figure(figsize=(5,5))
plt.title("Age Interval")
plt.xticks(ticks=intervals,labels=intervals)
plt.ylabel("Frequency")
plt.hist(ages,intervals,color="red")
plt.show()