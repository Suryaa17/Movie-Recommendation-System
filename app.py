import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System")
st.subheader("This model is Created by SURYAA NT")
st.markdown("Type or Select a movie present in the select box to get recommendations")
st.markdown("This ML model is working based on Cosine Similarity")

movies = pickle.load(open("artifacts/movie_list.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))

def poster_fetch(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies_name = []
    recommend_movies_poster = []
    for i in distance[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies_poster.append(poster_fetch(movie_id))
        recommend_movies_name.append(movies.iloc[i[0]].title)
    return recommend_movies_name, recommend_movies_poster

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie to get recommendations",
    movie_list
)

if st.button("Show Recommendation"):
    recommend_movies_name, recommend_movies_poster = recommend(selected_movie)

    st.write('Recommended Movies:')
    col_count = 2
    col_width = 300  # Adjust this value based on your preference
    spacing = 30  # Adjust this value for spacing between images

    col = st.columns(col_count)
    for i in range(0, len(recommend_movies_name), col_count):
        for j in range(col_count):
            if i + j < len(recommend_movies_name):
                with col[j]:
                    st.image(recommend_movies_poster[i + j], width=col_width)
                    st.write(recommend_movies_name[i + j])
                    st.write("")  # Adding empty line for spacing between images
        st.write("")  # Adding empty line for spacing between rows
