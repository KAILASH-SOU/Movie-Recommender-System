import pickle
import numpy as np
from pathlib import Path

MODEL_PATH = Path("models/recommender.pkl")

with open(MODEL_PATH, "rb") as f:
    artifact = pickle.load(f)

movies = artifact["movies"]
similarity = artifact["similarity"]


def recommend(movie_title, top_n=5):
    if movie_title not in movies["title"].values:
        return []

    idx = movies[movies["title"] == movie_title].index[0]

    distances = similarity[idx]
    movie_indices = np.argsort(distances)[::-1][1:top_n + 1]

    recommendations = movies.iloc[movie_indices]["title"].tolist()
    return recommendations
