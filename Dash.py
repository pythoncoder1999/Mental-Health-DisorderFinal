from dash import dcc, html, Dash, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
sns.set()
import sqlite3
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from Mental_Health_Final import ETL

ETL()
from Machine_Learning import models
c = sqlite3.connect('MentalHealth')
cursor = c.cursor()
pd.set_option('display.max_column',None)
di = ["Anxiety Disorder", "Mood Disorder", "Attention Deficit Hyperactivity Disorder", "Post-traumatic Stress Disorder",
      "Autism Spectrum Disorder", "Eating Disorder", "Obsessive-Compulsive Disorder", "Addictive Disorder",
      "Substance Use Disorder", "Psychotic Disorder", "Personality Disorder", "Stress Response Syndromes",
      "Dissociative Disorder", "Sleeping Disorder", "Attention Deficit Disorder"]


di2 = ["Back-endDeveloper", "Front-endDeveloper", "ExecutiveLeadership","Supervisor/TeamLead","DevEvangelist/Advocate","DevOps/SysAdmin","Support","Designer","One-personshop","Sales","HR","Other"]
di3 = ["Afghanistan","Argentina","Australia","Austria","Bangladesh","Belgium","Bosnia and Herzegovina","Brazil","Bulgaria","Canada","Chile","Colombia","Czech Republic","Denmark","Ecuador","Estonia","Finland","France","Germany","Hungary","India","Iran","Ireland","Israel","Italy","Japan","Mexico","Netherlands","New Zealand","Norway","Pakistan","Poland", "Romania","Russia", "Slovakia","South Africa","Spain","Sweden","Switzerland","United Kingdom","United States of America", "Vietnam","Other"]

df = pd.read_sql(sql = "SELECT * FROM FinalDataset",con=c)
df2 = pd.read_sql(sql="SELECT * FROM GlobalData1", con=c)
df3 = pd.read_sql(sql="SELECT * FROM GlobalData2", con=c)

