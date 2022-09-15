import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('Exploratory Data Analysis', 'Predict a Player'))

if navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()