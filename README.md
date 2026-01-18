```flowchart TD
    %% User Interaction Flow
    User[User] --> Streamlit[Streamlit UI]
    Streamlit --> Engine[Recommendation Engine]
    Engine --> Model[Trained Model]

    %% Data Pipeline Flow
    RawData[(TMDB Raw Data)] --> DVC{DVC Pipeline}
    DVC --> ProcessedData[Processed Data]
    ProcessedData --> Model

    %% Styling
    style RawData fill:#f9f,stroke:#333,stroke-width:2px
    style Model fill:#bbf,stroke:#333,stroke-width:2px
    style Streamlit fill:#dfd,stroke:#333,stroke-width:2px
```
