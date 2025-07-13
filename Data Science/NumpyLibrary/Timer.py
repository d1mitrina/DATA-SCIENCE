import numpy as np 
import time 

time1 = time.time()
list1 = [i for i in range(10000000)]
time2 = time.time()
print("Total time taken for creation of a list: ",(time2-time1))

time3 = time.time()
array1 = np.arange(10000000)
time4 = time.time()
print("Total time taken for creation of a array: ",(time4-time3))

