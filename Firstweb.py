import streamlit as st

st.title("Heritage And Cultural Sites")
st.header("Explore rich Heritage And Cultural Sites Across India")
state=st.selectbox("Select A State",["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya"])
st.write(f"You Have Selected {state}")