app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
#server = app.server
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Mental Health Disorder Prediction',style={'text-align':'center'})
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('"Hello!" This page is dedicated to prediction mental health related aspects! All data will be credited below. THIS IS NOT A FORMAL DIAGNOSIS, RATHER MACHINE LEARNED PREDICTIONS', style={'text-align':'center'})
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Predicting Mental Condition", style={'text-align':'center'}),
        ],width=12)

    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Number of employees in company"),
            employees:=dcc.Dropdown(options=(list(df['employees in company'].unique())), value='employees_',style={'font-family':'serif', 'text-align':'center','color':'black'})
        ],width=4),
        dbc.Col([
            html.H4("Part of tech based company?"),
            intech:=dcc.Dropdown(options=["True","False"], value='tech_',style={'color':'black'})
        ],width=4),
        dbc.Col([
            html.H4("Previous employers?"),
            previousemployers := dcc.Dropdown(options=(list(df['previous employers'].unique())), value='previous_employers_',style={'color':'black'})
        ],width=4),
    ]),

    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),

    dbc.Row([
        dbc.Col([
            html.H4("Work remotely"),
            work_remotely:=dcc.Dropdown(options=( ['Always', 'Never', 'Sometimes']), value='work_remotely_',style={'color':'black'}),
        ], width=4),
        dbc.Col([
            html.H4("Country"),
            country:=dcc.Dropdown(options=(list(di3)), value='country',style={'color':'black'}),
        ], width=4),
        dbc.Col([
            html.H4("Age? (- for any)"),
            age := dcc.Input(value='',style={'color':'black'})
        ], width=4),
    ]),


    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),


    dbc.Row([
        dbc.Col([
            html.H4("Gender?"),
            gender := dcc.Dropdown(options=(list(df['gender'].unique())), value='gender_',style={'color':'black'})
        ], width=4),
        dbc.Col([
            html.H4("Out of these, work positions you hold?"),
            work_positions := dcc.Dropdown(options=(list(di2)), value='work_positions_', multi=True,style={'color':'black'})
        ], width=4)
    ]),

    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
        ], width=4),
        dbc.Col([
            g := dcc.Markdown(children = '')
        ], width=4),
        dbc.Col([
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Predicting Number of Conditions",style={"text-align":"center"}),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([#_#
            html.H4("Number of employees in company"),
            employees2 := dcc.Dropdown(options=(list(df['employees in company'].unique())), value='employees_2',style={'color':'black'})
        ], width=4),
        dbc.Col([ #_#
            html.H4("Part of tech based company?"),
            intech2 := dcc.Dropdown(options=["True", "False"], value='tech_2',style={'color':'black'})
        ], width=4),
        dbc.Col([ #_#
            html.H4("Previous employers?"),
            previousemployers2 := dcc.Dropdown(options=(list(df['previous employers'].unique())),value='previous_employers_2',style={'color':'black'})
        ], width=4),
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Work remotely"),
            work_remotely2 := dcc.Dropdown(options=(['Always', 'Never', 'Sometimes']), value='work_remotely_2',style={'color':'black'}),
        ], width=4),
        dbc.Col([
            html.H4("Country"),
            country2 := dcc.Dropdown(options=(list(di3)), value='country_2',style={'color':'black'}),
        ], width=4),
        dbc.Col([
            html.H4("Family history of mental illness"),
            family_mental_illness := dcc.Dropdown(options=(['I don\'t know','No','Yes']), value='family_history_mental_illness',style={'color':'black'}),
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([ #_#
            html.H4("Age? (- for any)"),
            age2 := dcc.Input(value='',style={'color':'black'})
        ], width=4),
        dbc.Col([ #_#
            html.H4("Gender?"),
            gender2 := dcc.Dropdown(options=(list(df['gender'].unique())), value='gender_2',style={'color':'black'})
        ], width=4),
        dbc.Col([  #_#
            html.H4("Out of these, work positions you hold?"),
            work_positions2 := dcc.Dropdown(options=(list(di2)), value='work_positions_2', multi=True,style={'color':'black'})
        ], width=4),
        dbc.Col([
            html.H4("Mental illness in the past"),
            past_mental_illness := dcc.Dropdown(options=['Maybe','No','Yes'], value='past_mental_illness',style={'color':'black'}),
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
        ], width=4),
        dbc.Col([
            g2 := dcc.Markdown(children='')
        ], width=4),
        dbc.Col([
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Predicting Age based on mental health/other factors",style={'text-align':'center'}),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([  #_#
            html.H4("Which conditions do you have?"),
            conditions := dcc.Dropdown(options=list(di), value='conditions_', multi=True,style={'color':'black'})
        ], width=4),
        dbc.Col([
            html.H4("Number of employees in company"),
            employees3 := dcc.Dropdown(options=(list(df['employees in company'].unique())), value='employees_3',style={'color':'black'})
        ], width=4),
        dbc.Col([  # _#
            html.H4("Part of tech based company?"),
            intech3 := dcc.Dropdown(options=["True", "False"], value='tech_3',style={'color':'black'})
        ], width=4),
    ]),

    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([  # _#
            html.H4("Previous employers?"),
            previousemployers3 := dcc.Dropdown(options=(list(df['previous employers'].unique())),value='previous_employers_3',style={'color':'black'})
        ], width=4),
        dbc.Col([
            html.H4("Work remotely"),
            work_remotely3 := dcc.Dropdown(options=(['Always', 'Never', 'Sometimes']), value='work_remotely_3',style={'color':'black'}),
        ], width=4),
        dbc.Col([
            html.H4("Country"),
            country3 := dcc.Dropdown(options=(list(di3)), value='country_3',style={'color':'black'}),
        ], width=4),
    ]),

    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Family history of mental illness"),
            family_mental_illness2 := dcc.Dropdown(options=(['I don\'t know', 'No', 'Yes']),value='family_history_mental_illness2',style={'color':'black'}),
        ], width=3),
        dbc.Col([  # _#
            html.H4("Gender?"),
            gender3 := dcc.Dropdown(options=(list(df['gender'].unique())), value='gender_3',style={'color':'black'})
        ], width=3),
        dbc.Col([  # _#
            html.H4("Work positions you hold?"),
            work_positions3 := dcc.Dropdown(options=(list(di2)), value='work_positions_3', multi=True,style={'color':'black'})
        ], width=3),
        dbc.Col([
            html.H4("Mental illness in the past"),
            past_mental_illness2 := dcc.Dropdown(options=['Maybe', 'No', 'Yes'], value='past_mental_illness2',style={'color':'black'}),
        ], width=3)
    ]),

    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
        ], width=4),
        dbc.Col([
            g3 := dcc.Markdown(children='')
        ], width=4),
        dbc.Col([
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H4('Sources:')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('https://www.kaggle.com/datasets/thedevastator/osmi-mental-health-survey?select=OSMI-Survey-Data.csv')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('https://databank.worldbank.org/source/world-development-indicators')
        ], width=12)
    ]),

])


