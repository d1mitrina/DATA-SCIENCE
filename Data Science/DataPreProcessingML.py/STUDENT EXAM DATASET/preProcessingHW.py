# DATA PREPROCESSING FOR MACHINE LEARNING: STUDENT EXAM PERFORMANCE DATASET

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# STEP 1: Creating dataset using dictionary

df = pd.read_csv("DataPreProcessingML.py/STUDENTEXAM.csv")


print("Initial Data:")
print(df.head())
print("\nData Info:") #Useful metadata
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum()) #helps assess how much data we need to impute 


# STEP 2: Separate Features and Target
X = df.iloc[:, 0:3]
y = df.iloc[:, 3]

print("\nFeature Variables (X):")
print(X)
print("\nTarget Variable (y):")
print(y)


# STEP 3: Handle Missing Values (replace with mean)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean") #creates an imputer than replaces missing with mean of respetive column
X.iloc[:, 1:3] = imputer.fit_transform(X.iloc[:, 1:3])

print("\nAfter Imputing Missing Values:")
print(X)


# STEP 4: OneHotEncoding for Categorical Column ('Gender'), must be converted to numerical code 
col_trans = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
X_encoded = col_trans.fit_transform(X) #Applies transformation
X_encoded_df = pd.DataFrame(X_encoded)

print("\nAfter OneHotEncoding:")
print(X_encoded_df)


# STEP 5: Label Encode Target Variable, YES = 1, NO = 0 
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("\nEncoded Target Variable (y):")
print(y_encoded)


# STEP 6: Split into Training and Test Sets
xtrain, xtest, ytrain, ytest = train_test_split(X_encoded_df, y_encoded, test_size=0.2, random_state=42)

print("\nTraining Set (X):")
print(xtrain)
print("\nTest Set (X):")
print(xtest)


# STEP 7: Standardize Numerical Columns
sc = StandardScaler() #scaling data, standardize features
xtrain.iloc[:, 2:4] = sc.fit_transform(xtrain.iloc[:, 2:4])
xtest.iloc[:, 2:4] = sc.transform(xtest.iloc[:, 2:4])

print("\nStandardized Training Set:")
print(xtrain)
print("\nStandardized Test Set:")
print(xtest)
