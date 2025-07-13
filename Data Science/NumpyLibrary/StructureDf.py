#list == array in NUMPY 
import numpy as np # np is nickname of numpy--> could use another variable 

#two dimmemsional arrays with fuctions ones and zeros 

array1 = np.ones((5,5),dtype=int) #dtype = datatype (Float data type by default)
print(array1)

#array1 = np.ones((5,5))#dtype = datatype (Float data type by default)
print(array1)

print(type(array1))

array0 = np.zeros((5,5),dtype = int) 
print(array0)




#one or two dimmesional array?

print(array1.ndim) #NDIM is key word giving the dimmesnion of array



#shape of array? number of rows or colums?

print(array1.shape) #5,5 so 5t rows and 5 columns




#generate a range of numbers 
array3 = np.arange(1,21) #1D array generates numbers in order to 20
print(array3)

array4 = np.arange(1,25,3) #1D array generates numbers in order to 25, difference is three
print(array4)

array5 = np.linspace(1,30,5) #returns 4 numbers between 1 and 30 with equal differences between each number
print(array5)



#how to convert 1D arrays into 2D?

array6 = array3.reshape(4,5)
print(array6)

array7 = array3.reshape(10,2)
print(array7)

array8 = array6.reshape(20)
print(array8)



#random.randit is already in numpy:


array9 = np.random.randint(1,100,15) #(start, end, how many nums)
print(array9)

array9.sort()
print(array9)

array10 = np.random.randint(1,100, size =(5,5))
print(array10)


#list into arrays 

x = [1,2,3,4,5,6,7,7,8,9,0,6,4,3,4,5,6,8]
print(type(x)) #keywords never take any inputs but functions take something as input most the time

y = np.array(x)
print(type(y))

b = list(array10)

print(type(b))


print(np.sqrt(25))






















