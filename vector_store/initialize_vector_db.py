import chromadb
from chromadb.config import Settings


def initialize_vector_db():
    client = chromadb.Client(Settings())
    # check if the collection already exists
    collection = client.get_or_create_collection("real_estate_listings")
    return collection


def query_vector_db(user_query, n_results=5):
    collection = initialize_vector_db()
    results = collection.query(
        query_texts=[user_query],
        n_results=n_results
    )

    return [metadata for metadata in results['metadatas']]