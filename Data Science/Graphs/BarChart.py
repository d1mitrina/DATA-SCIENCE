import matplotlib.pyplot as plt 
import numpy as np 

x = ["Dog","Cat","Bees","Mouse","Parrot"]
y = np.array([1020,2000,10,0,900])

plt.figure(figsize=(5,5))
plt.title("Number of Pets")
plt.xlabel("Type of Pet")
plt.ylabel("Number of People owning")
plt.bar(x,y,color="red")
plt.show()