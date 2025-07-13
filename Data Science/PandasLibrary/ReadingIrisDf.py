import pandas as pd 

df = pd.read_csv("PandasLibrary/iris.csv")
print(df)
print("Min sepal length is:",df["sepal_length"].min())
print("Min petal_length",df["petal_length"].min())
print("Min petal_width",df["petal_width"].min())
print("Average sepal length is:",df["sepal_length"].mean())
print("Average petal_length",df["petal_length"].mean())

print(df["species"].value_counts())




