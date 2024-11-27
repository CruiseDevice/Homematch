import re
import json
from langchain_openai import OpenAIEmbeddings
from vector_store.initialize_vector_db import initialize_vector_db


def extract_listings_info(listings_text):
    # Define a regex pattern to capture each property listing, its description, and its neighborhood
    pattern = r"### \d+\.\s+(.+?)\n- \*\*Neighborhood:\*\* (.+?)\n- \*\*Price:\*\* (.+?)\n- \*\*Bedrooms/Bathrooms:\*\* (.+?)\n- \*\*House Size:\*\* (.+?)\n\n\*\*Description:\*\* (.+?)\n\n\*\*Neighborhood:\*\* (.+?)(?=\n---|\Z)"

    # Use re.findall to extract all matches of the pattern
    matches = re.findall(pattern, listings_text, re.DOTALL)

    listings_info = []
    for match in matches:
        title, neighborhood, price, bed_bath, house_size, description, neighborhood_description = match
        listings_info.append({
            "title": title.strip(),
            "neighborhood": neighborhood.strip(),
            "price": price.strip(),
            "bedrooms_bathrooms": bed_bath.strip(),
            "house_size": house_size.strip(),
            "description": description.strip(),
            "neighborhood_description": neighborhood_description.strip()
        })
    return listings_info


def generate_and_store_embeddings(listings_file):
    with open(listings_file, "r") as f:
        listings = json.load(f)

    embeddings = OpenAIEmbeddings()
    collection = initialize_vector_db()

    listings_info = extract_listings_info(listings)
    for listing in listings_info:
        vector = embeddings.embed_query(listing["description"])
        collection.add(
            documents=[listing["description"]],
            metadatas=[listing],
            ids=[listing["neighborhood"]]
        )