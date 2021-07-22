from bokeh.models.widgets import Div
import streamlit as st
page = st.selectbox("Choose your Tab", ["Gun Violence", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence":
  if st.button('Go to The Boston Police Homepage'):
    js = "window.open('https://www.boston.gov/departments/police')"  # New tab or window
    js = "window.location.href = 'https://www.boston.gov/departments/police'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)           
#elif page == "Deadly Days":
    # Display details of page 2
#elif page == "Top Crimes":


