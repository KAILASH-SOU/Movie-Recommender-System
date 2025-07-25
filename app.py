import pickle
import streamlit as st

# ========== Recommendation Logic ==========
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# ========== Load Models ==========
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

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
