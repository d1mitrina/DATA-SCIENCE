import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(1,10)
y1= x**2
y2=x**3

plt.figure(figsize=(5,5))
plt.title="Quadratic and Cubic Graphs"
plt.xlabel="x"
plt.ylabel="y"
plt.plot(x,y1,color="red",label="SQUARED")
plt.plot(x,y2,color="blue",label="CUBED")
plt.legend()

plt.show()