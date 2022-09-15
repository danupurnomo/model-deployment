import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Membuat Ttile
    st.title('Exploratory Data Analysis - EDA')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisa Dataset FIFA 2022')

    # Membuat Deskripsi
    st.write('Page ini dibuat oleh *Danu Purnomo*')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana.
    Dataset yang digunakan adalah dataset FIFA 2022.
    Dataset ini berasal dari web sofifa.com.
    '''

    # Show DataFrame
    data = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/FSDS_Guidelines/master/p1/v3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(data)

    # Membuat BarPlot
    st.write('#### Plot AttackingWorkRate')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='AttackingWorkRate', data=data)
    st.pyplot(fig)

    # Membuat Histogram
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data['Overall'], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Histogram berdasarkan Input User
    st.write('#### Histogram berdasarkan Input User')
    opt = st.selectbox('Pilih Column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[opt], bins=30, kde=True)
    st.pyplot(fig)

if __name__ == '__main__':
    run()