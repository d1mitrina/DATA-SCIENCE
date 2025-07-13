#Data Analysis of Risk of Heart Disease HW
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Creating dataset using dictionary

df = pd.read_csv("DataPreProcessingML.py/heart_disease_risk_dataset_earlymed.csv")

#STEP 2: Presenting Data about the dataset 

print("PreProccessing Data:")
print(df.head())
print("\nData Info:") #Useful metadata
print(df.info())
#1 = yes, 0= no

#STEP 3: Data Visualisation 

print(df["Heart_Risk"].value_counts()) #counts all sub species in numerical data 
print(df["Diabetes"].value_counts()) #counts all sub species in numerical data 

#Histrogram 
ages_diabetes = df[df["Diabetes"] == 1]["Age"]
plt.figure(figsize=(5,5))
plt.title("Age Distribution for People with Diabetes")
plt.ylabel("Number of People")
plt.xlabel("Age")
plt.hist(ages_diabetes, bins=5, color="red")
plt.show()

#Bar chart DOESNT WORK???
grouping_gender = df.groupby("Gender")["Heart_Risk"].mean()

y = df["Heart_Risk"]
plt.figure(figsize=(5,5))
plt.title("Risk of heart disease based on gender")
plt.xlabel("Gender")
plt.ylabel("Survived")
plt.bar(grouping_gender.index,grouping_gender.values,color="red") #.index helps you search values 
plt.show()

#Scatter 
plt.figure(figsize=(5,5))
x = df["Age"]
y = df["Heart_Risk"]
plt.scatter(x,y,color="Red")
plt.xlabel("Age")
plt.ylabel("Heart_Risk")
plt.title("How age determines heart risk")
plt.show()


#Pie chart
label = ["Female","Male"]
plt.figure(dpi=108)
slices = df["Heart_Risk"].value_counts()
print(slices)
plt.title("PieChart")
plt.pie(slices,labels=label)
plt.show()











