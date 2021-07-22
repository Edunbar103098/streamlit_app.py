"""
Name: Edward Dunbar
CS602: SN2
Data: Boston Crime Data
URL: https://share.streamlit.io/edunbar103098/streamlit_app.py/main
Description: This program desribes multiple analysis of aspects of crime in Boston. The first tab
discusses the prevalence of gun violence in crimes commited around the city, and how many involved a firearm.
I proceed to do a geopandas reverse geolocation to show an outline of the city itself, with districts as a backdrop.
In wake of the COVID-19 pandemic, gun violence rose in the city, so I provided a video for people to view about it.
My second page discusses the days in which crime is most prevalent in the city, and provides a graph to show hourly data of crime.
I then proceeded to make a comment about these days, and provide links to people of alternatives of going out and being involved in a crime.
My third page discusses the top crimes in the city, with the 50 most prevalent in an area chart. I proceed to present a chart of the top 3 crimes.
Below that is a tab that allows for users to see where these tabs occur in the city itself.
Finally, there is a link below that allows users to go directly to the BPD website for more information.
"""
import streamlit as st
import pandas as pd
import csv
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
st.sidebar.image('https://www.ctvnews.ca/polopoly_fs/1.2386301.1613680608!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')

st.sidebar.header('Boston Crime Statistics')
st.sidebar.subheader('By: Edward Dunbar')
if st.sidebar.button('Go to the source of this website):
  link = '[Website Source](https://github.com/Edunbar103098/streamlit_app.py/tree/main)'
  st.markdown(link, unsafe_allow_html=True)
page = st.sidebar.selectbox("Statistics", ["Gun Violence By District", "Deadly Days", "Top Crimes"]) 
#function I used to properly display the header for each section
def header(page):
  if page == "Gun Violence By District":
    st.header("Gun Violence By District")
  elif page == "Deadly Days":
    st.header("Deadly Days")
  elif page == "Top Crimes":
    st.header("Top Crimes")
#this is the massive if function I used to have multiple pages for my project  
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
  #this list creation was used to create a new dataframe with the labels of every district and number of crimes in that district, by combining my own list of 
  #districts, then making it into a dictionary from a list i created with the for loop present below, which provided the numbers.
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
    crimes= all.head(n=25)
    st.header("50 Most Prevalent Crimes in Boston")
    st.area_chart(crimes)
    st.header('Top 3 Crimes in Boston')
    st.write(top_crime)
    crime = st.selectbox("Pick a Crime", ['Investigate Person', 'Sick Assist', 'M/V - Leaving Scene- Property Damage'])
    #This provided the major if function to pull up the geopandas graphs by attack, and providing the link to the code used to make these charts.
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

