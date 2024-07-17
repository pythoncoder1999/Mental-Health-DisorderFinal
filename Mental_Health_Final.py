import time
import pandas as pd
import Mental_Health
import Mental_Health_2
import Mental_Health3
import sqlite3
i = pd.DataFrame()
i2 = pd.DataFrame()
i3 = pd.DataFrame()

def extract():
    global i
    global i2
    global i3
    Mental_Health.ETL()
    Mental_Health_2.ETL()
    Mental_Health3.ETL()

    c = sqlite3.connect('MentalHealth')
    cursor = c.cursor()
    i = pd.read_sql(sql = "SELECT * FROM MentalHealthOSMI",con=c)
    i2 = pd.read_sql(sql = "SELECT * FROM GlobalData1",con=c)
    i3 = pd.read_sql(sql = "SELECT * FROM GlobalData2",con=c)

def transform():
    global final_data
    final_data = pd.merge(pd.merge(i, i2, on="Country"),i3,on="Country")
    final_data = final_data.drop(['level_0'], axis = 1)

def load():
    global final_data
    c = sqlite3.connect('MentalHealth')
    cursor = c.cursor()
    final_data.to_sql('FinalDataset', c, if_exists='replace', index=False)

def ETL():
    print("Database - Final Database to be Loaded - Part 1 Level 2")
    print("Please Wait for Process to Complete...")
    (time.sleep(2))
    extract()
    print("Extracted...")
    (time.sleep(2))
    transform()
    print("Transformed...")
    (time.sleep(2))
    load()
    print("Loaded! MentalHealth Database now stores Final Database")
    (time.sleep(2))