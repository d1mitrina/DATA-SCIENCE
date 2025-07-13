import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,6,5,4,3,3,2])

plt.figure(figsize=(20,7))
plt.title("Line Plot")
plt.xlabel("Number Of People")
plt.ylabel("Quanitity purchased")
plt.plot(x,y,"r--o")
plt.show()

a=np.array([2,4,6,4,7,2,9])
b=np.array([4,2,7,8,4,2,4])

plt.figure(figsize=(10,6))
plt.title("Random Line")
plt.xlabel("Number of bees")
plt.ylabel("Temperature in Celcius")
plt.plot(a,b,"b--o")
plt.show()

