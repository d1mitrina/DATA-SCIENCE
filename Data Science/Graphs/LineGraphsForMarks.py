import matplotlib.pyplot as plt 
import numpy as np 

x = ["Bob","Dimi","Bill","Maya"]
maths = np.array([100,42,20,79])
cs = np.array([100,100,70,90])
english = np.array([3,5,100,99])

plt.figure(figsize=(10,10))
plt.title("Marks for Subject Exams")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.plot(x,maths,label="MATHS",color="red",linewidth=5)
plt.plot(x,cs,label="COMP SCI",color="blue",linewidth=5)
plt.plot(x,english,label="ENGLISH",color="green",linewidth=5)
plt.legend()
plt.show()