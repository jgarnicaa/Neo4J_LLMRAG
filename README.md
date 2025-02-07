# Neo4J_LLMRAG

This project is an interactive web application that combines **Neo4j**, a powerful graph database, and a **Large Language Model (LLM)** accessible via the **Together API**. The application allows users to query a movie database and receive AI-generated responses based on data retrieved from the graph database.

## Objectives
- Understand how to connect and query a **Neo4j** database.
- Learn to use **Streamlit** to create an interactive web application.
- Integrate an **LLM using the Together API** to generate natural language responses.
- Implement **Retrieval-Augmented Generation (RAG)** by combining real-time data retrieval with language model generation.

## Features

- **Neo4J as a graph database** for structured and efficient data storage.
- **Streamlit interface** for user-friendly interaction.
- **LLM integration** to enhance information retrieval.
- **Optimized RAG pipeline** for efficient queries.
- **Natural language query support** for an intuitive experience.

## Installation

### Requirements
- Python 3.8+
- Neo4J Community or Enterprise
- Dependencies listed in `requirements.txt`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/jgarnicaa/Neo4J_LLMRAG.git
   cd Neo4J_LLMRAG
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure Neo4J and ensure it is running.
5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage
- Adjust Neo4J connection parameters in `config.py`.
- Enter natural language queries to get LLM-generated responses.
- Explore the movie database through the Streamlit interface.
- Visualize relationships and structures using the Neo4J Browser.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For questions or suggestions, feel free to open an issue or contact the author.

