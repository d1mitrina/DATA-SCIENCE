import pandas as pd

df = pd.read_csv("PandasLibrary/titanic.csv")
print(df)

adult_names=df.loc[df["Age"]>18,"Name"]
print(adult_names)

print(df.columns)

df.iloc[0:3,3] = "Mr Bob"
print(df["Name"])
df.to_csv("changeData.csv")

df["NewFare"] = df["Fare"] - 5 
print(df.head())