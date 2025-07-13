#Data Analysis covid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DataPreProcessingML.py/covid_data.csv")
#print(df.head())

#print(df.isnull().sum()) ##checking how many missing values there are

df = df[["Province_State","Country_Region","Confirmed","Recovered","Deaths","Active"]]
print(df.head())
print(df.isnull().sum())
df["Province_State"].fillna(value=" ",inplace = True) #replaces all the null values with spaces. Inplace - true means make the changes in the data set permanent 
#whenever there is a string column you can remnove missing values using fillna and usually give a space 
print(df.isnull().sum())


#TOP 10 CONFIRMED
print("Top ten countries with most comfirmed cases")
top_ten_countries = df.sort_values(by="Confirmed",ascending=False).head(10) # sorting data by confirmed cases in descending order
print(top_ten_countries[["Country_Region","Confirmed"]])
print()

plt.figure(figsize=(5,5))
x = top_ten_countries["Country_Region"]
y = top_ten_countries["Confirmed"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Number of confirmed cases")
plt.title("Top 10 countries with confirmed cases")
plt.show()


#TOP 5 CONFIRMED
print("Top 5 countries with most confirmed cases")
top_five_countries = df.sort_values(by="Confirmed",ascending=False).head(5)
print(top_five_countries[["Country_Region","Confirmed"]])

plt.figure(figsize=(5,5))
x = top_five_countries["Country_Region"]
y = top_five_countries["Confirmed"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Number of confirmed cases")
plt.title("Top 5 countries with confirmed cases of covid")
plt.show()


#COUNTRIES WITH LEAST CONFIRMED CASES,, ERRONOUS
least_5_countries = df.sort_values(by="Confirmed",ascending=True).head(5) # sorting data by confirmed cases in descending order
print(least_5_countries[["Country_Region","Confirmed"]])

plt.figure(figsize=(5,5))
x = top_five_countries["Country_Region"]
y = top_five_countries["Confirmed"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Number of confirmed cases")
plt.title("Top 5 countries with least confirmed cases")
plt.show()



#---------------------------------------------------------------------------------------------------------------------------

#HW: ANALYSE ALL CATEGORIES WITH VISUALISATION 
# EG TOP 10 DEATHS, TOP 10 ACTIVE, LEAST DEATH, TOP 10 RECOVERED 

#TOP 10 COUNTRIES WITH HIGHEST DEATHS
print("Top 10 countries with most deaths from covid")
top_ten_countries_deaths = df.sort_values(by="Deaths",ascending=False).head(10) # sorting data by confirmed cases in descending order
print(top_ten_countries_deaths[["Country_Region","Deaths"]])
print()

plt.figure(figsize=(5,5))
x = top_ten_countries_deaths["Country_Region"]
y = top_ten_countries_deaths["Deaths"]
plt.bar(x,y,color="Blue")
plt.xlabel("Countries")
plt.ylabel("Number of deaths")
plt.title("Top 10 countries with highest death count")
plt.show()

#TOP 10 COUNTRIES WITH LEAST DEATHS --> ERRONOUS 
print("Top ten countries with least deaths from covid")
top_ten_countries_leastdeath = df.sort_values(by="Deaths",ascending=True).head(10) # sorting data by confirmed cases in descending order
print(top_ten_countries_leastdeath[["Country_Region","Deaths"]])
print()

plt.figure(figsize=(5,5))
x = top_ten_countries_leastdeath["Country_Region"]
y = top_ten_countries_leastdeath["Deaths"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Number of deaths")
plt.title("Top 10 countries with lowest death count")
plt.show()

#TOP 5 MOST ACTIVE COVID COUNTRIES
print("Top 5 most active countries")
top_five_countries_active = df.sort_values(by="Active",ascending=False).head(5)
print(top_five_countries_active[["Country_Region","Active"]])

plt.figure(figsize=(5,5))
x = top_five_countries_active["Country_Region"]
y = top_five_countries_active["Active"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Active Cases")
plt.title("Top 5 countries with active cases of COVID")
plt.show()

#TOP 5 RECOVERED COUNTRIES
print("Top 5 recovered countries")
top_five_countries_Rec = df.sort_values(by="Recovered",ascending=False).head(5)
print(top_five_countries_Rec[["Country_Region","Recovered"]])

plt.figure(figsize=(5,5))
x = top_five_countries_Rec["Country_Region"]
y = top_five_countries_Rec["Recovered"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Recovered Cases")
plt.title("Top 5 countries with most recovered patients")
plt.show()

#TOP 5 LEAST RECOVERED COUNTRIES --> ERRONOUS
print("Top 5 least recovered countries")
top_five_countries_leastRec = df.sort_values(by="Recovered",ascending=True).head(5)
print(top_five_countries_leastRec[["Country_Region","Recovered"]])

plt.figure(figsize=(5,5))
x = top_five_countries_leastRec["Country_Region"]
y = top_five_countries_leastRec["Recovered"]
plt.bar(x,y,color="Red")
plt.xlabel("Countries")
plt.ylabel("Recovered Cases")
plt.title("Top 5 countries with least recovered patients")
plt.show()