#data needs to be clean to be able to be understood and used for prediction models

#STEP1: CREATING DATA FRAME FROM RAW DATA AND CHEKCING FOR MISSING VALUES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("DataPreProcessingML.py/Data.csv")
print(df.head())
print(df.info()) #--> function that gives database informatin 
#non-null data without missing values 

#checking how many missing values there are
print(df.isnull().sum())





#STEP2: DIVIDING VARIABLES INTO FEATURE(BASED ON WHAT FACTORS THE TRAGET IS PREDICTED) AND TARGET(RESULT) VARIABLES 
X = df.iloc[:,0:3] #takes data in two parts 1) index of rows, : means everything  2) index of number of columns takes only first 3 columns. (0,1,2) as we dont wamt the 4th column
y = df.iloc[:,3] #takes all rows but only 3rd column 
print(X)
print(y) #target variable --> the amswer that the machine would predicts 
#feature columns are represented by capital X --> based on the data / features /factors, will the machine predict the target
#must import a module that helps us remove missing values 






#STEP3: REPLACING MISSING VALUES WITH MEAN OF THE COLUMN
from sklearn.impute import SimpleImputer # helps remove missing 
#by 1) deleting data where missing values are. 2) by replacing mising value with the average of the column 

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
result = imputer.fit_transform(X.iloc[:,1:3])
X.iloc[:,1:3] = result #first and second index // second and third column. emilinating country factor as it is unuseful
print(X)




#STEP4: CONVERTIMG STRING VALUES IN NUMBERS (IN COLUMNS)
#data set should onlt be either integer or boolean values
#ENCODING 
#HOTENCODING  - is a method that coverts catagorical values/ variables into a binary format, which is used in ML to improve prediction
#creating columns 

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder #modules

col_trans=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough") 
result2 = col_trans.fit_transform(X)
newdf = pd.DataFrame(result2)
print(newdf)



#STEP5: LABEL ENCODING, CONVERTING TARGET INTO INTEGER 
from sklearn.preprocessing import  LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y) #takes the y value that had nitially been seprated as a target in step 2 
print(y)
#NOW DATA IS CLEAN AND READY TO APPLY ML MODEL 





#STEP6: DIVIDE DATA INTO TWO PARTS: TRAINING AND TESTING SET (USUALLY MILLIONS OF DATA IS REQUIRED)
from sklearn.model_selection import train_test_split 
#this model will split your data into two parts 

xtrain,xtest,ytrain,ytest = train_test_split(newdf,y,test_size = 0.2,random_state = 42) #random esures that out data is not changed everytime we run the code. 
print(xtrain)
print(xtest)
print(ytrain)
print(ytest)




#STEP7: CONVERTING / STANDARDIZINGF ALL DATA INTO (ONE UNIT) SO no number is very small or too big 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
xtrain.iloc[:,3:5] = sc.fit_transform(xtrain.iloc[:,3:5])
xtest.iloc[:,3:5] = sc.fit_transform(xtest.iloc[:,3:5])
print(xtrain) #always standarize the feature not target as target is already 0 or 1 
print(xtest)


























