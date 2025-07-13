import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
df = pd.read_csv("PandasLibrary/titanic.csv")


#plot a pie chart graphs for the total number of men and women in the titanic 
label = ["Men (573)","Women (314)"]
plt.figure(dpi=108)
slices = df["Sex"].value_counts()
print(slices)
print(slices)
plt.title("PieChart for number of men and women on titanic")
plt.pie(slices,labels=label)
plt.show()

#plot a histogram for the age of people present

x = df["Age"]
plt.figure(figsize=(5,5))
plt.hist(x,bins=20,color="red")

plt.title("Ages of People Present on Titanic ")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()


#plot a graph for the fare for men and women    
x = df["Sex"]
y = df["Fare"]
fareofMen = df[df["Sex"]=="male"]["Fare"].mean()
fareofWomen = df[df["Sex"]=="female"]["Fare"].mean()
genders = ["Male","Female"]
fares = [fareofMen,fareofWomen]
plt.figure(figsize=(10,8))
plt.title("The fare for men and women")
plt.xlabel("Gender")
plt.ylabel("Fare")
plt.bar(genders,fares,color=["red","blue"])
plt.show()

