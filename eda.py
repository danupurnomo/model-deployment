import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='FIFA 2022 - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('FIFA 2022 Player rating Prediction')

    # Membuat Sub Header
    st.subheader('EDA untuk Analisa Dataset FIFA 2022')

    # Membuat Deskripsi
    st.write('Page ini dibuat oleh *Danu Purnomo*')

    # Menambahkan Gambar
    image = Image.open('soccer.jpg')
    st.image(image, caption='FIFA 2022')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    Pada page kali ini, penulis akan melakukan eskplorasi sederhana.
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

    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram berdasarkan Input User')
    pilihan = st.selectbox('Pilih Column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Plotly Plot - ValueEUR dengan Overall')
    fig = px.scatter(data, x='ValueEUR', y='Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()