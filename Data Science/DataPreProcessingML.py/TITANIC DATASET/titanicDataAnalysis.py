#Data analysis break down 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("PandasLibrary/titanic.csv")
print(df.head())

survived_df = df[df["Survived"]==1] 
print(survived_df)

print(survived_df["Pclass"].value_counts())


label = ["Class 1","Class 2","Class 3"]

plt.figure(dpi=108)
slices = survived_df["Pclass"].value_counts()
print(slices)
plt.title("PieChart for classes of people who survived on the titanic")
plt.pie(slices,labels=label)
plt.show()

#Historgram 
#bins --> number of bars
ages = df['Age']
plt.figure(figsize=(5,5))
plt.title("Age Interval")
plt.ylabel("Number of people")
plt.xlabel("Age intervals")


plt.hist(ages,bins=4,color="red")
plt.show()

#bar chart 


x = survived_df["Sex"]
y = survived_df["Survived"]

plt.figure(figsize=(5,5))
plt.title("Survival based on gender")
plt.xlabel("Sex")
plt.ylabel("Survived")
plt.bar(x,y,color="red")
plt.show()


