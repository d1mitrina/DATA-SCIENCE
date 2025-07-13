#making a raw dictionary into a Data frame 
import pandas as pd
dict = {"name":["Dimi","Mia","Eve","Bob"],"age":[16,29,12,43],"gender":["F","F","F","M"],"job":["Yes","No","Yes","Yes"]}
df = pd.DataFrame(dict)
print(df.head())
print(df.shape)
print(df["name"])
print(df[["name","age"]])
print(df["age"].max())
print(df["age"].min())

print(df.iloc[3,3])
print(df.iloc[:2]) #first two columns 
print()
