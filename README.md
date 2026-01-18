



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

    %% High-Contrast Styling (Black Text for Visibility)
    style User fill:#FF9999,stroke:#333,stroke-width:2px,color:#000
    style Streamlit fill:#99FF99,stroke:#333,stroke-width:2px,color:#000
    style Engine fill:#99FFFF,stroke:#333,stroke-width:2px,color:#000
    style Model fill:#9999FF,stroke:#333,stroke-width:2px,color:#000
    style RawData fill:#FFCC99,stroke:#333,stroke-width:2px,color:#000
    style DVC fill:#FFFF99,stroke:#333,stroke-width:4px,color:#000
    style ProcessedData fill:#E5CCFF,stroke:#333,stroke-width:2px,color:#000

