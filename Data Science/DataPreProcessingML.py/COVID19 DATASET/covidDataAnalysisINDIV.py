import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/covid_data.csv")

df = df[["Province_State","Country_Region","Confirmed","Recovered","Deaths","Active"]]
print(df.head())
print(df.isnull().sum())
df["Province_State"].fillna(value=" ",inplace = True) 
#replaces all the null values with spaces. Inplace - true means make the changes in the data set permanent 
#whenever there is a string column you can remnove missing values using fillna and usually give a space 
print(df.isnull().sum())

#Confirmed Cases US only

state_US = df[df["Country_Region"] == "US"] 
print(state_US.head())

confirmed_highest = state_US.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("States")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Red")
plt.title("Highest number of confirmed covid cases in US (states)")
plt.show()

total_deaths = state_US["Deaths"].sum()
total_recovered = state_US["Recovered"].sum()
total_confirmed = state_US["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') #%1.1% GIVES VALUE UP TO 1 DECIMAL
plt.title("Total confirmed, Deaths, and Recovered cases in US")
plt.show()


#INDIA


india = df[df["Country_Region"] == "India"] 
print(india.head())

confirmed_highest = india.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("States")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Brown")
plt.title("Highest number of confirmed covid cases in India (states)")
plt.show()

total_deaths2 = india["Deaths"].sum()
total_recovered2 = india["Recovered"].sum()
total_confirmed2 = india["Confirmed"].sum()

print("Total Deaths:",total_deaths2)
print("Total Recovered:",total_recovered2)
print("Total Confirmed:", total_confirmed2)

slices = [total_confirmed2,total_deaths2,total_recovered2]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') #%1.1% GIVES VALUE UP TO 1 DECIMAL
plt.title("Total confirmed, Deaths, and Recovered cases in India")
plt.show()



#UK

UK = df[df["Country_Region"] == "United Kingdom"] 
print(UK.head())

confirmed_highest = UK.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("States")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Orange")
plt.title("Highest number of confirmed covid cases in UK ")
plt.show()

total_deaths = UK["Deaths"].sum()
total_recovered = UK["Recovered"].sum()
total_confirmed = UK["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') #%1.1% GIVES VALUE UP TO 1 DECIMAL
plt.title("Total confirmed, Deaths, and Recovered cases in UK")
plt.show()


#GERMANY 
germany = df[df["Country_Region"] == "Germany"] 
print(germany.head())

confirmed_highest = germany.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("Cities")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Red")
plt.title("Highest number of confirmed covid cases in Germany ")
plt.show()

total_deaths = germany["Deaths"].sum()
total_recovered = germany["Recovered"].sum()
total_confirmed = germany["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%')
plt.title("Total confirmed, Deaths, and Recovered cases in Germany")
plt.show()


#ITALY 

italy = df[df["Country_Region"] == "Italy"] 
print(italy.head())

confirmed_highest = italy.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("Cities")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Green")
plt.title("Highest number of confirmed covid cases in Italy ")
plt.show()

total_deaths = italy["Deaths"].sum()
total_recovered = italy["Recovered"].sum()
total_confirmed = italy["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%')
plt.title("Total confirmed, Deaths, and Recovered cases in Italy")
plt.show()


#JAPAN
jap = df[df["Country_Region"] == "Japan"] 
print(jap.head())

confirmed_highest = jap.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("Cities")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Green")
plt.title("Highest number of confirmed covid cases in Japan ")
plt.show()

total_deaths = jap["Deaths"].sum()
total_recovered = jap["Recovered"].sum()
total_confirmed = jap["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') 
plt.title("Total confirmed, Deaths, and Recovered cases in Japan")
plt.show()

#SPAIN
spain = df[df["Country_Region"] == "Spain"] 
print(spain.head())

confirmed_highest = spain.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("Cities")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Blue")
plt.title("Highest number of confirmed covid cases in Spain ")
plt.show()

total_deaths = spain["Deaths"].sum()
total_recovered = spain["Recovered"].sum()
total_confirmed = spain["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') 
plt.title("Total confirmed, Deaths, and Recovered cases in Spain")
plt.show()


#SWEDEN
sweden = df[df["Country_Region"] == "Sweden"] 
print(sweden.head())

confirmed_highest = sweden.sort_values(by="Confirmed",ascending=False).head(10)
print(confirmed_highest[["Province_State","Confirmed"]])

plt.figure(figsize=(5,5))
plt.xlabel("Cities")
plt.ylabel("Confirmed Cases")
plt.bar(confirmed_highest["Province_State"],confirmed_highest["Confirmed"],color="Purple")
plt.title("Highest number of confirmed covid cases in Sweden ")
plt.show()

total_deaths = sweden["Deaths"].sum()
total_recovered = sweden["Recovered"].sum()
total_confirmed = sweden["Confirmed"].sum()

print("Total Deaths:",total_deaths)
print("Total Recovered:",total_recovered)
print("Total Confirmed:", total_confirmed)

slices = [total_confirmed,total_deaths,total_recovered]
labels = ["Confirmed","Deaths","Recovered"]
plt.pie(slices,labels=labels,autopct='%1.1f%%') 
plt.title("Total confirmed, Deaths, and Recovered cases in Sweden")
plt.show()


















