import streamlit as st
import numpy as np
import pandas as pd
import joblib
movies=pd.read_pickle(r"F:\ML\project\Netflix_show_clustering\model\movies.pkl")
km=joblib.load(r'F:\ML\project\Netflix_show_clustering\model\model.joblib')
st.set_page_config(page_title='Netflix Movies recomendation',page_icon='🍿',layout='centered')
st.image(r"F:\ML\project\Netflix_show_clustering\Data\images\ChatGPT Image Aug 19, 2025, 10_27_09 PM.png")
st.title("🎬Movie Recomendation System")
st.divider()
df=pd.read_csv(r'F:\ML\project\Netflix_show_clustering\Data\netflix_titles.csv\netflix_titles.csv')

def recomendation(movie):
    cluster = movies.loc[movies['title'] == movie, 'cluster'].values[0]
    a = movies[movies['cluster'] == cluster][['title']]
    a=a.reset_index(drop=True)
    return a.sample(10)

with st.form(key='movie_form'):
    option=st.selectbox(
    "Select the movie to see related movies",
    df['title']
    )
    submit_button = st.form_submit_button(label="Get Recommendations")

if submit_button:
    st.write(recomendation(option))