@app.callback(
    Output(component_id=g2, component_property='children'),
    Input(employees2, 'value'),
    Input(intech2, 'value'),
    Input(previousemployers2, 'value'),
    Input(work_remotely2, 'value'),
    Input(country2, 'value'),
    Input(family_mental_illness, 'value'),
    Input(age2, 'value'),
    Input(gender2, 'value'),
    Input(work_positions2, 'value'),
    Input(past_mental_illness, 'value')
)
def update_text(employees2,intech2,previousemployers2, work_remotely2,country2, family_mental_illness, age2, gender2, work_positions2, past_mental_illness):
    m_model1, m_model2, m_model3 = models()
    new = pd.DataFrame({
        'age':[0],'Work_Position_Back-endDeveloper':[0],'Work_Position_Front-endDeveloper':[0],'Work_Position_ExecutiveLeadership':[0],
        'Work_Position_Supervisor/TeamLead':[0],'Work_Position_DevEvangelist/Advocate':[0],'Work_Position_DevOps/SysAdmin':[0],'Work_Position_Support':[0],'Work_Position_Designer':[0],
        'Work_Position_One-personshop':[0],'Work_Position_Other':[0],'Work_Position_Sales':[0],'Work_Position_HR':[0], 'gender_Female':[0], 'gender_Male':[0], 'gender_Trans/Other':[0],'tech organization/company_False':[0],'tech organization/company_True':[0],
        'employees in company_1-5':[0],'employees in company_100-500':[0],'employees in company_26-100':[0],'employees in company_500-1000':[0],'employees in company_6-25':[0],'employees in company_More than 1000':[0],
        'previous employers_False':[0],'previous employers_True':[0],'family history of mental illness_I don\'t know':[0],
        'family history of mental illness_No':[0],'family history of mental illness_Yes':[0],'mental health disorder in the past_Maybe':[0],
        'mental health disorder in the past_No':[0],'mental health disorder in the past_Yes':[0], 'Country_Afghanistan':[0],'Country_Argentina':[0],'Country_Australia':[0],
        'Country_Austria':[0],'Country_Bangladesh':[0],'Country_Belgium':[0],'Country_Bosnia and Herzegovina':[0],'Country_Brazil':[0],'Country_Bulgaria':[0],'Country_Canada':[0],'Country_Chile':[0],
        'Country_Colombia':[0],'Country_Czech Republic':[0],'Country_Denmark':[0],'Country_Ecuador':[0],'Country_Estonia':[0],'Country_Finland':[0],'Country_France':[0],'Country_Germany':[0],
        'Country_Hungary':[0],'Country_India':[0],'Country_Iran':[0],'Country_Ireland':[0],'Country_Israel':[0],'Country_Italy':[0],'Country_Japan':[0],'Country_Mexico':[0],
        'Country_Netherlands':[0],'Country_New Zealand':[0],'Country_Norway':[0],'Country_Other':[0],'Country_Pakistan':[0],'Country_Poland':[0],'Country_Romania':[0],
        'Country_Russia':[0],'Country_Slovakia':[0],'Country_South Africa':[0],'Country_Spain':[0],'Country_Sweden':[0],'Country_Switzerland':[0],'Country_United Kingdom':[0],
        'Country_United States of America':[0],'Country_Vietnam':[0],'Work remotely_Always':[0],'Work remotely_Never':[0],'Work remotely_Sometimes':[0],'Different Professions_1':[0],
        'Different Professions_10':[0], 'Different Professions_2':[0],'Different Professions_3':[0],'Different Professions_4':[0],'Different Professions_5':[0],'Different Professions_6':[0],
        'Different Professions_7':[0],'Different Professions_8':[0],'Different Professions_9':[0],'Access to clean fuels and technologies for cooking (% of population)':[0],
        'Access to electricity (% of population)':[0],'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)':[0],
        'Adjusted net national income (current US$)':[0],'Adjusted net national income per capita (constant 2015 US$)':[0],'Population density (people per sq. km of land area)':[0],
        'Age dependency ratio (% of working-age population)':[0],'Urban population':[0],'Rural population':[0]
    })
    new['family history of mental illness_' + str(family_mental_illness)] = 1
    new['mental health disorder in the past_' + str(past_mental_illness)] = 1
    new['employees in company_' + str(employees2)] = 1
    new['tech organization/company_' + str(intech2)] = 1
    new['previous employers_' + str(previousemployers2)] = 1
    try:
        assert (int(age2))
        new['age'] = [int(age2)]
    except:
        return 'Prediction: Awaiting Valid Input'
    new['gender_' + str(gender2)] = 1
    sum = 0
    for i in work_positions2:
        new['Work_Position_' + str(i)] = 1
        sum += 1
    new['Different Professions_' + str(sum)] = 1
    new['Work remotely_' + str(work_remotely2)] = 1
    new['Country_' + str(country2)] = 1
    GlobalEntire = pd.merge(df2, df3, on="Country")
    GlobalEntire.loc[
        GlobalEntire['Country'] == 'Bulgaria', 'Access to clean fuels and technologies for cooking (% of population)'] = \
    GlobalEntire[GlobalEntire['Country'] != 'Bulgaria'][
        'Access to clean fuels and technologies for cooking (% of population)'].mean()
    for j in ['Access to clean fuels and technologies for cooking (% of population)',
              'Access to electricity (% of population)',
              'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)',
              'Adjusted net national income (current US$)',
              'Adjusted net national income per capita (constant 2015 US$)',
              'Population density (people per sq. km of land area)',
              'Age dependency ratio (% of working-age population)', 'Urban population', 'Rural population']:
        s = StandardScaler()
        s.fit(pd.DataFrame(GlobalEntire[j]))
        GlobalEntire[j] = (s.transform(pd.DataFrame(GlobalEntire[j])))
        new[j] = GlobalEntire[GlobalEntire['Country'] == country][j]

    return "Prediction:" + str(pd.Series(m_model2.predict(new))[0])


