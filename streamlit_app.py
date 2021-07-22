
import streamlit as st
page = st.selectbox("Choose your Tab", ["Gun Violence", "Deadly Days", "Top Crimes"]) 
if page == "Gun Violence":
  if st.button('Go to The Boston Police Homepage'):
    link = '[City of Boston](https://www.boston.gov/departments/police)'
    st.markdown(link, unsafe_allow_html=True))           
#elif page == "Deadly Days":
    # Display details of page 2
#elif page == "Top Crimes":


