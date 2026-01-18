import streamlit as st
from pathlib import Path


import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.models.similarity import recommend


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)


st.title("Movie Recommendation System")
st.write("Content-based recommendations using the TMDB 5000 dataset")

st.markdown("---")

movie_name = st.text_input(
    "Enter a movie name",
    placeholder="e.g. The Dark Knight"
)

top_n = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Recommend"):
    if not movie_name.strip():
        st.warning(" Please enter a movie name")
    else:
        with st.spinner("Finding similar movies..."):
            try:
                recommendations = recommend(movie_name, top_n)

                if not recommendations:
                    st.error("Movie not found in database")
                else:
                    st.success("Recommendations found ")
                    for i, movie in enumerate(recommendations, start=1):
                        st.write(f"{i}. {movie}")

            except FileNotFoundError:
                st.error(
                    " Model file not found. "
                    "Ensure `models/recommender.pkl` exists in the repository."
                )
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")

st.markdown("---")
st.caption("Built with  using Streamlit, Scikit-learn & TMDB dataset")
