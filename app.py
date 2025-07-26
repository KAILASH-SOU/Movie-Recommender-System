import pickle
import streamlit as st
import gdown
import os

# ========== Download Pickle Files if Not Exists ==========
movie_url = 'https://drive.google.com/file/d/1-D0Xe33hJgFUWRn6mKFUTelaXv57Pscf/view?usp=sharing'
similarity_url = 'https://drive.google.com/file/d/194CMNVqbv8t-hzxgkOK3qRg4tV69mTbk/view?usp=drive_link'

if not os.path.exists('movie_list.pkl'):
    gdown.download(movie_url, 'movie_list.pkl', quiet=False)

if not os.path.exists('similarity.pkl'):
    gdown.download(similarity_url, 'similarity.pkl', quiet=False)

# ========== Load Models ==========
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ========== Recommendation Logic ==========
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# ========== Streamlit UI ==========
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title('🎬 Movie Recommender System')
st.write("Select a movie to get content-based recommendations.")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button('Show Recommendations'):
    recommended_names = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for i, name in enumerate(recommended_names, start=1):
        st.write(f"{i}. {name}")
