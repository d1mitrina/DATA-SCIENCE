#Take your own data of a grocery shop and practice all the numpy functions used in the session today 

print("Welcome to the Grocery Shop Data! \n")
import numpy as np 
import time
from scipy import stats 

time1 = time.time()

item = np.array(["Bananas","Apples","Carrots","Peas","Milk","Orange","Blueberries","Passionfruit","Bread","Juice"])
price = np.array([10,4,8,3.40,3,9,4,5.5,10,200])
unit = np.array([100,200,100,400,200,400,600,300,400,200])
array3 = [[item[i],price[i]]for i in range (len(item))]

print(array3)
#num of items 
print("The number of items at this grocery shops is: ",np.size(item))

#total monetary value of all items 
total = price * unit 
monetary = np.sum(total)
print("\nTotal monetary price of all items is: ",monetary)

#total value of each item 
for i in range(len(item)):
    total_price = price[i]*unit[i]
    print(f"The total value of {item[i]} is: ",total_price)

#mean 
mean_value = np.mean(price)
print("The mean price is: ",mean_value)

#median  
median_value = np.median(price)
print("The median price is: ",median_value)

#cheapest
cheapest = np.min(price) 
print("The cheapest item is: ",cheapest)

#most expensive
expensive = np.max(price)
print("The most expensive item is: ", expensive)

#mode (using scipy)
most_common_price = stats.mode(price)
print("The mode price is: ", most_common_price)

#calculating time taken 
time2 = time.time()
total_time = time2-time1
print("This took",total_time,"to calculate and display on your screen!")




