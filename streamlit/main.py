import streamlit as st
import pandas as pd
import numpy


st.set_page_config(page_title="Bumble Final Project") # ponerlos mas grande: , layout="wide"

# Image

st.image('https://cdn.prod.website-files.com/63f6e52346a353ca1752970e/6440bf1a87dd9331e54024e7_study-cover-bumble.jpeg')


# Título principal centrado
st.markdown("<h1 style='text-align: center;'>Find your match</h1>", unsafe_allow_html=True)

# Import df

df = pd.read_csv("bumble.csv")

st.dataframe(df.head())

# Categories 
st.markdown("<h3 style='text-align: center;'>Choose how the person identifies</h3>", unsafe_allow_html=True)

st.text('nan: person who does not identify with any category.')

gen = st.selectbox("Choose a Gender",list(df.gender.unique()))


st.markdown("<h3 style='text-align: center;'>Choose Demographics</h3>", unsafe_allow_html=True)

ubi = st.selectbox("Select Location",list(df.location.unique()))

age = st.slider(label = "Select Range Age", min_value = 18, max_value = 74)

job = st.selectbox("Select Job",list(df.job.unique()))

edu = st.selectbox("Select Education",list(df.educationTag.unique()))


#height = st.number_input('Enter a Height')

st.markdown("<h3 style='text-align: center;'>Choose Family Plans</h3>", unsafe_allow_html=True)

inten = st.selectbox("Select Intention",list(df.intentions.unique()))

chil = st.selectbox("Select Children preference",list(df.childrens.unique()))

st.markdown("<h3 style='text-align: center;'>Choose lifestyle</h3>", unsafe_allow_html=True)

exer = st.selectbox("Select Exercise preferences",list(df.exercise.unique()))

drink = st.selectbox("Select Drinking preferences",list(df.drinking.unique()))

smoke = st.selectbox("Select Smoking preferences",list(df.smoking.unique()))

st.markdown("<h3 style='text-align: center;'>Choose Idiologias</h3>", unsafe_allow_html=True)

poli = st.selectbox("Select Political Idiology",list(df.politics.unique()))

reli = st.selectbox("Select Religion",list(df.religion.unique()))

zodiac = st.selectbox("Select Zodiac Sign",list(df.zodiacSign.unique()))


# Mostrar el resultado
st.markdown("<h2 style='text-align: center;'>Is there a match for you?</h2>", unsafe_allow_html=True)

if st.button('Filter Data'):
    
    filtered_df = df[
        ((df["gender"] == gen) | (df["gender"].isna())) &
        ((df["location"] == ubi) | (df["location"].isna())) &
        ((df["age"] == age) | (df["age"].isna())) &
        ((df["job"] == job) | (df["job"].isna())) &
        ((df["educationTag"] == edu) | (df["educationTag"].isna())) &
        ((df["intentions"] == inten) | (df["intentions"].isna())) &
        ((df["childrens"] == chil) | (df["childrens"].isna())) &
        ((df["exercise"] == exer) | (df["exercise"].isna())) &
        ((df["drinking"] == drink) | (df["drinking"].isna())) &
        ((df["smoking"] == smoke) | (df["smoking"].isna())) &
        ((df["politics"] == poli) | (df["politics"].isna())) &
        ((df["religion"] == reli) | (df["religion"].isna())) &
        ((df["zodiacSign"] == zodiac) | (df["zodiacSign"].isna()))
    ]
    
    st.write('Filtered DataFrame:', filtered_df)