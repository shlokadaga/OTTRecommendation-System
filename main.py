import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
st.sidebar.title('SIDEBAR')
ott=st.sidebar.selectbox('OTT Platform',['NETFLIX','PRIME VIDEO','HOTSTAR'])

def netflix():
       st.sidebar.image(r'netflix.jpg', width=300)
       st.title('NETFLIX')
       st.write("Netflix is a subscription-based streaming service that allows our members to watch TV shows and movies without commercials on an internet-connected device. You can also download TV shows and movies to your device and watch without an internet connection. If youre already a member and would like to learn more about using Netflix, visit www.netflix.com")

       netflix_data = pd.read_csv(r'C:\Users\dagas\OneDrive\Desktop\BE Project Report\Dataset\netflixData.csv')
       df_netflix = netflix_data.assign(names=netflix_data['Genres'].str.split(",")).explode('names')
       unique_genre=df_netflix['names'].unique()
       df_netflix['IMDB'] = df_netflix['Imdb Score'].str.split("/")

       col1, col2=st.columns(2)
       content_type = st.radio('Content Type', ['Movie', 'TV Show'])
       df_netflix_chart=df_netflix[df_netflix['Content Type']==content_type]
       total_genre=df_netflix_chart.groupby(by='names')['names'].count().sort_values(ascending=False).head(25)
       fig1=px.bar(total_genre,y='names')
       fig1.update_layout(yaxis_title='Total',xaxis_title='Genre',height=500, width=1100)
       st.plotly_chart(fig1)


       st.sidebar.text(' ')
       release_unique=df_netflix['Release Date'].unique()
       sidebarslider=st.sidebar.slider('Select Release Year',2009,2021)
       df2=netflix_data[netflix_data['Release Date']==sidebarslider]
       df2=df2[df2['Content Type']==content_type]

       df2=df2.sort_values(by='Imdb Score', ascending=False)[['Title','Imdb Score']]
       df2 = df2.reset_index()
       st.sidebar.dataframe(df2.head(5))
       st.markdown("""
       <style>
       body {
         background-color: #3B5992; 
       }
       </style>
           """, unsafe_allow_html=True)




       st.write(' ')
       option=st.selectbox('Select Your Genre',unique_genre)

       st.write(' ')
       def genre_recommend(genre):
              genre_rec = df_netflix[df_netflix['names'] == genre]
              genre_rec = genre_rec.sort_values(by='Imdb Score', ascending=False)
              genre_rec = genre_rec.reset_index().head(10)
              st.dataframe(genre_rec[['Title','Imdb Score','Production Country','Duration']])


       genre_recommend(option)

       age = st.slider('Select your age', 1, 100)

       gender = st.radio('Select your Gender', ['Male', 'Female', 'Other'])
def primevideo():
       s1,s2,s3,s4=st.columns(4)
       st.sidebar.image(r'primevideo.jpg', width=300)

def hotstar():
       st.sidebar.image(r'hotstar.jpg', width=300)


if ott=='NETFLIX':
       netflix()
elif ott=='PRIME VIDEO':
       primevideo()
elif ott=='HOTSTAR':
       hotstar()