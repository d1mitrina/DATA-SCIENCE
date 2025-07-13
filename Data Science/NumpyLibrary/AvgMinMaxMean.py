import numpy as np
from scipy import stats

#array.size() --> gives number of items in an array 

price = np.array([198,132,148,156,132,128,145,156,156,201])
units = np.array([9,8,9,9,8,8,9,6,5,7])
print(price)
print(units)

total_price = price*units
print(total_price)

total_monetary_price = np.sum(total_price)
print("The total monetary price is:", total_monetary_price)

average_prive = np.mean(price)
print("The average price is: ", average_prive)

cheapest_item = np.min(price)
print("The cheapest item is: ", cheapest_item)

expensive_item = np.max(price)
print("The most expensive item is: ", expensive_item)

median_price = np.median(price)
print("The median price is: ", median_price)

most_common_price = stats.mode(price)
print("The mode price is: ", most_common_price)

