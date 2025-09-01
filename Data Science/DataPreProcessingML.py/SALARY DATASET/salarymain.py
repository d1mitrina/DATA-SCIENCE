#Data Analysis Salary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/SALARY DATASET/salary.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

df.columns = ["Age","Class","ID","Education","Years of experience","MarriageStatus","Occupation","Relashionship","Race","Sex","Capital Gain","Capital Loss","Hours per Week","Country","Income"]
print(df.head)
#check for NaN Spaces
#axis = 0 when data is horzontal format axis=1 when data is vertival
print(df.isin([" ?"]).sum(axis=0))

#replacing spaces with a charecter "?"
df["Class"] = df["Class"].replace(" ?", np.nan) #replacing charecters "?" with nan vakues to be removed later
df["Occupation"] = df["Occupation"].replace(" ?", np.nan)
df["Country"] = df["Country"].replace(" ?", np.nan)
print(df.isin([" ?"]).sum(axis=0))
print(df.isnull().sum())

#Ensuring all the changes are permanent using "inplace" function 
df.dropna(inplace= True) #functuion drops all nan value, makes change permament 
print(df.isnull().sum()) #always check again to ensure code works

#DROP ALL UNSUSED DATA COLUMNS FROM DATASET which are irrelevant in this case 
print(df.columns)
df.drop(["Capital Gain","Capital Loss","ID","Hours per Week","Age","Country"], axis=1, inplace=True)
print(df.columns)

print(df["Income"].value_counts()) #checks types and number of items in income column 
#Mapping the income value to 0 and 1 as all data must be in numbers
df["Income"] = df["Income"].map({" <=50K":0," >50K":1}).astype(int) #mapping allows for creation of dictionary 
print(df.head()) #check
print(df["Income"].value_counts()) #check


meanincome = df["Income"].mean()
print(meanincome)


#SEX
print(df["Sex"].value_counts())
df["Sex"] = df["Sex"].map({" Male":0," Female":1})
print(df.head())
print(df["Sex"].value_counts())


inc = set(df["Income"])

df.groupby("Sex").inc.mean().plot(kind="bar")
plt.show()




























