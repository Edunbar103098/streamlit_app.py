pip install plotly
import streamlit as st
import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
st.image('https://www.ctvnews.ca/polopoly_fs/1.2386301.1613680608!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')
st.header('Boston Crime Statistics')
st.subheader('By: Edward Dunbar')
page = st.selectbox("Statistics", ["Gun Violence By District", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence By District":
  if st.button('Go to The Boston Police Homepage'):
    fig= px.pie(df, values='NUMBER', names='DAY_OF_WEEK')
    st.plotly_chart(fig)
    link = '[City of Boston](https://www.boston.gov/departments/police)'
    st.markdown(link, unsafe_allow_html=True)           
elif page == "Deadly Days":
    day=df["DAY_OF_WEEK"].value_counts()
    st.write(day)
elif page == "Top Crimes":
    all = df["OFFENSE_DESCRIPTION"].value_counts()
    top_crime = all.head(n=10)
    st.write(top_crime)
    st.area_chart(top_crime)

