import numpy as np

radii = [3.53,4,8,4.4,20,18,5,2,3,3]
pi = 3.14
for i in radii:
    area = ((i**2) * pi)
    print(area)


radius = np.array([3.53,4,8,4.4,20,18,5,2,3,3])
area = np.pi*(radius**2)
print(area)

#list --> cannot mulitply each value by 2 that efficiently than arrays
nums = [1,4,6,3,5,8,4,3,5,7,4,34444,68]
print(nums*2)

#every value multiplied by 2
numbers = np.array([1,4,6,3,5,8,4,3,5,7,4,34444,68])
multiply = numbers*2
print(multiply)

#arrays are faster, more efficient, take up less storage/space

