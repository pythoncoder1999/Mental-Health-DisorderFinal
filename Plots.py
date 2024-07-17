import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import sqlite3
import scipy.stats
c = sqlite3.connect('MentalHealth')
cursor = c.cursor()
pd.set_option('display.max_column',None)

df = pd.read_sql(sql = "SELECT * FROM FinalDataset",con=c)

print(df)
print(df.describe())
sns.countplot(data = df['employees in company'])
sns.countplot(data = df['mental health disorder in the past'])
sns.countplot(data = df['mental health disorder now'])
sns.countplot(data = df['previous employers'])
sns.boxplot(x="Number of conditions", y="family history of mental illness", data = df)
sns.boxplot(x="Number of conditions", y="gender", data = df)
sns.jointplot(x="age", y="Number of conditions", data = df)

sns.countplot(data = df['family history of mental illness'])
df['sought treatment from mental health professional'].value_counts().plot.pie(radius=1, figsize = (10,8))
df['gender'].value_counts().plot.pie()
df['Age Group'].value_counts().plot.pie()
df['Country'].value_counts().plot.pie()

df['conditions'].value_counts().plot.pie()
df['Number of conditions'].value_counts().plot.pie()

sns.jointplot(x="age", y="Different Professions", data = df)
sns.jointplot(x="Access to clean fuels and technologies for cooking (% of population)", y="Different Professions", data = df)
sns.jointplot(x="Access to clean fuels and technologies for cooking (% of population)", y="Number of conditions", data = df)
sns.jointplot(x="Adjusted net national income (current US$)", y="Number of conditions", data = df)
sns.jointplot(x="Adjusted net national income (current US$)", y="Different Professions", data = df)


sns.boxplot(x="mental health disorder now", y="age", data = df)
sns.boxplot(x="mental health disorder now", y="Adjusted net national income (current US$)", data = df)
sns.boxplot(x="age", y="Number of conditions", data = df)

sns.boxplot(x="sought treatment from mental health professional", y="age", data = df)
sns.boxplot(x="sought treatment from mental health professional", y="Adjusted net national income (current US$)", data = df)
plt.show()