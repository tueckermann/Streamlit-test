import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

import os
path= os.getcwd() + '/Data/population.csv'
df = pd.read_csv(path)
# df = pd.read_csv('population.csv')

# a) Create a new Pandas data frame where the first column is the year and other 142 columns are 
# populations of all the countries in the data

df_pivot = df.pivot(index='year', columns='country', values='pop')
df_pivot.reset_index(inplace=True)

df_pivot.columns.name = None
df_pivot.rename_axis(None, axis=1, inplace=True)

# b) Use streamlit and create an interactive web graph where you can select the countries to be included in the population plot

columns = st.multiselect('Columns: ',df_pivot.columns)
st.line_chart(df_pivot,x = 'year',y = columns, y_label = 'Population', x_label = 'Year')