@app.callback(
    Output(component_id=g, component_property='children'),
    Input(employees, 'value'),
    Input(intech, 'value'),
    Input(previousemployers, 'value'),
    Input(age, 'value'),
    Input(gender, 'value'),
    Input(work_positions, 'value'),
    Input(work_remotely, 'value'),
    Input(country, 'value')

)
def update_text(employees,intech,previousemployers, age, gender, work_positions, work_remotely, country):
    m_model1, m_model2, m_model3 = models()
    new2 = pd.DataFrame({
        'age':[0],'Work_Position_Back-endDeveloper':[0],'Work_Position_Front-endDeveloper':[0],'Work_Position_ExecutiveLeadership':[0],
        'Work_Position_Supervisor/TeamLead':[0],'Work_Position_DevEvangelist/Advocate':[0],'Work_Position_DevOps/SysAdmin':[0],'Work_Position_Support':[0],'Work_Position_Designer':[0],
        'Work_Position_One-personshop':[0],'Work_Position_Other':[0],'Work_Position_Sales':[0],'Work_Position_HR':[0], 'gender_Female':[0], 'gender_Male':[0], 'gender_Trans/Other':[0],'tech organization/company_False':[0],'tech organization/company_True':[0],
        'employees in company_1-5':[0],'employees in company_100-500':[0],'employees in company_26-100':[0],'employees in company_500-1000':[0],'employees in company_6-25':[0],'employees in company_More than 1000':[0],
        'previous employers_False':[0],'previous employers_True':[0],'Country_Afghanistan':[0],'Country_Argentina':[0],'Country_Australia':[0],'Country_Austria':[0],'Country_Bangladesh':[0],
        'Country_Belgium':[0],'Country_Bosnia and Herzegovina':[0],'Country_Brazil':[0],'Country_Bulgaria':[0],'Country_Canada':[0],'Country_Chile':[0],'Country_Colombia':[0],
        'Country_Czech Republic':[0],'Country_Denmark':[0],'Country_Ecuador':[0],'Country_Estonia':[0],'Country_Finland':[0],'Country_France':[0],'Country_Germany':[0],
        'Country_Hungary':[0],'Country_India':[0],'Country_Iran':[0],'Country_Ireland':[0],'Country_Israel':[0],'Country_Italy':[0],'Country_Japan':[0],'Country_Mexico':[0],
        'Country_Netherlands':[0],'Country_New Zealand':[0],'Country_Norway':[0],'Country_Other':[0],'Country_Pakistan':[0],'Country_Poland':[0],'Country_Romania':[0],
        'Country_Russia':[0],'Country_Slovakia':[0],'Country_South Africa':[0],'Country_Spain':[0],'Country_Sweden':[0],'Country_Switzerland':[0],'Country_United Kingdom':[0],
        'Country_United States of America':[0],'Country_Vietnam':[0],'Work remotely_Always':[0],'Work remotely_Never':[0],'Work remotely_Sometimes':[0],'Different Professions_1':[0],
        'Different Professions_10':[0], 'Different Professions_2':[0],'Different Professions_3':[0],'Different Professions_4':[0],'Different Professions_5':[0],'Different Professions_6':[0],
        'Different Professions_7':[0],'Different Professions_8':[0],'Different Professions_9':[0],'Access to clean fuels and technologies for cooking (% of population)':[0],
        'Access to electricity (% of population)':[0],'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)':[0],
        'Adjusted net national income (current US$)':[0],'Adjusted net national income per capita (constant 2015 US$)':[0],'Population density (people per sq. km of land area)':[0],
        'Age dependency ratio (% of working-age population)':[0],'Urban population':[0],'Rural population':[0]
    })
    new2['employees in company_'+str(employees)] = 1
    new2['tech organization/company_'+str(intech)] = 1
    new2['previous employers_'+str(previousemployers)] = 1
    try:
        assert(int(age))
        new2['age'] = [int(age)]
    except:
        return 'Prediction: Awaiting Valid Input'
    new2['gender_'+str(gender)] = 1
    sum = 0
    for i in work_positions:
        new2['Work_Position_'+str(i)] = 1
        sum+=1
    new2['Different Professions_'+str(sum)]=1
    new2['Work remotely_'+str(work_remotely)]=1
    new2['Country_'+str(country)] = 1
    GlobalEntire = pd.merge(df2, df3, on="Country")
    GlobalEntire.loc[GlobalEntire['Country'] == 'Bulgaria', 'Access to clean fuels and technologies for cooking (% of population)'] = GlobalEntire[GlobalEntire['Country'] != 'Bulgaria']['Access to clean fuels and technologies for cooking (% of population)'].mean()
    for j in ['Access to clean fuels and technologies for cooking (% of population)','Access to electricity (% of population)','Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)','Adjusted net national income (current US$)','Adjusted net national income per capita (constant 2015 US$)','Population density (people per sq. km of land area)','Age dependency ratio (% of working-age population)','Urban population','Rural population']:
        s = StandardScaler()
        s.fit(pd.DataFrame(GlobalEntire[j]))
        GlobalEntire[j] = (s.transform(pd.DataFrame(GlobalEntire[j])))
        new2[j] = GlobalEntire[GlobalEntire['Country']==country][j]
    return "Prediction:" + str(pd.Series(m_model1.predict(new2)).map({2:'Yes', 1:'Maybe', 0:'No'})[0])


