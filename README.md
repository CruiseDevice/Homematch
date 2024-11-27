# HomeMatch: Personalized Real Estate Agent

## Overview
HomeMatch is an **AI-powered real estate application** designed to revolutionize the way potential buyers interact with property listings. By leveraging cutting-edge technologies like **Large Language Models (LLMs)** and **vector databases**. HomeMatch creates personalized property search experiences tailored to the buyers unique preferences. This project utilizes **Retrieval-Augmented Generation (RAG)** to combine semantic search and natural language generation, allowing for customized, engaging property descriptions that resonates with users.

## Features
- **Personalized Property Listings**: Generates natural, buyer-specific descriptions based on user preferences.
- **Semantic Search**: Matches buyer preferences to relevant property listings using a vector database.
- **Customizable Input**: Accepts preferences in natural language, making the interface intuitive for non-technical users.
- **Accurate and Relevant Results**: Ensures property details are factually correct while emphasizing aspects that matter most to the buyer.
- **Scalable Data**: Handles large datasets of real estate listings using vector-based search.

## Technologies Used
- **Large Language Model (LLM)**: OpenAI's GPT-3.5-turbo for generating descriptions and handling user input.
- **Vector Database**: ChromaDB for storing and performing semantic searches on property listing embeddings.
- **LangChain**: For efficient integration of LLMs and vector embeddings.

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `bash pip install -r requirements.txt`
3. Set your OpenAI API key in .env file
4. Run the application: `python main.py` or `python3 main.py`

