import pandas as pd 
import matplotlib.pyplot as plt
import  numpy as np

df = pd.read_csv("PandasLibrary/titanic.csv")
print(df.head())

#SCATTER GRAPH
plt.figure(figsize=(5,5))
x = df["Pclass"]
y = df["Fare"]

plt.scatter(x,y,color="Red")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Passenger Class VS Fare")
plt.show()

#PIECHART
label = ["Not Survived","Survived"]

plt.figure(dpi=108)
slices = df["Survived"].value_counts()
print(slices)
plt.title("PieChart for who survived // not survived")
plt.pie(slices,labels=label)
plt.show()


label1 = ["Pclass = 3","Plass = 1","Pclass = 2"]
plt.figure(dpi=108)
slices1 = df["Pclass"].value_counts()
print(slices1)
plt.title("Piechart for different classes in titanic")
plt.pie(slices1,labels=label1)
plt.show()