@app.callback(
    Output(component_id=g3, component_property='children'),
    Input(employees3, 'value'),
    Input(intech3, 'value'),
    Input(previousemployers3, 'value'),
    Input(work_remotely3, 'value'),
    Input(country3, 'value'),
    Input(family_mental_illness2, 'value'),
    Input(gender3, 'value'),
    Input(work_positions3, 'value'),
    Input(past_mental_illness2, 'value'),
    Input(conditions, 'value')

)
def update_text(employees3,intech3,previousemployers3, work_remotely3,country3, family_mental_illness2, gender3, work_positions3, past_mental_illness2, conditions):
    m_model1, m_model2, m_model3 = models()
    new3 = pd.DataFrame({'Work_Position_Back-endDeveloper':[0],'Condition_AnxietyDisorder':[0],
                        'Condition_MoodDisorder':[0],'Work_Position_Front-endDeveloper':[0], 'Condition_StressResponseSyndromes':[0],
                        'Work_Position_ExecutiveLeadership':[0],'Work_Position_Supervisor/TeamLead':[0],'Work_Position_DevEvangelist/Advocate':[0],
                        'Work_Position_DevOps/SysAdmin':[0],'Work_Position_Support':[0], 'Condition_SubstanceUseDisorder':[0],
                        'Work_Position_Designer':[0], 'Work_Position_One-personshop':[0],'Condition_AddictiveDisorder':[0],
                        'Condition_Obsessive-CompulsiveDisorder':[0],'Condition_EatingDisorder':[0], 'Work_Position_Other':[0],
                        'Condition_PersonalityDisorder':[0], 'Work_Position_Sales':[0],'Condition_AttentionDeficitHyperactivityDisorder':[0],
                        'Condition_PsychoticDisorder':[0], 'Condition_Post-traumaticStressDisorder':[0],'Condition_SomethingElse':[0],
                        'Condition_DissociativeDisorder':[0],'Work_Position_HR':[0], 'Condition_SleepingDisorder':[0],'Condition_AutismSpectrumDisorder':[0],
                        'gender_Female':[0], 'gender_Male':[0],'gender_Trans/Other':[0], 'tech organization/company_False':[0],'tech organization/company_True':[0],
                        'employees in company_1-5':[0],'employees in company_100-500':[0], 'employees in company_26-100':[0], 'employees in company_500-1000':[0],
                        'employees in company_6-25':[0],'employees in company_More than 1000':[0], 'previous employers_False':[0],
                        'previous employers_True':[0],'family history of mental illness_I don\'t know':[0],'family history of mental illness_No':[0],
                        'family history of mental illness_Yes':[0],'mental health disorder in the past_Maybe':[0],'mental health disorder in the past_No':[0],
                        'mental health disorder in the past_Yes':[0],'mental health disorder now_Maybe':[0], 'mental health disorder now_No':[0],
                        'mental health disorder now_Yes':[0],'Country_Afghanistan': [0], 'Country_Argentina':[0], 'Country_Australia':[0], 'Country_Austria':[0],
                        'Country_Bangladesh':[0], 'Country_Belgium':[0],'Country_Bosnia and Herzegovina':[0], 'Country_Brazil':[0], 'Country_Bulgaria':[0],
                        'Country_Canada':[0], 'Country_Chile':[0], 'Country_Colombia':[0],'Country_Czech Republic':[0], 'Country_Denmark':[0], 'Country_Ecuador':[0],
                        'Country_Estonia':[0], 'Country_Finland':[0], 'Country_France':[0],'Country_Germany':[0], 'Country_Hungary':[0], 'Country_India':[0], 'Country_Iran':[0],
                        'Country_Ireland':[0], 'Country_Israel':[0], 'Country_Italy':[0], 'Country_Japan':[0],'Country_Mexico':[0], 'Country_Netherlands':[0], 'Country_New Zealand':[0],
                        'Country_Norway':[0], 'Country_Other':[0], 'Country_Pakistan':[0], 'Country_Poland':[0],'Country_Romania':[0], 'Country_Russia':[0], 'Country_Slovakia':[0],
                        'Country_South Africa':[0], 'Country_Spain':[0], 'Country_Sweden':[0],'Country_Switzerland':[0], 'Country_United Kingdom':[0],
                        'Country_United States of America':[0], 'Country_Vietnam':[0],'Work remotely_Always':[0], 'Work remotely_Never':[0],'Work remotely_Sometimes':[0], 'Number of conditions_0':[0],
                        'Number of conditions_1':[0], 'Number of conditions_2':[0],'Number of conditions_3':[0], 'Number of conditions_4':[0],'Number of conditions_5':[0], 'Number of conditions_6':[0],
                        'Number of conditions_8':[0], 'Different Professions_1':[0],'Different Professions_10':[0], 'Different Professions_2':[0],
                        'Different Professions_3':[0], 'Different Professions_4':[0],'Different Professions_5':[0], 'Different Professions_6':[0],'Different Professions_7':[0], 'Different Professions_8':[0],
                        'Different Professions_9':[0]
    })
    new3['family history of mental illness_' + str(family_mental_illness2)] = 1
    new3['mental health disorder in the past_' + str(past_mental_illness2)] = 1
    new3['employees in company_' + str(employees3)] = 1
    new3['tech organization/company_' + str(intech3)] = 1
    new3['previous employers_' + str(previousemployers3)] = 1
    new3['gender_' + str(gender3)] = 1
    sum = 0
    for i in work_positions3:
        new3['Work_Position_' + str(i)] = 1
        sum += 1
    new3['Different Professions_' + str(sum)] = 1
    new3['Work remotely_' + str(work_remotely3)] = 1
    new3['Country_' + str(country3)] = 1
    sum2 = 0
    for y in conditions:
        new3['Condition_' + str(y).replace(" ","")] = 1
        sum2+=1
    new3['Number of conditions_' + str(sum2)] = 1
    return "Prediction:" + (str(round(pd.Series(m_model3.predict(new3))[0])))


#def update_text(text):
#    return text
if __name__ == '__main__':
    app.run_server(port = 8080)