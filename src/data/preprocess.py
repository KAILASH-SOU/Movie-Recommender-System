import pandas as pd
import ast
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def load_data():
    movies = pd.read_csv(RAW_DIR / "tmdb_5000_movies.csv")
    credits = pd.read_csv(RAW_DIR / "tmdb_5000_credits.csv")
    return movies, credits


def parse_json(col):
    return [d['name'] for d in ast.literal_eval(col)]


def preprocess():
    movies, credits = load_data()

   
    df = movies.merge(credits, left_on='id', right_on='movie_id')

   
    df = df[['id', 'title_x', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    df.rename(columns={'title_x': 'title'}, inplace=True)

    
    df.dropna(inplace=True)

   
    df['genres'] = df['genres'].apply(parse_json)
    df['keywords'] = df['keywords'].apply(parse_json)

    df['cast'] = df['cast'].apply(
        lambda x: [i['name'] for i in ast.literal_eval(x)[:3]]
    )

    def fetch_director(crew):
        for member in ast.literal_eval(crew):
            if member['job'] == 'Director':
                return member['name']
        return ""

    df['director'] = df['crew'].apply(fetch_director)

    
    df['tags'] = (
        df['overview'].apply(lambda x: x.split()) +
        df['genres'] +
        df['keywords'] +
        df['cast'] +
        df['director'].apply(lambda x: x.split())
    )

    df['tags'] = df['tags'].apply(lambda x: " ".join(x).lower())

    df = df[['id', 'title', 'tags']]

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "movies_cleaned.csv", index=False)

    print(" Preprocessing completed successfully")


if __name__ == "__main__":
    preprocess()
