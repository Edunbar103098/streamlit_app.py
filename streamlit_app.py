import csv
import pandas as pd
import matplotlib.pyplot as plt
import reverse_geocode as rg
import pprint
import streamlit as st
df = pd.read_csv("boston.csv")
#street_map = gdp.read_file(r'C:\Users\Dunbar_Edwa\PycharmProjects\Boston Project\City_of_Boston_Boundary.shp')
df = pd.read_csv("boston.csv")
all = df["OFFENSE_DESCRIPTION"].value_counts()
crime_percentages= (all / (df["OFFENSE_DESCRIPTION"].count()))
street=df["STREET"].value_counts()
street_percentages=(street/ (df["STREET"].count()))
street_top = street_percentages.head(n= 10)
all = df["OFFENSE_DESCRIPTION"].value_counts()
top_crime = all.head(n=10)
chances_of_crime= (top_crime / (df["OFFENSE_DESCRIPTION"].count()))

# df1 = df.drop(columns = ['INCIDENT_NUMBER','OFFENSE_CODE','OFFENSE_CODE_GROUP','OFFENSE_DESCRIPTION','DISTRICT','REPORTING_AREA','SHOOTING','OCCURRED_ON_DATE','YEAR','MONTH','DAY_OF_WEEK','HOUR','UCR_PART','Location'])
day=df["DAY_OF_WEEK"].value_counts()
day_percentages=(day/ (df["DAY_OF_WEEK"].count()))
st.pie(top_crime)
