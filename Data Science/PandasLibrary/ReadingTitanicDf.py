import pandas as pd

df = pd.read_csv("PandasLibrary/titanic.csv")
print(df)
print(df.head()) # head function gives the first 5 rows 
print(df.tail()) # tail function gives the last 5 rows 
print(df.head(9)) # head function gives the first 9 rows 

print (df.info())# prints info of data
print (df.size)# prints size of date
print (df.shape) #returns num of rows and colums
print (df[["Age","Name"]])
print (df[df["Survived"]==1])
female = df[df["Sex"]=="female"]
print (female)
print(female[female["Age"]<=30])
print()
print(df.iloc[0:3,0:3]) #rows n columns
print()
print(df.iloc[1:3,0:4]) #rows n columns

