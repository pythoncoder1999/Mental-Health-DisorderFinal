import sqlite3
import time
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

sns.set()
i = pd.DataFrame()
def extract():
    global i
    i = pd.read_csv("C://Users//madha//Downloads//P_Data_Extract_From_World_Development_Indicators//4d6be555-a7ae-4aed-9e21-8d3683e47eee_Data.csv")
def transform():
    global i
    pd.set_option('display.max_column',None)
    i = i[:1596]

    i2 = pd.DataFrame({
        "Country": pd.Series(i['Country Name'].unique()),
        "Access to clean fuels and technologies for cooking (% of population)": i[i['Series Name'] == 'Access to clean fuels and technologies for cooking (% of population)']['2017 [YR2017]'].dropna(ignore_index = True),
        "Access to electricity (% of population)":i[i['Series Name']=='Access to electricity (% of population)']['2017 [YR2017]'].dropna(ignore_index = True),
        "Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)": i[i['Series Name'] == 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)']['2017 [YR2017]'].dropna(ignore_index = True),
        "Adjusted net national income (current US$)":i[i['Series Name'] == 'Adjusted net national income (current US$)']['2017 [YR2017]'].dropna(ignore_index = True),
        "Adjusted net national income per capita (constant 2015 US$)":i[i['Series Name'] == 'Adjusted net national income per capita (constant 2015 US$)']['2017 [YR2017]'].dropna(ignore_index = True),
        "Population density (people per sq. km of land area)":i[i['Series Name'] == 'Population density (people per sq. km of land area)']['2017 [YR2017]'].dropna(ignore_index = True)
    })
    i = i2[:]
    def func(str):
        if str == '..':
            return -1
        return str
    i.loc[i['Country']=='Afghanistan','Adjusted net national income per capita (constant 2015 US$)'] = 550.241360031403
    i.loc[i['Country'] == 'Australia', 'Adjusted net national income per capita (constant 2015 US$)'] = 44512.5960291842
    i['Access to clean fuels and technologies for cooking (% of population)'] = i['Access to clean fuels and technologies for cooking (% of population)'].apply(func)
    i['Access to clean fuels and technologies for cooking (% of population)'] = i['Access to clean fuels and technologies for cooking (% of population)'].astype(float)

    i['Access to electricity (% of population)'] = i['Access to electricity (% of population)'].apply(func)
    i['Access to electricity (% of population)'] = i['Access to electricity (% of population)'].astype(float)

    i['Adjusted net national income (current US$)'] = i['Adjusted net national income (current US$)'].apply(func)
    i['Adjusted net national income (current US$)'] = i['Adjusted net national income (current US$)'].astype(float)

    i['Adjusted net national income per capita (constant 2015 US$)'] = i['Adjusted net national income per capita (constant 2015 US$)'].apply(func)
    i['Adjusted net national income per capita (constant 2015 US$)'] = i['Adjusted net national income per capita (constant 2015 US$)'].astype(float)

    i['Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'] = i['Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'].apply(func)
    i['Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'] = i['Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'].astype(float)

    i['Population density (people per sq. km of land area)'] = i['Population density (people per sq. km of land area)'].apply(func)
    i['Population density (people per sq. km of land area)'] = i['Population density (people per sq. km of land area)'].astype(float)

    def changescountry(co):
        if(co == 'United States'):
            return 'United States of America'
        if(co == 'Russian Federation'):
            return 'Russia'
        if(co == 'Czechia'):
            return 'Czech Republic'
        if(co =='Venezuela, RB'):
            return 'Venezuela'
        if(co == 'Brunei Darussalam'):
            return 'Brunei'
        if(co == 'Viet Nam'):
            return 'Vietnam'
        if(co == 'Slovak Republic'):
            return 'Slovakia'
        return co
    i['Country'] = i['Country'].apply(changescountry)

def load():
    global i
    c = sqlite3.connect('MentalHealth')
    cursor = c.cursor()
    i.to_sql('GlobalData1', c, if_exists = 'replace', index = False)

def ETL():
    print("Database - Global Data - Part 1 (of 2) Part 2 Level 1")
    print("Please Wait for Process to Complete...")
    (time.sleep(2))
    extract()
    print("Extracted...")
    (time.sleep(2))
    transform()
    print("Transformed...")
    (time.sleep(2))
    load()
    print("Loaded! MentalHealth Database now stores Global Data Part 1")
    (time.sleep(2))