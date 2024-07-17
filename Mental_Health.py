import sqlite3
import time
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.preprocessing import StandardScaler
i = pd.DataFrame()
def extract():
    global i
    i = pd.read_csv("C://Users//madha//Downloads//archive (52)//OSMI_Survey_Data.csv")

def transform():
    global i
    i = i.drop(['Question Group','ResponseID','Is your primary role within your company related to techIT','Have you been diagnosed with a mental health condition by a medical professional', 'If so, what conditions were you diagnosed with','What US state or territory do you live in','What country do you work in','What US state or territory do you work in','Question about speaking openly about mental health vs physical health','Are you selfemployed'],axis = 1)
    #print((i['Do you have a family history of mental illness'].value_counts()))
    def cleaning(str):
        return str.split("|")


    def sections(strl):
        di = ["Anxiety Disorder", "Mood Disorder", "Attention Deficit Hyperactivity Disorder", "Post-traumatic Stress Disorder", "Autism Spectrum Disorder", "Eating Disorder", "Obsessive-Compulsive Disorder", "Addictive Disorder", "Substance Use Disorder", "Psychotic Disorder", "Personality Disorder", "Stress Response Syndromes", "Dissociative Disorder", "Sleeping Disorder", "Attention Deficit Disorder"]
        l = set()
        for i in strl:
            if len((i).lstrip(" ")) > 0:
                p = re.compile(r'(.*)\(.*\)')
                r = re.search(p, i)
                if (r):
                    strtoanalyze = ""
                    if r.group(1)[len(r.group(1)) - 1] == " ":
                        strtoanalyze = (str(r.group(1)[:-1]).title())
                    else:
                        strtoanalyze = (str(r.group(1)).title())
                    if(strtoanalyze in di):
                        l.add(strtoanalyze)
                    elif(strtoanalyze == ''):
                        l.add('')
                    elif(len(strl)==1):
                        l.add("Something Else")
                else:
                    if (i in di):
                        l.add(i)
                    elif (i == ''):
                        l.add('')
                    elif(len(strl)==1):
                        l.add("Something Else")
        return l

    #has condition

    i['If yes, what conditions have you been diagnosed with'] = i['If yes, what conditions have you been diagnosed with'].fillna("")
    #i2 = i.copy()
    #i2['If yes, what conditions have you been diagnosed with'] = i2['If yes, what conditions have you been diagnosed with'].apply(cleaning)
    #i2['If yes, what conditions have you been diagnosed with'] = i2['If yes, what conditions have you been diagnosed with'].apply(sections)
    #i2['Number of conditions: '] = i['If yes, what conditions have you been diagnosed with'].apply(len)

    i['If yes, what conditions have you been diagnosed with'] = i['If yes, what conditions have you been diagnosed with'].apply(cleaning)
    i['If yes, what conditions have you been diagnosed with'] = i['If yes, what conditions have you been diagnosed with'].apply(sections)
    #print("This?")
    #print(i['If yes, what conditions have you been diagnosed with'].value_counts())
    #print(462/(60186-46662)) #<5%

    #maybe has condition
    i['If maybe, what conditions do you believe you have'] = i['If maybe, what conditions do you believe you have'].fillna("")
    #i3 = i.copy()
    #i3['If maybe, what conditions do you believe you have'] = i3['If maybe, what conditions do you believe you have'].apply(cleaning)
    #i3['If maybe, what conditions do you believe you have'] = i3['If maybe, what conditions do you believe you have'].apply(sections)
   # print(i3['If maybe, what conditions do you believe you have'].value_counts())
   # print(i3['If maybe, what conditions do you believe you have'].value_counts().sum())

    i['If maybe, what conditions do you believe you have'] = i['If maybe, what conditions do you believe you have'].apply(cleaning)
    i['If maybe, what conditions do you believe you have'] = i['If maybe, what conditions do you believe you have'].apply(sections)
   # print(294/(60186-46662)) #<5%

    #how many employees

    #primarily tech
    #print(i['Is your employer primarily a tech companyorganization'].value_counts())
    #print(i['Is your employer primarily a tech companyorganization'].isnull().sum())

    i['Is your employer primarily a tech companyorganization'] = i['Is your employer primarily a tech companyorganization'].fillna("NA")

    #previous employers
    #print(i['Do you have previous employers'].value_counts())
    #print(i['Do you have previous employers'].isnull().sum())

    #family history
    #print(i['Do you have a family history of mental illness'].value_counts())
    #print(i['Do you have a family history of mental illness'].isnull().sum())

    #past mental health
    #print(i['Have you had a mental health disorder in the past'].value_counts())
    #print(i['Have you had a mental health disorder in the past'].isnull().sum())



    #current mental health?
    #print(i['Do you currently have a mental health disorder'].value_counts())
    #print(i['Do you currently have a mental health disorder'].isnull().sum())


    #maybe conditions
    #print(i['If maybe, what conditions do you believe you have'].value_counts())
    #print(i['If maybe, what conditions do you believe you have'].isnull().sum())


    #seeked help
    #print(i['Have you ever sought treatment for a mental health issue from a mental health professional'].value_counts())
    #print(i['Have you ever sought treatment for a mental health issue from a mental health professional'].isnull().sum())

    def uni(row):
        row["Maybe or Has Mental Disorder"] = (row['If maybe, what conditions do you believe you have']) | (row['If yes, what conditions have you been diagnosed with'])
        return row
    i = i.apply(uni,axis = 1)
    i['Number of conditions: '] = i["Maybe or Has Mental Disorder"].apply(len)
    #print(i.columns)

    #Age
    #print(i['What is your age'].isnull().sum())
    #Gender
    #print(i['What is your gender '].isnull().sum())
    #Age Group Work
    #print(i['Age Group'].isnull().sum())
    #Country Work
    #print(i['What country do you live in'].value_counts())

    #pd.set_option('display.max_rows',None)
    #work position work
    i['Which of the following best describes your work position'] = i['Which of the following best describes your work position'].fillna("")
    i['Which of the following best describes your work position'] = (i['Which of the following best describes your work position'].apply(cleaning))
    #s = set()
    #for h in i['Which of the following best describes your work position']:
    #    for j in h:
    #        s.add(j)
    #print(s)

    #Response Work
    i['Response'] = (i['Response'].fillna("No Response"))

    #Removing any other null values remaining
    i = i.dropna()
    #print(i.isnull().sum())

    #Change columns
    pd.set_option('display.max_column',None)

    i.columns = ['index', 'employees in company', 'tech organization/company', 'previous employers','family history of mental illness','mental health disorder in the past','mental health disorder now', 'conditions', 'possible conditions', 'sought treatment from mental health professional', 'age','gender','Age Group','Country','Work position', 'Work remotely', 'Question', 'Response', 'Maybe or has mental disorder','Number of conditions']
    i['Different Professions'] = i['Work position'].apply(len)

    #Removing outliers
    #print(i.describe(include = 'all'))
    q = i['age'].quantile(0.97)
    i = i[i['age']<q]
    #sns.displot(i['age'])
    #sns.displot(i['Number of conditions'])


    #print(i.dtypes)
    #Change Data Types
    i ['age'] = i['age'].astype(int)
    #print(i)
    #plt.show()

    i["previous employers"] = i["previous employers"].astype(str)
    i["sought treatment from mental health professional"] = i["sought treatment from mental health professional"].astype(str)
    i["Number of conditions"] = i["Number of conditions"].astype(str)
    i["Different Professions"] = i["Different Professions"].astype(str)

    g = set()
    i = i.reset_index()
    for iq in range(len(i)):
        for jq in i['Maybe or has mental disorder'][iq]:
            jq = jq.replace(" ", "").replace("'","")
            if jq != "":
                if jq not in g:
                    i['Condition_' + jq] = [0.0] * len(i)
                    g.add(jq)
                i.loc[iq, "Condition_" + jq] += 1
        for k in i['Work position'][iq]:
            k = k.replace(" ", "").replace("'","")
            if k != "":
                if k not in g:
                    i['Work_Position_' + k] = [0.0] * len(i)
                    g.add(k)
                i.loc[iq, "Work_Position_" + k] += 1
    i=i.drop(['Work position', 'conditions','possible conditions', 'Maybe or has mental disorder'],axis = 1)
    i2 = i.copy()
    new = pd.concat([i2['gender'],i2['tech organization/company'],i2['employees in company'],i2['previous employers'],i2['family history of mental illness'],i2['mental health disorder in the past'], i2['mental health disorder now'],i2['Age Group'],i2['Country'],i2['Work remotely'],i2['Number of conditions'], i2['Different Professions']], axis = 1)
    i = pd.concat([i,pd.get_dummies(new)], axis = 1)

def load():
    global i
    c = sqlite3.connect('MentalHealth')
    cursor = c.cursor()
    i.to_sql('MentalHealthOSMI', c, if_exists = 'replace', index = False)

def ETL():
    print("Database - OSMI Mental Health - Part 1 Level 1")
    print("Please Wait for Process to Complete (1)")
    (time.sleep(2))
    extract()
    print("Extracted...")
    (time.sleep(2))
    transform()
    print("Transformed...")
    (time.sleep(2))
    load()
    print("Loaded! MentalHealth Database now stores OSMI Dataset")
    (time.sleep(2))