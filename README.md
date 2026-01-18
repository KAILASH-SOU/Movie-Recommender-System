flowchart TB
    %% User Layer
    U[👤 User]

    %% Frontend
    S[🎬 Streamlit UI<br/>streamlit_app/app.py]

    %% Backend Logic
    R[🧠 Recommendation Engine<br/>TF-IDF + Cosine Similarity]

    %% Model & Data
    M[(📦 Trained Model<br/>recommender.pkl)]
    D1[(📁 Raw Data<br/>TMDB CSVs)]
    D2[(📁 Processed Data<br/>movies_cleaned.csv)]

    %% MLOps
    G[🐙 GitHub Repository]
    DVC[DVC Pipeline<br/>ingest → preprocess → train]

    %% Flow
    U --> S
    S --> R
    R --> M

    D1 --> DVC
    DVC --> D2
    D2 --> DVC
    DVC --> M

    G --> S
    G --> R
    G --> DVC
