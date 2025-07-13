import pandas as pd

df = pd.read_csv("PandasHomework/adult.csv") #relative path to data set
print(df)
print(df.head()) # head function gives the first 5 rows 
print(df.tail()) # tail function gives the last 5 rows 
print(df.head(7)) # head function gives the first 9 rows 

print (df.info())# prints info of data
print (df.size)# prints size of date
print (df.shape) #returns num of rows and colums

print(df[["age","education"]])
print(df[df["sex"]=="Female"])
HIGHincome = df[df["income"]==">50K"]
print (HIGHincome)
print(HIGHincome[HIGHincome["age"]<=30])

print(df.iloc[0:3,0:3]) #rows n columns
print(df.iloc[1:3,0:4]) #rows n columns