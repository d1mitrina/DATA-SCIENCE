#Data Analysis Salary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/SALARY DATASET/salary.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

df.columns = ["Age","Class","ID","Education","Years of experience","Marriage Status","Occupation","Relashionship","Race","Sex","Capital Gain","Capital Loss","Hours per Week","Country","Income"]
print(df.head)
#check for ?
 #axis = 0 when data is horzontal format axis=1 when data is vertival
print(df.isin([" ?"]).sum(axis=0))

df["Class"] = df["Class"].replace(" ?", np.nan) #replacing charecters "?" with nan vakues to be removed later
df["Occupation"] = df["Occupation"].replace(" ?", np.nan)
df["Country"] = df["Country"].replace(" ?", np.nan)
print(df.isin([" ?"]).sum(axis=0))
print(df.isnull().sum())

df.dropna(inplace= True) #functuion drops all nan value, makes change permament 
print(df.isnull().sum()) #alwayts check again to ensure code works




df.drop(["Capital Gain","Capital Loss","ID","Hours per Week"])
















