#!/usr/bin/env python
# coding: utf-8

#import data libraries
import pandas as pd
import plotly
import numpy as np
import seaborn as sns
import os
import random

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

#expand view of this workbook to display more columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#create a user/patient column and a days since covid started and an is_dead column
patient = list(np.random.randint(0,150000,size=150000))
days_since_covid = list(np.random.randint(0,150,size=150000))
is_dead = list(np.random.randint(0,2,size=150000))


#create fake data whole numbers
df = pd.DataFrame(np.random.randint(0,150000,size=(150000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))

#add patient and days columns to the dataframes
df['patient'] = patient
df['days_since_covid'] = days_since_covid
df['is_dead'] = is_dead

#reorder the columns
df.columns = ['patient','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','days_since_covid','is_dead']

#easily able to retitle the columns but i don't even know what the columns would be named

#print out what this dataframe (table, database, data, csv, spreadsheet whatever you want to call it) looks like:
print("The size of this dataframe is (rows, columns): ", df.shape)
print(df.head(20))

#create fake data with decimals
df1 = pd.DataFrame(np.random.rand(150000, 17) , columns=list('ABCDEFGHIJKLMNOPQ'))

#add it to the dataframes
df1['patient'] = patient
df1['days_since_covid'] = days_since_covid

#reorder the columns
df1.columns = ['patient','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','days_since_covid']

#easily able to retitle the columns but i don't even know what the columns would be named

print("The size of this dataframe is (rows, columns): ", df1.shape)
print(df1.head(20))

#I'll even make it look pretty
df1.head(20).style.background_gradient(cmap='Blues')


#create fake data whole numbers with numbers that increase
number_1 = pd.DataFrame(np.random.randint(0,10000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_2 = pd.DataFrame(np.random.randint(5000,15000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_3 = pd.DataFrame(np.random.randint(10000,20000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_4 = pd.DataFrame(np.random.randint(20000,40000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_5 = pd.DataFrame(np.random.randint(25000,45000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_6 = pd.DataFrame(np.random.randint(40000,50000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_7 = pd.DataFrame(np.random.randint(50000,70000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_8 = pd.DataFrame(np.random.randint(60000,75000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
number_9 = pd.DataFrame(np.random.randint(80000,100000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))
# number_10 = pd.DataFrame(np.random.randint(100000,150000,size=(15000, 17)), columns=list('ABCDEFGHIJKLMNOPQ'))

#join all dataframes together
covid_df = pd.concat([number_1, number_2, number_3, number_4, number_5, number_5, number_6, number_7, number_8, number_9])
covid_df

#show the average of column a over time
covid_df['MA'] = covid_df.rolling(window=5)['A'].mean()

#add it to the dataframes
covid_df['patient'] = patient
covid_df['days_since_covid'] = days_since_covid

#reorder the columns
# covid_df.columns = ['patient','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','MA']

#easily able to retitle the columns but i don't even know what the columns would be named

print("The size of this dataframe is (rows, columns): ", covid_df.shape)
print(covid_df.head(20))

#Fake plot it
x = np.arange(10)
fig = go.Figure(data=go.Scatter(x=x, y=x**2))
fig.update_layout(title_text="Covid Deaths - Hydroxychloroquine Trials")
fig.update_xaxes(title_text='Days in Trial')
fig.update_yaxes(title_text='Deaths per Day')
fig.show()
