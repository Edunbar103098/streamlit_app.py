import streamlit as st
import pandas as pd
import csv
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
st.sidebar.image('https://www.ctvnews.ca/polopoly_fs/1.2386301.1613680608!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')

st.sidebar.header('Boston Crime Statistics')
st.sidebar.subheader('By: Edward Dunbar')
page = st.sidebar.selectbox("Statistics", ["Gun Violence By District", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence By District":
  st.header('Gun Violence on the Rise During the Pandemic')
  st.video('https://youtu.be/-OuII9QsdkI')
  st.header('Gun Violence Vs Non Gun Violence, With District Crime Backdrop')
  st.subheader('Black: Non Gun Violence')
  st.subheader('Red: Gun Violence')
  st.image('https://i.pinimg.com/474x/84/37/cb/8437cb1783e45dffa657c3b11897b7aa.jpg')
  if st.button('See Code to Create this Geo Chart:'):
    link = '[Geopandas Chart](https://github.com/Edunbar103098/streamlit_app.py/blob/main/geopandas)'
    st.markdown(link, unsafe_allow_html=True)
  st.header('Total Crime By District')
  shooting = df["DISTRICT"].value_counts()
  st.write(shooting)
  st.header('Representation Of Crime by District')
  st.image('https://i.pinimg.com/474x/dc/8e/3a/dc8e3a106cb1688df7f07e900ad158c4.jpg') 
  if st.button('See Code to Create this Pie Chart:'):
    link = '[District Pie Chart](https://github.com/Edunbar103098/streamlit_app.py/blob/main/District%20Pie%20Chart)'
    st.markdown(link, unsafe_allow_html=True)          
elif page == "Deadly Days":
    st.header('Chance of Crime on Any Given Day in Boston')
    day=df["DAY_OF_WEEK"].value_counts()
    day_percentages=(day/70)
    st.write(day_percentages)
    st.image("https://i.pinimg.com/originals/5a/0a/66/5a0a667714f3604dc4b8ae85b1de25d5.jpg")
    hour=df["HOUR"].value_counts()
    st.bar_chart(hour)
    st.text("As seen by the data above, it is not the weekend when most crimes are committed, but the days leading up.")
    st.text("To keep yourself safe, here are some alternatives to going out on Thursdays and Fridays:")
    if st.button('Safe Option 1'):
      link1 = '[Netflix](https://www.netflix.com/)'  
      st.markdown(link1, unsafe_allow_html=True)  
    if st.button('Safe Option 2'): 
     link2 = '[Disney +](https://www.disneyplus.com/)'
      st.markdown(link, unsafe_allow_html=True) 
elif page == "Top Crimes":
    all = df["OFFENSE_DESCRIPTION"].value_counts()
    top_crime = all.head(n=10)
    st.write(top_crime)
    if st.button('Listen Live:'):
      link = '[Live Coverage of Boston Police Radio](https://www.broadcastify.com/listen/feed/35233)'
    if st.button('Go to The Boston Police Homepage'):
      link = '[City of Boston](https://www.boston.gov/departments/police)'  
      st.markdown(link, unsafe_allow_html=True)    

