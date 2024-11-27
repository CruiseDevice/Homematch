import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def personalize_description(listing, preferences):
    prompt = f"""
    Based on the following buyer preferences:
    {preferences},
    Rewrite the listing description to highlight these preferences without altering factual details:
    {listing['description']}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content