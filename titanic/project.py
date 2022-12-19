import pandas as pd
import math_functions as mf #come importare altri file creati da noi e usare funcioni esterne
import streamlit as st
import matplotlib.pyplot as plt


titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')

# print('is  3 prime?', mf.is_prime(3))
#dinamic web pages
st.header('Titanic Project')
st.subheader('predicting death')
#side bar
st.sidebar.subheader('Settings')
#we can hide something:
#se no anche senza sidebar e lo farà non a parte
if st.sidebar.checkbox('Display DataFrame'): 
    st.write('The DataFrame:')
    st.write(titanic_df)

if st.button('same thing'): #ma con questo non puoi tornare indietro
    st.write('The DataFrame:')
    st.write(titanic_df)

st.subheader('Plots')

#figure una accanto all'altra. come se fossero canvas
col_1, col_2 = st.columns(2)

with col_1:
    fig, ax = plt.subplots()
    titanic_df.Age.hist()
    st.write(fig)
    st.caption('Age description')

with col_2:
    fig, ax = plt.subplots()
    titanic_df.Sex.hist()
    st.write(fig)
    st.caption('Sex description')

#for the project: first try to print on the colab, then here 
#st.write e company non servono su colab perchè li stampa già

#with st.expander('Show model:'): tendina
    #...
