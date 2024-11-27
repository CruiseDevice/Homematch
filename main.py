from personalization.generate_listings import generate_listings
from personalization.preference_parser import parse_preferences
from personalization.personalize_description import personalize_description
from vector_store.store_embeddings import generate_and_store_embeddings
from vector_store.initialize_vector_db import query_vector_db


def main():
    # Generate real estate listings and save to file
    listings_path = "data/listings.json"
    generate_listings(listings_path)

    # initialize vector database and store embeddings
    generate_and_store_embeddings(listings_path)

    # Collect user preferences (hardcoded for simplicity)
    preferences = {
        "house_size": "2,500 sqft",
        "top_features": "Quiet neighborhood, good schools, large backyard",
        "desired_amenities": "Community pool, gym, near parks",
        "location": "Suburban with access to urban areas",
        "budget": "$600,000 - $800,000"
    }

    # parse preferences into a search query
    user_query = parse_preferences(preferences)

    results = query_vector_db(user_query)

    personalized_listings = [
        {
            **listing,
            "Personalized Description": personalize_description(listing, preferences)
        } for listing_group in results for listing in listing_group
    ]

    # Display the personalized listings
    print(f"User Query:\n{user_query}")
    for idx, listing in enumerate(personalized_listings, start=1):
        print(f"--- Listing {idx} ---")
        print(f"Neighborhood: {listing['neighborhood']}")
        print(f"Personalized Description: {listing['Personalized Description']}")


if __name__ == "__main__":
    main()