import streamlit as st
import webbrowser
page = st.selectbox("Choose your Tab", ["Gun Violence", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence":
  url = 'https://www.boston.gov/departments/police'
  if st.button('Go to The Boston Police Homepage'):
     webbrowser.open_new_tab(url)             
#elif page == "Deadly Days":
    # Display details of page 2
#elif page == "Top Crimes":


