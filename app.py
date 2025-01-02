import streamlit as st
import pickle
import pandas as pd



movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_list = movies['title'].values


st.title('Movie Recommender System')


selected_movie_name = st.selectbox('Choose a movie:', movies_list)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('MOVIES YOU MAY LIKE:')
    for movie in recommendations:
        st.write(movie)
