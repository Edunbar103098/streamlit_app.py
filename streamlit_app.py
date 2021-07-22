import streamlit as st
import pandas as pd
import csv
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
st.sidebar.image('https://www.ctvnews.ca/polopoly_fs/1.2386301.1613680608!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')

st.sidebar.header('Boston Crime Statistics')
st.sidebar.subheader('By: Edward Dunbar')
page = st.sidebar.selectbox("Statistics", ["Gun Violence By District", "Deadly Days", "Top Crimes"]) 
def header(page):
  if page == "Gun Violence By District":
    st.header("Gun Violence By District")
  elif page == "Deadly Days":
    st.header("Deadly Days")
  elif page == "Top Crimes":
    st.header("Top Crimes")
  
if page == "Gun Violence By District":
  header(page)
  st.image('https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_15/3464361/210413-infrastructure-policing-2x1-cs.jpg')
  st.header('Gun Violence Vs Non Gun Violence, With District Crime Backdrop')
  st.subheader('Black Dots: Non Gun Violence')
  st.subheader('Red Dots: Gun Violence')
  st.image('https://i.pinimg.com/474x/84/37/cb/8437cb1783e45dffa657c3b11897b7aa.jpg')
  if st.button('Try This Code Yourself!'):
    link = '[Geopandas Chart](https://github.com/Edunbar103098/streamlit_app.py/blob/main/geopandas)'
    st.markdown(link, unsafe_allow_html=True)
  st.header('Total Crime By District')
  shooting = df["DISTRICT"].value_counts()
  list= []
  mylabels= ['B2','C11','D4','A1','B3','C6','D14','E13','E18','A7','E5','A15','External']
  for x in shooting:
     if x not in list:
         list.append(x)
  district_totals = {mylabels[i]: list[i] for i in range(len(mylabels))}
  districtdf= pd.DataFrame(district_totals.items(), columns=["District Name", "Total Crime in That District"])
  st.write(districtdf)
  st.header('Representation Of Crime by District')
  st.image('https://i.pinimg.com/474x/dc/8e/3a/dc8e3a106cb1688df7f07e900ad158c4.jpg')
  if st.button('See Code to Create this Pie Chart:'):
    link = '[District Pie Chart](https://github.com/Edunbar103098/streamlit_app.py/blob/main/District%20Pie%20Chart)'
    st.markdown(link, unsafe_allow_html=True)
  st.header('Gun Violence on the Rise During the Pandemic')
  st.video('https://youtu.be/-OuII9QsdkI')        
elif page == "Deadly Days":
    header(page)
    st.image("https://i.pinimg.com/originals/5a/0a/66/5a0a667714f3604dc4b8ae85b1de25d5.jpg")
    st.header('Chance of Crime on Any Given Day in Boston')
    day=df["DAY_OF_WEEK"].value_counts()
    day_percentages=(day/70)
    st.write(day_percentages)
    hour=df["HOUR"].value_counts()
    st.header('Crime by the Hour')
    st.bar_chart(hour)
    st.text("As seen by the data above, Thursday and Friday have high crime percentages")
    st.text("To keep yourself safe, here are some alternatives to going out on Thursdays and Fridays:")
    if st.button('Safe Option 1'):
      link1 = '[Netflix](https://www.netflix.com/)'  
      st.markdown(link1, unsafe_allow_html=True)  
    if st.button('Safe Option 2'): 
     link2 = '[Disney +](https://www.disneyplus.com/)'
     st.markdown(link2, unsafe_allow_html=True) 
elif page == "Top Crimes":
    header(page)
    st.image('https://massbaymovers.com/wp-content/uploads/2021/01/Boston-MA-Crime-Rate.jpg')
    all = df["OFFENSE_DESCRIPTION"].value_counts()
    top_crime = all.head(n=3)
    st.header('Top 3 Crimes in Boston')
    st.write(top_crime)
    crime = st.selectbox("Pick a Crime", ['Investigate Person', 'Sick Assist', 'M/V - Leaving Scene- Property Damage'])
    if crime == "Investigate Person":
        st.header('Locations of Investigating People in Boston')
        st.image('https://i.pinimg.com/564x/82/5a/a2/825aa2a607ef383b18661aeb3a98a405.jpg')
        if st.button('Try This Code Yourself!'):
          link = '[Investigation Chart](https://github.com/Edunbar103098/streamlit_app.py/blob/main/INVESTIGATE%20PERSON)'
          st.markdown(link, unsafe_allow_html=True)
    elif crime == 'Sick Assist':
        st.header('Locations of Sick Assists Crimes in Boston')
        st.image('https://i.pinimg.com/564x/b2/cc/33/b2cc33bc6f054aa9b522dfd5f751b940.jpg')
        if st.button('Try This Code Yourself!'):
          link = '[Sick Assist](https://github.com/Edunbar103098/streamlit_app.py/blob/main/SICK%20ASSIST)'
          st.markdown(link, unsafe_allow_html=True)
    elif crime == 'M/V - Leaving Scene- Property Damage':
        st.header('Locations of M/V Property Damage Crimes in Boston')
        st.image('https://i.pinimg.com/564x/33/fe/cc/33feccee0dce431d337cf4c35c157659.jpg')
        if st.button('Try This Code Yourself!'):
          link = '[M/V Damage](https://github.com/Edunbar103098/streamlit_app.py/blob/main/MV)'
          st.markdown(link, unsafe_allow_html=True)
    if st.button('Go to The Boston Police Homepage'):
      link = '[City of Boston](https://www.boston.gov/departments/police)'  
      st.markdown(link, unsafe_allow_html=True)    

