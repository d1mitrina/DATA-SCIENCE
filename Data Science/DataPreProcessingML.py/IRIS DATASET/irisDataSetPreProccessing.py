import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier #helps classfiy data 
from sklearn import metrics

df = pd.read_csv("PandasLibrary/iris.csv")

print(df.head())
print(df.info())
print(df["species"].value_counts()) #counts all sub species in numerical data 

df["species"] = df["species"].replace({"setosa":0,"versicolor":1,"virginica":2})
print(df["species"].value_counts()) #verified that data successfully changed 

#Before applying model, we will analyse data step by step using visualisation 
#Scatter Graph 
plt.figure(figsize=(5,5))
x = df["sepal_length"]
y = df["species"]
plt.scatter(x,y,color="Red")
plt.xlabel("Sepal Length")
plt.ylabel("Species")
plt.title("How sepal length can determine species of flower")
plt.show()


plt.figure(figsize=(5,5))
x = df["sepal_width"]
y = df["species"]
plt.scatter(x,y,color="Blue")
plt.xlabel("Sepal Width")
plt.ylabel("Species")
plt.title("How sepal width can determine species of flower")
plt.show()


plt.figure(figsize=(5,5))
x = df["petal_length"]
y = df["species"]
plt.scatter(x,y,color="Yellow")
plt.xlabel("Petal length")
plt.ylabel("Species")
plt.title("How petal length can determine species of flower")
plt.show()

plt.figure(figsize=(5,5))
x = df["petal_width"]
y = df["species"]
plt.scatter(x,y,color="Green")
plt.xlabel("Petal Width")
plt.ylabel("Species")
plt.title("How petal width can determine species of flower")
plt.show()

#DATA is standarsized, so now we apply ML model so DIVIDE data set into two parts: feature variables 

X = df[["petal_length","petal_width","sepal_length","sepal_width"]]
y = df["species"]
print(X.head())
print(y.head()) #checking

#split data into two parts 
xtrain,xtest,ytrain,ytest = train_test_split(X,y,test_size = 0.2,random_state = 42)
print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)

model = DecisionTreeClassifier(max_depth=3,random_state = 1) #internally takes 3 decisions
model.fit(xtrain,ytrain)
#Now we will make predictions
predictions = model.predict(xtest)
print(metrics.accuracy_score(predictions,ytest)) #checks and gives accuracy score


