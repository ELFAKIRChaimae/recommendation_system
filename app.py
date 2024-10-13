import pickle
import streamlit as st
import requests

st.header("Movies Recommndation System Using Machine Learning")
movies=pickle.load(open('recommendation/movie_list.pkl','rb'))
similarity=pickle.load(open('recommendation/similarity.pkl','rb'))
movie_list=movies['title'].values
selected_movie=st.selectbox('Select a movie ',movie_list)

def fetch_poster(movie_id):
   return 0




def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key= lambda x: x[1])
    recommended_movies_name=[]
    recommended_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movies_id
        recommended_movies_poster.append(fetch_poster(movie_id) )
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster
if st.button("Show Recommendation"):
  recommended_movies_name , recommended_movies_poster=recommend(selected_movie)
