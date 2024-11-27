from dotenv import load_dotenv
import os
from openai import OpenAI
import json

# Load environment from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def generate_listings(output_file):
    prompt = """
    Create 10 diverse real estate property listings with the following details:
    - Neighborhood, price, number of bedrooms/bathrooms, house size
    - A unique description highlighting the property's features.
    - An additional description about the neighborhood.
    """
    if os.path.exists(output_file) and os.path.getsize(output_file):
        print("Listings already exist. Skipping generation...")
        return

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": prompt},
        ]
    )
    listings = response.choices[0].message.content
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # save listings to a json file
    with open(output_file, "w") as f:
        json.dump(listings, f)

