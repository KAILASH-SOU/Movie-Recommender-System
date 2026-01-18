import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "movies_cleaned.csv"


@st.cache_resource(show_spinner=False)
def load_recommender():
    df = pd.read_csv(DATA_PATH)

    tfidf = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = tfidf.fit_transform(df["tags"]).toarray()
    similarity = cosine_similarity(vectors)

    return df, similarity


def recommend(movie_title, top_n=5):
    df, similarity = load_recommender()

    if movie_title not in df["title"].values:
        return []

    idx = df[df["title"] == movie_title].index[0]
    distances = similarity[idx]

    movie_indices = np.argsort(distances)[::-1][1:top_n + 1]
    return df.iloc[movie_indices]["title"].tolist()
