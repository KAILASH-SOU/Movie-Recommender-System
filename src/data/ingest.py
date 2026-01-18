import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

MOVIES_FILE = RAW_DIR / "tmdb_5000_movies.csv"
CREDITS_FILE = RAW_DIR / "tmdb_5000_credits.csv"


def validate_movies(df: pd.DataFrame):
    required_cols = {
        "id",
        "title",
        "overview",
        "genres",
        "keywords"
    }
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f" Missing columns in movies file: {missing}")


def validate_credits(df: pd.DataFrame):
    required_cols = {
        "movie_id",
        "cast",
        "crew"
    }
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f" Missing columns in credits file: {missing}")


def ingest():
    if not MOVIES_FILE.exists():
        raise FileNotFoundError(f" {MOVIES_FILE} not found")

    if not CREDITS_FILE.exists():
        raise FileNotFoundError(f" {CREDITS_FILE} not found")

    movies = pd.read_csv(MOVIES_FILE)
    credits = pd.read_csv(CREDITS_FILE)

    validate_movies(movies)
    validate_credits(credits)

    print(" Raw data ingestion successful")
    print(f"Movies shape: {movies.shape}")
    print(f"Credits shape: {credits.shape}")


if __name__ == "__main__":
    ingest()
