from fastapi import FastAPI, Query, HTTPException
from src.models.similarity import recommend

app = FastAPI(
    title="Movie Recommendation API",
    description="Content-based movie recommender using TMDB dataset",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/recommend")
def get_recommendations(
    movie: str = Query(..., description="Movie title"),
    top_n: int = Query(5, ge=1, le=10)
):
    recommendations = recommend(movie, top_n)

    if not recommendations:
        raise HTTPException(
            status_code=404,
            detail=f"Movie '{movie}' not found in database"
        )

    return {
        "input_movie": movie,
        "recommendations": recommendations
    }
