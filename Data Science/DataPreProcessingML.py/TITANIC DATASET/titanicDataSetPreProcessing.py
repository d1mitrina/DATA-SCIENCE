import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

df = pd.read_csv("PandasLibrary/titanic.csv")

print(df.head())
print(df.info())
print(df["Sex"].value_counts()) 

df["Sex"] = df["Sex"].replace({"male":0,"female":1})
print(df["Sex"].value_counts()) #verified that data successfully changed 
print(df["Pclass"].value_counts())

#data visualisation

print(df["Pclass"].value_counts())
print(df["Survived"].value_counts())

plt.figure(figsize=(5,5))
x = df["Pclass"]
y = df["Survived"]
plt.plot(x,y,color="Red")
plt.xlabel("Passenger class")
plt.ylabel("Surcival rate")
plt.title("How pclass affects survival rate in titanic")
plt.show()


#DATA is standarsized, so now we apply ML model so DIVIDE data set into two parts: feature variables 

X = df[["Pclass","Sex","Age"]]
y = df["Survived"]
print(X.head())
print(y.head()) 

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
print(metrics.accuracy_score(predictions,ytest))


#70% accuracy score and above is good 