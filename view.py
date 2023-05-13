import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    dis = similarity[movie_index]
    top5 = sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in top5:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
option = st.selectbox('Which movies you want to search?',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
    


