import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/WHO-COVID-19-global-data.csv")
print(df.head(10))
print(df.info())
print(df.shape)
print(df.isnull().sum())
print(df.columns)

# shortening column nanmes 
df2 = df[['DateReported', 'Country_code', 'Country', 'WHO_region', 'New_cases','Cumulative_cases', 'New_deaths', 'Cumulative_deaths']]
df2.columns = ('date_reported', 'country_code', 'country', 'region', 'new_cases','cumul_cases', 'new_deaths', 'cumul_deaths')
print(df2.head())

# removing missing values // data cleaning 
df2['country_code'].fillna(value =" ",inplace = True) 
# inplace makes changes in data frame permanent
# now data is clean

#grouping data according to the date 
#more than one data type = object

df2["date_reported"] = pd.to_datetime(df2["date_reported"]) #fuction which converts 
print(df2.info())
dateReported = df2.groupby("date_reported").sum()
print(dateReported)

plt.figure(figsize=(10,8))
plt.bar(dateReported.index,dateReported["cumul_cases"],color = "Purple")
plt.xlabel("Date")
plt.ylabel("Cumulative Number of cases")
plt.title("Cumulative cases worldwide Datawise")
plt.show()


plt.figure(figsize=(10,8))
plt.bar(dateReported.index,dateReported["new_cases"],color = "Purple")
plt.xlabel("Date")
plt.ylabel("Number of cases")
plt.title("New cases worldwide Datawise")
plt.show()


plt.figure(figsize=(10,8))
plt.bar(dateReported.index,dateReported["new_deaths"],color = "Purple")
plt.xlabel("Date")
plt.ylabel("New number of deaths")
plt.title("New deaths worldwide Datawise")
plt.show()


plt.figure(figsize=(10,8))
plt.bar(dateReported.index,dateReported["cumul_deaths"],color = "Purple")
plt.xlabel("Date")
plt.ylabel("Cumulative Number of deaths")
plt.title("Cumulative deaths worldwide Datawise")
plt.show()


#UK

us = df2[df2["country"] == "United States of America"]
print(us.head())
USreported = us.groupby("date_reported").sum()


plt.figure(figsize=(8,8))
plt.bar(USreported.index,us["new_cases"],color = "Purple")
plt.xlabel("Date")
plt.ylabel("Number of cases")
plt.title("New cases US Datawise")
plt.show()


