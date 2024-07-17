import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
sns.set()
import sqlite3
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

c = sqlite3.connect('MentalHealth')
cursor = c.cursor()
pd.set_option('display.max_column',None)

df = pd.read_sql(sql = "SELECT * FROM FinalDataset",con=c)


for k in df.columns:
    if k == 'Access to clean fuels and technologies for cooking (% of population)' or k == 'Access to electricity (% of population)' or k== 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)' or k=='Adjusted net national income (current US$)' or k == 'Adjusted net national income per capita (constant 2015 US$)' or k=='Population density (people per sq. km of land area)' or k=='Age dependency ratio (% of working-age population)' or k == 'Urban population' or k == 'Rural Population': #k == 'age' or
        s = StandardScaler()
        s.fit(pd.DataFrame(df[k]))
        df[k] = (s.transform(pd.DataFrame(df[k])))

df2 = df.copy()
df2['mental health disorder now'] = df2['mental health disorder now'].map({'Yes':2, 'Maybe':1, 'No':0})
c = [x for x in df2.columns if type(df2[x][0]) == str]
df2 = df2.drop(c,axis = 1)

todrop=['index', 'tech organization/company'] + [x for x in df2.columns if x.startswith('Number of conditions_')] + [x for x in df2.columns if x.startswith('Age Group')] + [x for x in df2.columns if x.startswith('mental health disorder now')] + [x for x in df2.columns if x.startswith('mental health disorder in the past')] +[x for x in df2.columns if x.startswith('Condition_')] + [x for x in df2.columns if x.startswith('family history of mental illness_')]
x = pd.DataFrame(df2.drop(todrop, axis=1))
y = pd.DataFrame(df2['mental health disorder now'])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
r = RandomForestClassifier(max_depth = 20,min_samples_split=10)
(r.fit(x_train,y_train))
plt.show()
pred = r.predict(x_test)
print(r.score(x_test,y_test))


df4 = df.copy()
df4 = df4[df4["mental health disorder now"]=='Yes'].copy()
df4 = df4[df4['Number of conditions'] != '0']
c2 = ["Number of conditions", "index", 'tech organization/company']+[x for x in df4.columns if x.startswith('mental health disorder now_')] + [x for x in df4.columns if x.startswith("Age Group_")]+[x for x in df4.columns if type(df4[x][42]) == str] + [x for x in df4.columns if x.startswith('Condition_')] + [x for x in df4.columns if x.startswith("Number of conditions_")]
x = pd.DataFrame(df4.drop(c2, axis=1))
y = pd.DataFrame(df4['Number of conditions'])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

n2 = RandomForestClassifier(max_depth=15, min_samples_split=10)
(n2.fit(x_train,y_train))
pred = n2.predict(x_test)
print(n2.score(x_test,y_test))



df5 = df.copy()
c3 = [x for x in df5.columns if type(df4[x][42]) == str]
k = RandomForestRegressor()
x = pd.DataFrame(df5.drop(['index','tech organization/company'] + [x for x in df5.columns if x.startswith('Age Group')] + c3 + ['age','Access to clean fuels and technologies for cooking (% of population)','Access to electricity (% of population)','Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)','Adjusted net national income (current US$)','Adjusted net national income per capita (constant 2015 US$)','Population density (people per sq. km of land area)','Age dependency ratio (% of working-age population)','Urban population', 'Rural population'],axis = 1))
y = pd.DataFrame(df5['age'])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

n = RandomForestRegressor(max_depth=20, min_samples_split=10)
(n.fit(x_train,y_train))
p = n.predict(x_test)
print(n.score(x_test,y_test))


def models():
    return (r, n2, n)