import altair as alt
import streamlit as st
import pandas as pd
import csv
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
page = st.selectbox("Choose your Tab", ["Gun Violence", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence":
  if st.button('Go to The Boston Police Homepage'):
    st.image('https://github.com/Edunbar103098/streamlit_app.py/blob/main/Shootings.JPG')
    link = '[City of Boston](https://www.boston.gov/departments/police)'
    st.markdown(link, unsafe_allow_html=True)           
elif page == "Deadly Days":
    day=df["DAY_OF_WEEK"].value_counts()
    st.write(day)
elif page == "Top Crimes":
    all = df["OFFENSE_DESCRIPTION"].value_counts()
    top_crime = all.head(n=10)
    st.write(top_crime)

