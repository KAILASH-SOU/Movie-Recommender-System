import pandas as pd
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PROCESSED_DIR = Path("data/processed")
MODEL_DIR = Path("models")

DATA_FILE = PROCESSED_DIR / "movies_cleaned.csv"
MODEL_FILE = MODEL_DIR / "recommender.pkl"


def train():
    df = pd.read_csv(DATA_FILE)

    tfidf = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = tfidf.fit_transform(df["tags"]).toarray()
    similarity = cosine_similarity(vectors)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    artifact = {
        "movies": df,
        "tfidf": tfidf,
        "similarity": similarity
    }

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(artifact, f)

    print(" Model training completed")
    print(f"Model saved at: {MODEL_FILE}")


if __name__ == "__main__":
    train()
