import numpy as np
from sklearn.preprocessing import StandardScaler
from Mental_Health_Final import ETL
import pandas as pd
import sqlite3
c = sqlite3.connect('MentalHealth')
cursor = c.cursor()
pd.set_option('display.max_columns',None)

ETL()

i = pd.read_sql(sql = "SELECT * FROM FinalDataset",con=c)
i.loc[i['Country'] == 'Bulgaria', 'Access to clean fuels and technologies for cooking (% of population)'] = i[i['Country'] != 'Bulgaria']['Access to clean fuels and technologies for cooking (% of population)'].mean()

i2 = pd.read_sql(sql = "SELECT * FROM FinalDataset WHERE [previous employers] = 0 ",con=c)
i3 = pd.read_sql(sql = "SELECT * FROM FinalDataset WHERE [family history of mental illness] = 'No'",con=c)

i4 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG(age) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i5 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG(age) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i7 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG(age) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i8 = pd.read_sql(sql = "SELECT [Number of conditions], AVG(age) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i9 = pd.read_sql(sql = "SELECT [Different Professions], AVG(age) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i10 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG([Access to clean fuels and technologies for cooking (% of population)]) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i11 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG([Access to clean fuels and technologies for cooking (% of population)]) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i13 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG([Access to clean fuels and technologies for cooking (% of population)]) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i14 = pd.read_sql(sql = "SELECT [Number of conditions], AVG([Access to clean fuels and technologies for cooking (% of population)]) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i15 = pd.read_sql(sql = "SELECT [Different Professions], AVG([Access to clean fuels and technologies for cooking (% of population)]) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i16 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG([Access to electricity (% of population)]) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i17 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG([Access to electricity (% of population)]) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i19 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG([Access to electricity (% of population)]) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i20 = pd.read_sql(sql = "SELECT [Number of conditions], AVG([Access to electricity (% of population)]) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i21 = pd.read_sql(sql = "SELECT [Different Professions], AVG([Access to electricity (% of population)]) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i22 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG([Population density (people per sq. km of land area)]) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i23 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG([Population density (people per sq. km of land area)]) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i25 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG([Population density (people per sq. km of land area)]) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i26 = pd.read_sql(sql = "SELECT [Number of conditions], AVG([Population density (people per sq. km of land area)]) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i27 = pd.read_sql(sql = "SELECT [Different Professions], AVG([Population density (people per sq. km of land area)]) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i28 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG([Age dependency ratio (% of working-age population)]) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i29 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG([Age dependency ratio (% of working-age population)]) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i31 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG([Age dependency ratio (% of working-age population)]) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i32 = pd.read_sql(sql = "SELECT [Number of conditions], AVG([Age dependency ratio (% of working-age population)]) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i33 = pd.read_sql(sql = "SELECT [Different Professions], AVG([Age dependency ratio (% of working-age population)]) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i34 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG(([Urban population])) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i35 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG(([Urban population])) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i37 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG(([Urban population])) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i38 = pd.read_sql(sql = "SELECT [Number of conditions], AVG(([Urban population])) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i39 = pd.read_sql(sql = "SELECT [Different Professions], AVG(([Urban population])) FROM FinalDataset GROUP BY [Different Professions]",con=c)
i40 = pd.read_sql(sql = "SELECT [mental health disorder in the past], AVG(([Rural population])) FROM FinalDataset GROUP BY [mental health disorder in the past]",con=c)
i41 = pd.read_sql(sql = "SELECT [mental health disorder now], AVG(([Rural population])) FROM FinalDataset GROUP BY [mental health disorder now]",con=c)
i43 = pd.read_sql(sql = "SELECT [sought treatment from mental health professional], AVG(([Rural population])) FROM FinalDataset GROUP BY [sought treatment from mental health professional]",con=c)
i44 = pd.read_sql(sql = "SELECT [Number of conditions], AVG(([Rural population])) FROM FinalDataset GROUP BY [Number of conditions]",con=c)
i45 = pd.read_sql(sql = "SELECT [Different Professions], AVG(([Rural population])) FROM FinalDataset GROUP BY [Different Professions]",con=c)
for k in (i4,i5,i7,i8,i9,i10,i11,i13,i14,i15,i16,i17,i19,i20,i21,i22,i23,i25,i26,i27,i28,i29,i31,i32,i33,i34,i35,i37,i38,i39,i40,i41,i43,i44,i45):
    print("_________________________________")
    print(k)

i.to_sql('FinalDataset', c, if_exists='replace', index=False)