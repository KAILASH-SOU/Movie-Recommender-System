



```mermaid
flowchart TD
    %% Nodes
    User[User]
    Streamlit[Streamlit UI]
    Engine[Recommendation Engine]
    Model[Trained Model]
    RawData[(TMDB Raw Data)]
    DVC{DVC Pipeline}
    ProcessedData[Processed Data]

    %% Connections
    User --> Streamlit
    Streamlit --> Engine
    Engine --> Model
    RawData --> DVC
    DVC --> ProcessedData
    ProcessedData --> Model

    %% Colors
    style User fill:#FF9999,stroke:#333,stroke-width:2px
    style Streamlit fill:#99FF99,stroke:#333,stroke-width:2px
    style Engine fill:#99FFFF,stroke:#333,stroke-width:2px
    style Model fill:#9999FF,stroke:#333,stroke-width:2px
    style RawData fill:#FFCC99,stroke:#333,stroke-width:2px
    style DVC fill:#FFFF99,stroke:#333,stroke-width:4px
    style ProcessedData fill:#E5CCFF,stroke:#333,stroke-width:2px

