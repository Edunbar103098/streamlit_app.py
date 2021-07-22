import streamlit as st
import pandas as pd
import csv
df = pd.read_csv('https://raw.githubusercontent.com/Edunbar103098/streamlit_app.py/16786d8ea3dd570730347dabbecf5c8cc367a8fe/boston.csv')
st.image('https://www.ctvnews.ca/polopoly_fs/1.2386301.1613680608!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')

st.header('Boston Crime Statistics')
st.subheader('By: Edward Dunbar')
page = st.selectbox("Statistics", ["Gun Violence By District", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence By District":
  st.header('Gun Violence Vs Non Gun Violence, With District Crime Backdrop')
  st.subheader('Black: Non Gun Violence')
  st.subheader('Red: Gun Violence')
  st.image('https://i.pinimg.com/474x/84/37/cb/8437cb1783e45dffa657c3b11897b7aa.jpg')
  if st.button('See Code to Create this Chart:'):
      st.text("#import pandas as pd"
              #import matplotlib.pyplot as plt'
# import descartes
# import geopandas as gpd
# from shapely.geometry import Point, Polygon'
# pd.set_option('display.max_rows',7000)'
#
# street_map = gpd.read_file(r'C:\Users\Dunbar_Edwa\PycharmProjects\Boston Project\City_of_Boston_Boundary.shp')'
# fig,ax = plt.subplots(figsize = (15,15))
# df = pd.read_csv("boston.csv")'
# crs = {'init': 'epsg:4326'}
# geometry = [Point(xy) for xy in zip(df['Long'], df['Lat'])]'
# geo_df = gpd.GeoDataFrame(df,
#                          crs = crs,
#                           geometry = geometry)'
# geo_df1 = geo_df.loc[geo_df["Lat"] > 0]'
#
#
# fig.ax = plt.subplots(figsize = (30,30))'
# street_map.plot(ax = ax, alpha = .4, color = 'grey')'
# geo_df1[geo_df1[SHOOTING] == 0].plot(ax = ax, markersize = 4, color = 'red', marker ='.', label = 'No shooting', )'
# geo_df1[geo_df1[SHOOTING] == 1].plot(ax = ax, markersize = 10, color = 'black', marker ='D', label = 'Shooting')'
# geo_df1[geo_df1[DISTRICT] == 'B2'].plot(ax = ax, markersize = 200, color = 'gray',alpha = .02,  label = 'No shooting', marker ='o')'
# geo_df1[geo_df1[DISTRICT] == 'B3'].plot(ax = ax, markersize = 200, color = 'gray',alpha = .02,  label = 'No shooting', marker ='o')'
# geo_df1[geo_df1[DISTRICT] == 'C11'].plot(ax = ax, markersize = 200, color = 'gray',alpha = .02,  label = 'No shooting', marker ='o')'
# geo_df1[geo_df1[DISTRICT] == 'D4'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o' )'
# geo_df1[geo_df1[DISTRICT] == 'A1'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1[DISTRICT] == 'C6'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1[DISTRICT] == 'D14'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1[DISTRICT] == 'E13'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1['DISTRICT'] == 'E18'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1['DISTRICT'] == 'A7'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1['DISTRICT'] == 'E5'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
# geo_df1[geo_df1['DISTRICT'] == 'A15'].plot(ax = ax, markersize = 200, color = 'gray', label = 'No shooting',alpha = .02, marker ='o'  )'
 "plt.show()")
  if st.button('Go to The Boston Police Homepage'):
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

