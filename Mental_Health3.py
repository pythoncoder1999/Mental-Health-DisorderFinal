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
    i = pd.read_csv("C://Users//madha//Downloads//P_Data_Extract_From_Population_estimates_and_projections//43ae7c02-c2a2-45a4-8673-fe7b6c5699ac_Data.csv")
def transform():
    global i
    #print(i)
    i = i[:len(i)-5]
    #print(i['Series Name'].value_counts())
    d = {}

    d['Country'] = pd.Series(i['Country Name'].unique())
    for f in list(i['Series Name'].unique()):
        d[f] = i[i['Series Name'] == f]['2017 [YR2017]'].dropna(ignore_index = True)
    i2 = pd.DataFrame(d)
    i = i2[:]
    def func(str):
        if str == '..':
            return -1
        return str
    i['Age dependency ratio (% of working-age population)'] = i['Age dependency ratio (% of working-age population)'].apply(func)
    i['Age dependency ratio (% of working-age population)'] = i['Age dependency ratio (% of working-age population)'].astype(float)

    i['Urban population'] = i['Urban population'].apply(func)
    i['Urban population'] = i['Urban population'].astype(float)

    i['Rural population'] = i['Rural population'].apply(func)
    i['Rural population'] = i['Rural population'].astype(float)

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
    i = i.iloc[:,:4]

def load():
    global i
    c = sqlite3.connect('MentalHealth')
    cursor = c.cursor()
    i.to_sql('GlobalData2', c, if_exists = 'replace', index = False)

def ETL():
    print("Database - Global Data - Part 2 (of 2) Part 2 Level 1")
    print("Please Wait for Process to Complete...")
    (time.sleep(2))
    extract()
    print("Extracted...")
    (time.sleep(2))
    transform()
    print("Transformed...")
    (time.sleep(2))
    load()
    print("Loaded! MentalHealth Database now stores ALL Global Data ")
    (time.sleep(2))